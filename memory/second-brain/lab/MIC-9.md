# MIC-9: Point bigMike memory at the Second Brain and retire the old Settings memory screens

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

bigMike's memory config, docs and readers use the Second Brain paths (the old paths are symlinks today). Once the app covers the same needs, remove the memory screens from Settings.

## Last report of the agent

**What's missing to close MIC-9:** only one thing, the question box in bigMike's Memory screen. That work is tracked in MIC-7.

**Done (from the thread, not re-checked in this run):**
- bigMike's config, docs and readers use the Second Brain paths. This was done through `.env`.
- The memory screens are gone from Settings, along with their components and tests.
- The server endpoints are kept, because the Second Brain app uses them.

**Left:**
- bigMike's question box, which answers questions over the new memory layout. It belongs to MIC-7, not to this task.

**Needs your decision:** MIC-9 can't be fully closed until MIC-7 is done. You can:
- **A)** Keep MIC-9 open and close it together with MIC-7.
- **B)** Close MIC-9 now as "paths moved, Settings screens retired", and track the question box only in MIC-7. This is cleaner, because nothing else in MIC-9 is left.

I'd choose B. Which do you want?

**What I did not do:** change any code, or confirm that the old symlinks can be removed.

**How to check:** open Settings in bigMike and confirm there is no memory section. Then check that the `.env` memory paths point into `second-brain/`.
