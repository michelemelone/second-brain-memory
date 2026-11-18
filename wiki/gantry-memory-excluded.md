---
type: decision
updated: 2026-11-18
sources:
  - MIC-13 (owner answer, 2026-11-17: "for now we keep the memory of Gantry out of my second brain")
  - MIC-303 (owner, 2026-11-18: Gantry's Lab development history may live in the Second Brain)
---
# Gantry memory stays out of the Second Brain

**Decision (2026-11-17, owner):** for now, Gantry's memory is not summarised into the Second Brain.

- Direction: none. No export from Gantry, no pull by Sirius, no scheduled job.
- Filter and allowed paths: not defined, because nothing flows.
- Standing rule unchanged: Gantry never reads the Second Brain, and nothing from here is copied into Gantry.
- Narrowed by MIC-303 (2026-11-18): the only folder allowed under `memory/gantry/` is `memory/gantry/lab/`, holding ONLY the development history of Gantry in the Lab (what was asked of the agents, what they reported). It is not the memory of the Gantry application and holds none of Gantry's own data or content. Anything else under `memory/gantry/` stays forbidden.

## Revisit
Only when the owner asks. The options then are: Gantry exports to a drop folder; Sirius pulls read-only from explicit paths; or manual summaries on request. Any filter should be an allowlist plus a check for secrets and raw data.
