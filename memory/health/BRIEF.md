# Health: brief
Updated: 2026-11-18 · Refresh: see "Refresh" at the end · Contract: `memory/README.md`
Sources: `health/CLAUDE.md`, `health/scripts/README.md`, `health/scripts/restart.sh`, `health/current-state.md` (via wiki), wiki `projects/health`, `decisions/health-energy-model-garmin-burn`, `decisions/strict-two-decimal-weights`, `decisions/per-food-breakdown-in-reports`, `memory/health/<YYYY-MM>.md`. Lab history of this app: none yet (`memory/health/lab/` empty).

## What it is
Michele's personal health workspace and web portal: weight and body measures, Jab (tirzepatide) log, meals and nutrition, Garmin/Xiaomi tracker data, training analysis, and an "Ask AI" chat. Not a medical device; nobody here is a licensed professional (`health/CLAUDE.md`).

## Stack and where the code lives
- Repo `/home/beedme/data/workspace/health`. Python scripts in `scripts/` build a responsive static page `portal/index.html` (git-ignored) from CSVs; `scripts/health_server.py` serves it plus a write API `/api/<kind>`, port 8765 (`scripts/restart.sh`).
- Chat: `chat_worker.py` runs on the host via a systemd user path unit and calls `claude -p` in the repo (`scripts/README.md`).
- Garmin sync hourly (`garmin_sync.py`); Xiaomi import `import_xiaomi_export.py`.

## Where the data lives
CSVs under `health/data/` (weight, jabs, nutrition, `tracker/` Garmin+Xiaomi), journal in `health/journal/YYYY-MM.md`, state in `health/current-state.md`. Raw exports in `data/<source>/raw/` (git-ignored, never delete). Raw data stays in the app; here only monthly summaries `memory/health/<YYYY-MM>.md` (generated, no AI).

## Current state
Jab 2.5 mg weekly since 2026-09-22; goal weight 85 kg (to confirm with the doctor; one note says 88). Details are in `current-state.md`, not copied here (wiki `projects/health`). Test suite: unknown, no `tests/` folder found.

## Decisions that constrain changes
- Energy model: burned = Garmin total only; no TEF/TDEE (`decisions/health-energy-model-garmin-burn`).
- Every weight shown with two decimals, no rounding (`decisions/strict-two-decimal-weights`).
- Nutrition always per single food (`decisions/per-food-breakdown-in-reports`).
- Never hand-edit CSVs: log with `scripts/log_entry.py <kind> '<json>'`; correct by a new row, never delete (`CLAUDE.md`).
- Training only from Garmin (workouts.csv retired); `exercise_sets.csv` and `tracker_daily` are derived, rebuild with `build_exercises.py` / `build_tracker_daily.py`.
- UI "Mounjaro" is now "Jab"; internal files `jab_*` (wiki `projects/health`, 2026-10-26).
- Dose changes only by the doctor; warn on warning signs (`CLAUDE.md`).

## Recent work (no Lab keys yet; from the wiki)
- 2026-11-15 Energy tab shows kcal/day over the active period.
- 2026-11-13 Daily analysis on demand (7/30/90/365 days); two-decimal weights.
- 2026-11-13 Ask bigMike chat aligned with bigMike status and light theme.
- 2026-11-09 Multi-tracker architecture (`tracker/`): Garmin wins on overlapping days.

## Known pitfalls
- Today's Garmin row and meals are partial: only closed days count (`scripts/README.md`).
- Embedded bigMike chat must run with the light theme (wiki 2026-11-13).
- Portal is generated: after changing scripts/CSVs rebuild `build_portal.py`.

## How to verify and restart
Restart: `health/scripts/restart.sh` (port 8765, log `logs/portal-server.log`); in a Lab task use `bigmike-restart "Health portal" --task <KEY>`. Verify: open `http://127.0.0.1:8765`. Unit tests: unknown.

Refresh: after a Lab task of Health finishes, or on request, update this file from itself (compress, do not restart from zero).
