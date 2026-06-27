#!/usr/bin/env python3
"""
AWS AIP-C01 practice exam — tiny local app.

Run:  python3 app.py   (or double-click "Start AWS Quiz.command" / "AWS Quiz.app")

It serves index.html on http://localhost:8000, loads the question bank from
questions.json, and saves every attempt as a CSV in ./results/.
No third-party packages — Python 3 standard library only.

You normally won't need to edit this file. To change questions, edit questions.json.
"""
import csv, io, json, os, sys, threading, webbrowser
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
QDIR = os.path.join(HERE, "questions")
QFILES = {
    "easy": os.path.join(QDIR, "questions_easy.json"),
    "hard": os.path.join(QDIR, "questions_hard.json"),
    "veryhard": os.path.join(QDIR, "questions_veryhard.json"),
}
# Back-compat: fall back to the original single bank if a difficulty file is missing.
QFILE_FALLBACK = os.path.join(QDIR, "questions.json")
INDEX = os.path.join(HERE, "index.html")
PORT = int(os.environ.get("PORT", "8000"))

CSV_COLUMNS = ["attempt_id", "finished_at", "difficulty", "question_id", "task",
               "task_name", "type", "source", "status", "flagged", "your_answer",
               "correct_answer", "selected_idx", "correct_idx", "question", "explanation"]


def _norm_difficulty(d):
    d = (d or "easy").lower()
    return d if d in QFILES else "easy"


def _bank_path(difficulty):
    path = QFILES[_norm_difficulty(difficulty)]
    if not os.path.isfile(path) and os.path.isfile(QFILE_FALLBACK):
        return QFILE_FALLBACK
    return path


def load_bank(difficulty="easy"):
    with open(_bank_path(difficulty), encoding="utf-8") as f:
        return json.load(f)


def grade(bank, question_ids, answers, difficulty="easy", flagged=None):
    """Build CSV rows + summary. Unanswered questions are recorded but NOT counted as wrong."""
    by_id = {q["id"]: q for q in bank["questions"]}
    tasks = bank.get("tasks", {})
    difficulty = _norm_difficulty(difficulty)
    flagged = set(flagged or [])
    rows, correct = [], 0
    answered = 0
    for qid in question_ids:
        q = by_id.get(qid)
        if not q:
            continue
        opts = q["options"]
        correct_idx = [i for i, o in enumerate(opts) if o.get("correct")]
        sel = answers.get(qid)
        sel = sorted(sel) if sel else []
        if sel:
            answered += 1
            is_correct = (sel == sorted(correct_idx))
            status = "correct" if is_correct else "incorrect"
            if is_correct:
                correct += 1
        else:
            status = "unanswered"
        rows.append({
            "difficulty": difficulty,
            "question_id": qid,
            "task": q["task"],
            "task_name": tasks.get(q["task"], {}).get("name", ""),
            "type": q["type"],
            "source": q.get("source", ""),
            "status": status,
            "flagged": "yes" if qid in flagged else "",
            "your_answer": " | ".join(opts[i]["text"] for i in sel),
            "correct_answer": " | ".join(opts[i]["text"] for i in correct_idx),
            "selected_idx": ";".join(map(str, sel)),
            "correct_idx": ";".join(map(str, correct_idx)),
            "question": q["question"],
            "explanation": " ".join(opts[i].get("explanation", "") for i in correct_idx).strip(),
        })
    summary = {
        "total": len(rows),
        "answered": answered,
        "correct": correct,
        "incorrect": answered - correct,
        "unanswered": len(rows) - answered,
        "flagged": sum(1 for r in rows if r["flagged"] == "yes"),
        "pct": round(correct / answered * 100) if answered else 0,
        "passPct": bank.get("passPct", 75),
        "difficulty": difficulty,
    }
    return rows, summary


