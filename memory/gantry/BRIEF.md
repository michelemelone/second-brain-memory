# Gantry: brief
Updated: 2026-11-25 · Refresh: see end · Contract: `memory/README.md`
Sources: `gantry/programs/README.md`, `servicenow_ai/gantry/README.md`, `servicenow_ai/build_agent/Process.md` and `agents/*.md`, `servicenow_ai/gantry/backend/src/{release,backlog,runner}`, `docs/INSTALL.md`, Lab MIC-286, 329, 361-363, 409, 415, 416, 426-432, 462, 463, 465 (`lab/`), `gantry/backend/src/runner/runTrigger.ts`.

## What it is
Michele's ServiceNow delivery portal (not Gantry Enterprise, a separate world). Requirements are filed in its Backlog; headless agents design and build them as Fluent (TypeScript) source for a dev instance. Since 2026-11-25 a run takes a requirement end to end to Released by itself.

## Stack and where the code lives
Repo `/home/beedme/data/workspace/gantry/programs` (remote GitHub `servicenow-builder`). App in `servicenow_ai/gantry/`: `backend` (Node, `npm run build` then `node dist/server.js`; tests `vitest`) and `frontend` (React/Vite). Agent prompts and the process: `servicenow_ai/build_agent/` (`Process.md`, `agents/` orchestrator, sn-architect, sn-doc, sn-builder, sn-tester, sn-release, sn-solo). Service: `gantry.service`. In-app help: `frontend/src/pages/architecture.md`.

## Where the data lives
One folder per requirement with `PBI.md` (7 sections) and `state.json` (phases, numbered runs, evidence). Location of the documentation root: unknown here. Secrets stay in the server environment.

## Validation gate (owner decision 2026-11-26, MIC-498)
No run starts while any point of the latest validation round is open, of any severity (blocking or optional) and kind (change or question), for every caller including the bigMike service account: the server answers 409. The owner resolves each point (apply, decline, answer) or uses "Accept as is, start anyway" (round 3 on, only while a point is open; it records the open points as accepted). It replaces the MIC-437 rule where only blocking points locked the run.

## Current state: end-to-end release (owner decision 2026-11-25, option A)
Every requirement goes end to end through its own worktree to **Released**, with no manual step and no automated live test (MIC-462 backend, MIC-463 UI, MIC-465 docs). It replaces the batch model of 2026-11-21 (MIC-426..MIC-432: stop at "Ready to release", **Release (N)** button), kept here only as history.
1. The owner writes the requirement and validates it with AI (mandatory before the first run and after every change, MIC-429), then starts the run.
2. The agent designs, runs the static check (one PASS/FAIL line per rule in the Build log, cross-scope checks included) and `npm run build` (max 3 attempts); its part ends at `built`. `sn-tester` is only a build and syntax checker.
3. Gantry then goes on in the same run, with no agent: installs from the requirement's own worktree through the integration folder (never the main folder), one deploy at a time per instance, dev instance only (production and UAT refused); a minimal read-back (artifacts exist, are active, updated at or after the deploy; sys_id and version in `state.json`); lands the branch on main only after a good read-back; section 6 and a dated Change log entry are written and the requirement is Released. It is the same numbered run.
4. A requirement that depends on an unreleased one waits and continues by itself; a failure marks nothing Released, keeps the worktree and branch, shows the reason on the card with Retry, and a failed read-back never reinstalls (MIC-440).
5. The owner does the live check by hand after the release, with the run's "Check by hand" list.
6. Later changes: same PBI chat, "Update this PBI" or "Add sub-task (1 level)"; a released requirement can be iterated many times (MIC-446) and goes through the same steps.
Board columns (MIC-463): Development = build, Test = install and read-back, Release = landed. Backlog "Runs & release" column: Not built, Installed, Change pending. A Global-scope requirement has no SDK project (its Update Set is installed by hand), so the release step stops on it with that reason (seen on #162, MIC-462).
Global-scope deletion (MIC-471): the footprint of a Global requirement reads its exported `Global/<id>_*.xml` and the delivery log `global-update-set.mjs` keeps (`.gantry/global/<id>.json`) into `platform.global.records`; a record is "created" when its own `sys_created_on` is not before the delivery started. DELETE runs `scripts/global-cleanup.mjs` (audited, dev instance only) with what it created, children first; a table and the parts of a table it created are left to check by hand (MIC-466 leftovers), and a record only modified is never touched.
Agents write a `Memory consulted` / `Memory applied` block (MIC-430).

## Decisions that constrain changes
- All user-facing text and code are English only.
- UI is a copy of the bigMike Lab look, dark and light, desktop and phone (MIC-286, 329).
- Numbered runs on the same PBI, edit lock during a run, Change log for every change (MIC-361, 363).
- Chat is the single entry point for changes (MIC-362); validation gate on a released requirement (MIC-416). The Action button of MIC-415 and the Release (N) button no longer exist (MIC-463).
- No configuration is ever changed directly on an instance; only source is.
- Second Brain rule MIC-13/303: Gantry never reads this folder; this brief was added on the owner's request in MIC-432.

## Recent work
MIC-426 to 431 built the batch process (history); MIC-462/463 replaced it with the end-to-end release; MIC-465 rewrote Process.md, the agent prompts, the help and the docs, with a prompt test (`tests/endToEndPrompts.test.ts`).

## Known pitfalls
- `.gitignore` once ignored `src/release/` (fixed to `/release/`, MIC-428): check new folders are tracked.
- `runs.test.ts` "Start run clears it" was red after MIC-416 (MIC-431 note).
- No real run has yet produced a filled `Memory consulted` block (MIC-430).
- Screenshots with real data rows were never taken (MIC-427, 431).

## How to verify and restart
`cd servicenow_ai/gantry/backend && npm test -- tests/<file>`; build both sides first. Restart only with `bigmike-restart Gantry --task <KEY>`, never directly.

Refresh: the developer of the next Gantry Lab task updates this brief from `lab/`.
