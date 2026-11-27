# Memory: global index (always injectable)
Updated: 2026-11-27. One line per application: what it is, and the brief to read first. Task history of all apps: `memory/lab-index.md`. Gantry: brief and Lab history only in Markdown (MIC-13, MIC-432); operational data (no secrets) goes to the warehouse.

**Data source rule:** `memory/warehouse/warehouse.sqlite` (documented in `memory/warehouse/SCHEMA.md`) is the central source for ANY question on application data (atomic rows across all apps). Markdown is only for chats, wiki, briefs, Lab history, and documents.

| App | What it is | Read first |
|---|---|---|
| bigMike | Personal assistant chat + Lab (task backoffice) | `bigmike/BRIEF.md` |
| Gantry | ServiceNow delivery portal: batch-release process | `gantry/BRIEF.md` |
| Second Brain | This vault and its web app (Memory) | `second-brain/BRIEF.md` |
| Health | Weight, Jab, meals, Garmin portal | `health/BRIEF.md` |
| Finance | Ledger web app: bank/card transactions | `finance/BRIEF.md` |
| Mail | Multi-account Gmail triage, clean-up, drafts | `mail/BRIEF.md` |
| Cucina | Cooking, sourdough, meal plans | none yet: `cucina/` |
| Learning German | German study and vocabulary | none yet: `learning-german/` |
| Live camera | Camera sessions and transcripts | none yet: `live-camera/` |
| Beedme server | Home server operations | none yet: `beedme-server/lab/` |

Briefs: `memory/<app>/BRIEF.md`, max 4,000 characters, rules in `second-brain/README.md`.
