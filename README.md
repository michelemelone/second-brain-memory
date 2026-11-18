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
- Gantry's own application memory is excluded from the Second Brain per architectural decision MIC-13 (`wiki/gantry-memory-excluded.md`), narrowed by MIC-303: the ONLY thing allowed under `memory/gantry` is `memory/gantry/lab/`, the Lab development history of Gantry (what was asked of the agents, what they reported). Never put anything else of Gantry there.
- Symlink for backwards compatibility: `personal-assistant/data/memory` links into `memory/bigmike/`. The old `personal-assistant/data/lab-memory` symlink is removed (MIC-303).
- Lab history (MIC-303, supersedes the lab placement of MIC-196): each application keeps its own Lab task files and `INDEX.md` in `memory/<app>/lab/` (`bigmike`, `health`, `finance`, `second-brain`, `gantry`, `beedme-server`); tasks with no project are in `memory/bigmike/lab/no-project/`. One global index of every task, with the path of its file, is `memory/lab-index.md`: read it first. Written automatically by bigMike, no AI.
- Gantry must never read this folder; the other applications may read all of it.
