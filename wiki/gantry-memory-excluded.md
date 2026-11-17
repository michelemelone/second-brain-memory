---
type: decision
updated: 2026-11-17
sources:
  - MIC-13 (owner answer, 2026-11-17: "for now we keep the memory of Gantry out of my second brain")
---
# Gantry memory stays out of the Second Brain

**Decision (2026-11-17, owner):** for now, Gantry's memory is not summarised into the Second Brain.

- Direction: none. No export from Gantry, no pull by Sirius, no scheduled job.
- Filter and allowed paths: not defined, because nothing flows.
- Standing rule unchanged: Gantry never reads the Second Brain, and nothing from here is copied into Gantry.
- No folder such as `memory/gantry/` is created.

## Revisit
Only when the owner asks. The options then are: Gantry exports to a drop folder; Sirius pulls read-only from explicit paths; or manual summaries on request. Any filter should be an allowlist plus a check for secrets and raw data.
