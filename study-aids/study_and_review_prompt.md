You are an expert AWS instructor and assessment writer helping me prepare for the **AWS Certified Generative AI Developer – Professional (AIP-C01)** exam. You have access to my **`aws_exam_prep`** folder. Work in two phases, **in order**. Don't ask me questions first — read the folder and begin with Phase 1.

## The folder (read these before doing anything)
- `questions_easy.json` — Easy bank (~196 questions).
- `questions_hard.json` — Hard bank (~135), official practice-exam style. 20 questions are tagged `"source":"BenchPrep"` — these are the real official practice questions.
- `questions_veryhard.json` — Very Hard bank (~131); the options are deliberately close, with "no obvious answer."
- `AIP-C01_practice_questions.md` — the 20 official **BenchPrep** questions with full explanations. **This is your gold standard for style, difficulty, and accuracy** — match the others to it.
- `app.py`, `index.html` — a local quiz app that loads the three banks. **Do not modify these.**

Each question object looks like:
```json
{ "id": "1.4-13", "task": "1.4", "type": "single|multi",
  "question": "...",
  "options": [ {"text": "...", "correct": true, "explanation": "..."} ],
  "source": "BenchPrep" }
```
(`source` is optional and appears only on official questions.) Each bank also has top-level `exam`, `difficulty`, `passPct`, a `tasks` map (`{name, domain, resources:[{label,url}]}`), and a `_comment`.

---

## PHASE 1 — Build my study plan (do this first)

Create a new file **`AIP-C01_study_plan.md`** in the folder: a checklist I can tick off as I study.

1. **Find the official AIP-C01 exam guide** on AWS (use web search/fetch; check aws.amazon.com/certification and docs.aws.amazon.com). Base the plan's domains, tasks, and in-scope topics on that official guide, and **cite the exact exam-guide URL** at the top of the file. If you genuinely cannot find an official guide, say so explicitly at the top and instead derive the structure from the `tasks` maps inside the three JSON banks.
2. **Structure:** group by **Domain → Task statement → specific topics**. Render every topic as a markdown checkbox (`- [ ]`) so I can tick it off.
3. Under each topic, list the **specific AWS services/features in scope** (e.g., for RAG: Bedrock Knowledge Bases, vector stores, reranking, hybrid search, chunking strategies). **Mark high-yield, heavily tested topics with a ⭐.**
4. For every topic, add a **reference link to the official AWS documentation** it is based on (prefer docs.aws.amazon.com). Make sure the links point to real official pages.
5. Add a short "How to use this plan" intro and a one-line progress tracker per domain (e.g., `Progress: 0 / N`).

Deliver the file, then briefly tell me what you created before moving on.

---

## PHASE 2 — Review and improve the three question banks

Read all three banks. Evaluate **every** question and **edit the weak ones in place** in the JSON. Then write a changelog.

### What counts as "needs improving"
- **Factual accuracy** — verify claims against current official AWS docs; fix anything outdated or wrong (note the doc in the changelog).
- **Answer correctness** — for `single`, exactly one option is the clearly best/defensible answer; for `multi`, the correct set is unambiguous. Fix any mis-keyed answers.
- **Distractor quality** — wrong options must be plausible but clearly inferior; no throwaway or joke options. (Easy may be simpler; Hard and Very Hard must be tight.)
- **Tier fit** — Easy = approachable, mostly single-answer fundamentals; Hard = BenchPrep style (rich scenario, "LEAST/MOST overhead" framing, "select TWO", strong distractors); **Very Hard = closely competing options with no obvious answer**, where a decisive constraint in the scenario (a hard service limit, lowest overhead/cost, input-vs-output, same-vs-different model, etc.) picks the winner.
- **Exam relevance** — remove or replace obscure trivia and out-of-scope detail. Everything must plausibly appear on AIP-C01.
- **Explanations** — every option says why it is right or wrong; the correct option explains why it beats the close alternatives (especially in Very Hard).
- **Clarity** — the scenario must state the decisive constraint; fix ambiguous wording, grammar, and any question where two answers are arguably equally correct.
- **Duplicates** — flag exact duplicates within a bank (consolidate them). Near-duplicates across tiers are acceptable if the difficulty genuinely differs.

### Hard rules (do not break)
- **Never change a question's `id`.** My saved quiz results map back to questions by `id`.
- **Preserve every `"source":"BenchPrep"` tag.** For BenchPrep questions, only fix clear typos or outright errors — otherwise keep them faithful to the official set.
- Keep the schema exactly. Maintain integrity: `single` = exactly one `correct:true`; `multi` = two or more `correct:true`; **Very Hard questions must have ≥ 4 options**.
- Do not change the top-level `exam`, `difficulty`, `passPct`, or `_comment` fields. Only add a key to a bank's `tasks` map if a question truly needs a new task (include `name`, `domain`, and `resources`).
- After editing each file, **validate it** and re-check integrity, e.g.:
  `python3 -c "import json; d=json.load(open('questions_hard.json')); print(len(d['questions']))"` (repeat per file).
- **Do not modify `app.py` or `index.html`.**

### Deliverable
Write **`question_review_changelog.md`** listing, per bank: total reviewed, number changed, and for each changed question its `id`, what changed (question text / option text / keyed answer / explanation / fully replaced), and a one-line reason (with a doc link for factual fixes). End with a section listing any duplicates and any questions you recommend I review manually.

Work bank by bank (Easy → Hard → Very Hard). After each bank, tell me: **reviewed N, changed M.**
