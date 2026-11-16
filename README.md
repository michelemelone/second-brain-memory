# Second Brain

One place for everything Michele's applications remember. Folders are read by every application except Gantry, which is kept apart.

| Folder | Content | Written by |
|---|---|---|
| `bigmike/` | bigMike chats and its memory wiki (own git repository, `personal-assistant-memory`) | bigMike |
| `library/` | Imported documents (books, PDFs, scans) as Markdown; each subfolder is one memory | bigMike Memory → Import, `doc-ocr` |
| `wiki/` | Cross-domain pages (people, projects, topics, decisions, preferences) linking all the others | an agent, on request |
| `finance/` | Readable summaries generated from the Finance data (planned) | a nightly generator, no AI |
| `health/` | Readable summaries generated from the Health data (planned) | a nightly generator, no AI |
| `paperclip/` | Decisions, lessons and reports of the Michele Lab agents (planned) | Paperclip agents |
| `gantry/` | Not here yet: how to bring the Gantry memory in is still to be decided | |

## Rules
- Raw data (transactions, measurements) stays in its application database; this folder holds Markdown views of it, never the source.
- Never here: credentials, `.env`, `master.key`, databases, run logs.
- The old paths still work: `personal-assistant/data/memory` and `/home/beedme/data/LLM Wiki` are symlinks into this folder.
- Gantry must never read this folder; the other applications may read all of it.
