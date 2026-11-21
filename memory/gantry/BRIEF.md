# Gantry: brief
Updated: 2026-11-21 · Refresh: see end · Contract: `memory/README.md`
Sources: `gantry/programs/README.md`, `servicenow_ai/gantry/README.md`, `servicenow_ai/build_agent/Process.md` and `agents/*.md`, `servicenow_ai/gantry/backend/src/{release,backlog,runner}`, `docs/INSTALL.md`, Lab MIC-286, 329, 361-363, 409, 415, 416, 426-432 (`lab/`).

## What it is
Michele's ServiceNow delivery portal (not Gantry Enterprise, a separate world). Requirements are filed in its Backlog; headless agents design and build them as Fluent (TypeScript) source for a dev instance. Only the owner installs, in batches.

## Stack and where the code lives
Repo `/home/beedme/data/workspace/gantry/programs` (remote GitHub `servicenow-builder`). App in `servicenow_ai/gantry/`: `backend` (Node, `npm run build` then `node dist/server.js`; tests `vitest`) and `frontend` (React/Vite). Agent prompts and the process: `servicenow_ai/build_agent/` (`Process.md`, `agents/` orchestrator, sn-architect, sn-doc, sn-builder, sn-tester, sn-release, sn-solo). Service: `gantry.service`. In-app help: `frontend/src/pages/architecture.md`.

## Where the data lives
One folder per requirement with `PBI.md` (7 sections) and `state.json` (phases, numbered runs, evidence). Location of the documentation root: unknown here. Secrets stay in the server environment.

## Current state: the batch-release process (agreed 2026-11-21)
1. The owner writes the requirement and validates it with AI (mandatory before the first run and after every change, MIC-429).
2. A run designs, runs a static check (one PASS/FAIL line per rule in the Build log), then `npm run build` (max 3 attempts) and stops at **Ready to release** (`built` done, `installed` not). No deploy, no live test (MIC-426). `sn-tester` is only a build and syntax checker.
3. **Release (N)** (Backlog toolbar, banner, application cards; disabled at 0) installs the ticked requirements: one `npm run build` and one `npm run deploy` per application, dependency order, no agent, minimal read-back, dev instance only; production and UAT are refused (MIC-427, 428).
4. The owner tests by hand with the run's "Check by hand" list.
5. Later changes go in the same PBI chat: "Update this PBI" (bug, correction, preference) or "Add sub-task (1 level)" (new functionality). A change on an installed requirement returns it to Ready to release after its next run (MIC-431).
States in the Backlog "Runs & release" column: Not built, Ready to release, Installed, Change pending.
Agents write a `Memory consulted` / `Memory applied` block (MIC-430).

## Decisions that constrain changes
- All user-facing text and code are English only.
- UI is a copy of the bigMike Lab look, dark and light, desktop and phone (MIC-286, 329).
- Numbered runs on the same PBI, edit lock during a run, Change log for every change (MIC-361, 363).
- Chat is the single entry point for changes (MIC-362); Action button only when there is something to release (MIC-415); validation gate on a released requirement (MIC-416).
- No configuration is ever changed directly on an instance; only source is.
- Second Brain rule MIC-13/303: Gantry never reads this folder; this brief was added on the owner's request in MIC-432.

## Recent work
MIC-426 to 431 built the process above; MIC-432 aligned Process.md, the prompts and the docs.

## Known pitfalls
- `.gitignore` once ignored `src/release/` (fixed to `/release/`, MIC-428): check new folders are tracked.
- `runs.test.ts` "Start run clears it" was red after MIC-416 (MIC-431 note).
- No real run has yet produced a filled `Memory consulted` block (MIC-430).
- Screenshots with real data rows were never taken (MIC-427, 431).

## How to verify and restart
`cd servicenow_ai/gantry/backend && npm test -- tests/<file>`; build both sides first. Restart only with `bigmike-restart Gantry --task <KEY>`, never directly.

Refresh: the developer of the next Gantry Lab task updates this brief from `lab/`.
