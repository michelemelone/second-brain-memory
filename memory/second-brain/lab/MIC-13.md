# MIC-13: Decide how the Gantry memory reaches the Second Brain

- Project: Second Brain
- Status: done
- Priority: low
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

Gantry must never read the Second Brain, but its own memory may be summarised into it. Decide the direction and the filter, then write it down. Needs Michele.

## Last report of the agent

**Report MIC-13**

**Done**
- I recorded your decision as `wiki/gantry-memory-excluded.md`: for now, Gantry's memory stays out of the Second Brain.
- The page says there is no direction, no filter and no allowed paths, because nothing flows. It also says Gantry still never reads the Second Brain.
- It lists the options for later: Gantry exports, Sirius pulls, or manual summaries on request. It suggests an allowlist plus a secrets check if you reopen this.
- I committed and pushed it (`caef37c`).

**Not done**
- I did not create `memory/gantry/`.
- I did not write any script.
- I did not ask which Gantry paths count as its memory, since that is moot for now.

**Assumed**
- "For now" means this stays closed until you ask to reopen it.

**Left for you**
- Nothing.

How to check: open `wiki/gantry-memory-excluded.md`, or run `git log -1` in `second-brain`.