def write_csv(attempt_id, rows):
    os.makedirs(RESULTS, exist_ok=True)
    finished = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = os.path.join(RESULTS, "attempt_%s.csv" % attempt_id)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        w.writeheader()
        for r in rows:
            r = dict(r, attempt_id=attempt_id, finished_at=finished)
            w.writerow(r)
    return os.path.basename(path), finished


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summarize_rows(rows):
    answered = [r for r in rows if r["status"] in ("correct", "incorrect")]
    correct = sum(1 for r in rows if r["status"] == "correct")
    return {
        "total": len(rows),
        "answered": len(answered),
        "correct": correct,
        "incorrect": len(answered) - correct,
        "unanswered": len(rows) - len(answered),
        "flagged": sum(1 for r in rows if (r.get("flagged") or "") == "yes"),
        "pct": round(correct / len(answered) * 100) if answered else 0,
        "finished_at": rows[0]["finished_at"] if rows else "",
        "difficulty": (rows[0].get("difficulty") or "easy") if rows else "easy",
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet console
        pass

    def _send(self, code, body, ctype="application/json", extra=None):
        if isinstance(body, (dict, list)):
            body = json.dumps(body)
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _file(self, path, ctype):
        try:
            with open(path, "rb") as f:
                self._send(200, f.read(), ctype, {"Cache-Control": "no-store"})
        except FileNotFoundError:
            self._send(404, {"error": "not found: %s" % os.path.basename(path)})

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._file(INDEX, "text/html; charset=utf-8")
        if u.path.startswith("/questions_") and u.path.endswith(".json"):
            diff = u.path[len("/questions_"):-len(".json")]
            if diff in QFILES:
                return self._file(_bank_path(diff), "application/json; charset=utf-8")
        if u.path == "/questions.json":  # back-compat -> easy bank
            return self._file(_bank_path("easy"), "application/json; charset=utf-8")
        if u.path == "/api/attempts":
            out = []
            if os.path.isdir(RESULTS):
                for name in os.listdir(RESULTS):
                    if name.endswith(".csv"):
                        try:
                            rows = read_csv(os.path.join(RESULTS, name))
                            out.append(dict(summarize_rows(rows), file=name))
                        except Exception:
                            pass
            out.sort(key=lambda a: a.get("finished_at", ""), reverse=True)
            return self._send(200, out)
        if u.path == "/api/attempt":
            name = (parse_qs(u.query).get("file") or [""])[0]
            if "/" in name or "\\" in name or not name.endswith(".csv"):
                return self._send(400, {"error": "bad file"})
            path = os.path.join(RESULTS, name)
            if not os.path.isfile(path):
                return self._send(404, {"error": "no such attempt"})
            rows = read_csv(path)
            return self._send(200, {"file": name, "summary": summarize_rows(rows), "rows": rows})
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        u = urlparse(self.path)
        if u.path == "/api/shutdown":
            self._send(200, {"ok": True})
            threading.Thread(target=self.server.shutdown, daemon=True).start()
            return
        if u.path == "/api/save":
            length = int(self.headers.get("Content-Length", "0"))
            try:
                payload = json.loads(self.rfile.read(length) or b"{}")
            except Exception:
                return self._send(400, {"error": "bad json"})
            attempt_id = "".join(c for c in str(payload.get("attempt_id", "")) if c.isalnum() or c in "_-")
            if not attempt_id:
                attempt_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            difficulty = _norm_difficulty(payload.get("difficulty"))
            try:
                bank = load_bank(difficulty)  # reload so newly added questions grade correctly
                rows, summary = grade(bank, payload.get("question_ids", []), payload.get("answers", {}),
                                      difficulty, payload.get("flagged", []))
                fname, finished = write_csv(attempt_id, rows)
            except Exception as e:
                return self._send(500, {"error": str(e)})
            return self._send(200, {"ok": True, "file": fname, "finished_at": finished, "summary": summary})
        return self._send(404, {"error": "not found"})


def main():
    global PORT
    os.makedirs(RESULTS, exist_ok=True)
    for _ in range(20):  # find a free port starting at PORT
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
            break
        except OSError:
            PORT += 1
    else:
        print("Could not bind a port."); sys.exit(1)
    url = "http://localhost:%d/" % PORT
    print("AWS quiz running at %s   (Ctrl+C or the 'Quit' button to stop)" % url)
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("\nStopped.")


if __name__ == "__main__":
    main()
