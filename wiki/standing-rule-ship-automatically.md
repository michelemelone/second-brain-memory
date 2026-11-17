---
type: preference
updated: 2026-11-17
sources:
  - MIC-179 (owner instruction, 2026-11-17)
---
# Standing rule: ship automatically, do not ask routinely

**Preference (owner, Michele):** do not ask "approve and ship" as a routine step.

- When the tests and build pass and everything is fine, ship automatically (commit, push, build, deploy as the task allows).
- Ask the owner only on real doubt or unusual cases: a risky or hard-to-undo change, a failing check, missing information only the owner has, or a destructive or external action.
- Limits that stay in force: never force-push, never skip hooks, never read secrets, and never restart a service in the middle of a reply (see the Lab rules).
- Applies to every agent and every project.

Related: [[gantry-memory-excluded]]
