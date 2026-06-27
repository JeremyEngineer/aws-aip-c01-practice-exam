# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A local, single-machine practice-exam app for the AWS Certified AI Practitioner (AIP-C01) exam. Pure Python 3 standard library on the backend, one vanilla-JS HTML file on the frontend. **No build step, no dependencies, no package manager, no test suite.**

## Run it

```bash
python3 app.py            # serves http://localhost:8000 and opens the browser
PORT=8001 python3 app.py  # override the start port
```

The server scans up to 20 ports starting at `PORT` (default 8000) until it finds a free one. Stop it with Ctrl+C or the in-app **Quit** button (which POSTs `/api/shutdown`). `Start AWS Quiz.command` (macOS) and `Start AWS Quiz.bat` (Windows) are double-click launchers that just resolve their own directory, locate Python, and run `app.py`.

## Architecture

Two files do all the work:

- **`app.py`** — a `ThreadingHTTPServer` with one `Handler`. It serves the UI and question banks as static files and exposes a tiny JSON API. **All grading happens here, server-side** (`grade()`), not in the browser — the client only sends raw selections.
- **`index.html`** — the entire UI in one file: vanilla JS, no framework, no bundler. A screen-based state machine (home/difficulty → exam → result → review) driven by a global `exam` object. Loads banks and talks to the API via `fetch`.

### HTTP API (all in `app.py`)

| Method + path | Purpose |
|---|---|
| `GET /` or `/index.html` | the UI |
| `GET /questions_<diff>.json` | a difficulty's question bank (`easy`/`hard`/`veryhard`) |
| `GET /questions.json` | back-compat alias → easy bank |
| `GET /api/attempts` | summaries of every saved CSV in `results/` |
| `GET /api/attempt?file=…` | full rows + summary for one attempt |
| `POST /api/save` | grade an attempt, write a CSV, return the summary |
| `POST /api/shutdown` | stop the server (the Quit button) |

### Question banks

Three independent files in **`questions/`** — `questions_easy.json`, `questions_hard.json`, `questions_veryhard.json` — each a self-contained JSON object with its own `tasks` map and `questions` array (top-level keys: `_comment`, `exam`, `difficulty`, `passPct`, `tasks`, `questions`). The `_comment` field documents the schema inline. Key rules:

- A question's `task` **must** be a key in the *same file's* `tasks` map (the `tasks` map supplies the "Read more on AWS" links shown in review).
- `type` is `"single"` (one correct option) or `"multi"` (≥2 correct, graded **all-or-nothing**).
- `source` is optional; when present (e.g. `"BenchPrep"`) the UI shows a badge.
- Banks are re-read on every `/api/save` and on browser reload, so **edits to questions need no server restart**.

### Results / grading semantics

- One CSV per attempt in `results/`, named `attempt_<id>.csv`. Column order is fixed by `CSV_COLUMNS` in `app.py` — keep writes and reads consistent with it.
- **Unanswered questions are recorded but never counted wrong.** Score is `correct ÷ answered`; pass threshold is the bank's `passPct` (default 75).

## Gotchas

- The HTTP path (`/questions_<diff>.json`) is independent of the on-disk path. The frontend always fetches `/questions_<diff>.json`; `app.py` maps that to `questions/…` via `QFILES`/`_bank_path()`. If you move the bank files, update `QDIR`/`QFILES` in `app.py` only — `index.html` needs no change.
- There is no automated test suite — verify changes by running `app.py` and exercising the flow in the browser.
