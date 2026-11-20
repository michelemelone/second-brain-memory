# MIC-14: Switch on the nightly wiki routine after the move

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

The Second Brain knowledge wiki distillation routine is paused. Turn it on once the paths and the app are final, and check its first run.

## Last report of the agent

**Report MIC-14**

**Fatto**
- Ho registrato la tua decisione in `wiki/memory-wiki-routine-on-demand.md`. Paperclip verrà dismesso, quindi la routine non viene attivata come notturna. Deve stare dentro bigMike Lab e partire solo on demand.
- Ho fatto commit e push: `7359ef4`.

**Non fatto**
- Non ho acceso nessuna routine e non ho toccato Paperclip.
- Non ho spostato la routine in bigMike Lab. Serve un task di sviluppo separato, per il team di Dragon.

**Ipotesi**
- On demand significa il pulsante già esistente in bigMike (Impostazioni → Memory → Update memory wiki). Non ho verificato se serve altro.

**Resta a te**
- Decidere se aprire il task di sviluppo per portare la routine in bigMike Lab.
- Dire a chi gestisce Paperclip di lasciare in pausa la routine attuale.

How to check: apri `wiki/memory-wiki-routine-on-demand.md` e controlla con `git -C second-brain log -1` che il commit `7359ef4` sia sul remote.
