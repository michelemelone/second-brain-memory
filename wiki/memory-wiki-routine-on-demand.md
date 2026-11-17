---
type: decision
updated: 2026-11-17
sources:
  - MIC-14 (owner answer, 2026-11-17: Paperclip will be retired, so the routine must live inside bigMike Lab and be on demand)
---
# Memory wiki routine: on demand, inside bigMike Lab

**Decision (2026-11-17, owner):** the wiki distillation routine is not switched on as a nightly Paperclip routine.

- Paperclip will be retired, so nothing is scheduled there.
- The routine belongs inside bigMike Lab and runs on demand only (bigMike Settings → Memory → Update memory wiki).
- No nightly model call. Only the existing export and chat-sync timers stay, and they call no model.
- The paused Paperclip routine stays paused and is not resumed.

## Open for the owner
Moving the routine into bigMike Lab is a separate build task (Dragon's team). Nothing was changed outside `second-brain/`.
