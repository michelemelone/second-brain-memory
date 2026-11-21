# Second Brain

One place for everything Michele's applications remember. Folders are read by every application except Gantry, which is kept apart (MIC-13).

| Folder | Content | Written by |
|---|---|---|
| `memory/bigmike/` | bigMike chats, memory wiki, and Lab task history (`lab/`) (own git repository, `personal-assistant-memory`) | bigMike |
| `memory/finance/` | Readable monthly summaries generated from Finance data | `scripts/gen_finance_summary.py` (nightly, no AI) |
| `memory/health/` | Readable monthly summaries generated from Health data | `scripts/gen_health_summary.py` (nightly, no AI) |
| `memory/cucina/` | Readable summaries of cooking sessions, sourdough, recipes, and meal plans | periodic generator or agent (planned) |
| `memory/learning-german/` | Readable summaries of German study sessions, vocabulary progress, and curriculum | periodic generator or tutor agent (planned) |
| `memory/live-camera/` | Readable summaries, observations, and transcripts of camera sessions | periodic generator or camera script (planned) |
| `memory/paperclip/` | Decisions, lessons, and reports of the Michele Lab agents | Paperclip agents |
| `memory/library/` | Imported documents (books, PDFs, scans) as Markdown; each subfolder is one memory | bigMike Memory → Import, `doc-ocr` |
| `wiki/` | Cross-domain pages (people, projects, topics, decisions, preferences) linking all the others | an agent, on request |

## Layout
- `memory/` holds everything that feeds the wiki (the sources: chats, imported documents, summaries of all applications). Each application has its dedicated folder under `memory/`.
- `wiki/` is the central cross-domain wiki, built from `memory/` by the nightly job. Sources are searchable on their own; the wiki connects and summarises them.

## Rules
- Raw data (transactions, measurements, video, audio) stays in its application database; this folder holds Markdown views of it, never the source.
- Never here: credentials, `.env`, `master.key`, databases, run logs.
- Gantry's own application memory is excluded from the Second Brain per architectural decision MIC-13 (`wiki/gantry-memory-excluded.md`), narrowed by MIC-303: the only things allowed under `memory/gantry` are `memory/gantry/lab/` (the Lab development history of Gantry) and, since MIC-432 (owner request, 2026-11-21), `memory/gantry/BRIEF.md`. Never put anything else of Gantry there.
- Symlink for backwards compatibility: `personal-assistant/data/memory` links into `memory/bigmike/`. The old `personal-assistant/data/lab-memory` symlink is removed (MIC-303).
- Lab history (MIC-303, supersedes the lab placement of MIC-196): each application keeps its own Lab task files and `INDEX.md` in `memory/<app>/lab/` (`bigmike`, `health`, `finance`, `second-brain`, `gantry`, `beedme-server`); tasks with no project are in `memory/bigmike/lab/no-project/`. One global index of every task, with the path of its file, is `memory/lab-index.md`: read it first. Written automatically by bigMike, no AI.
- Gantry must never read this folder; the other applications may read all of it.

## Application briefs (MIC-304)
Each application has one short, injectable brief: `memory/<app>/BRIEF.md`. The always-injectable index is `memory/README.md` (max 2,000 characters, one line per application).

**Contract**
- English; hard cap 4,000 characters (target 2,500-3,500); no secrets, no raw personal data (no measurements, transactions, credentials).
- Header: `Updated: YYYY-MM-DD` and `Sources:` (everything it was built from).
- Sections, in this order: What it is; Stack and where the code lives; Where the data lives; Current state; Decisions that constrain changes; Recent work (last 3-5 items with task keys); Known pitfalls; How to verify and restart. End with a one-line Refresh note.
- Evidence rule: every claim comes from the Second Brain (Lab history, wiki, project documents, monthly summaries, chats) or from the application's own README/docs, and cites the task key or path. Say "unknown" instead of guessing.
- Over the cap: condense the least important parts first; never drop a decision or a pitfall, never truncate silently.

**Who refreshes it, and when:** the agent that finishes a Lab task of that application (Sirius, or the developer in the same task) updates the brief, or an explicit refresh run does. The existing brief is the input and is compressed and updated, not rewritten from zero. The inputs are the Second Brain only (`memory/<app>/lab/`, `memory/lab-index.md`, the wiki, the app's documents); the bigMike database is never read, and bigMike keeps no copy: it reads `memory/<app>/BRIEF.md` (injection is MIC-305).

**Gantry** has a brief since MIC-432 (owner request, narrowing MIC-13 and MIC-303): `memory/gantry/BRIEF.md`, written from the code and the Lab history only. Gantry itself still never reads this folder.
