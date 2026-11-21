# MIC-7: App phase 4: question box (including Health and Finance summaries)

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Pegasus
- Parent: MIC-5
- Updated: 2026-11-17

## Request

A box in the app to ask questions over the whole Second Brain, using the local search first and a model only when asked. Health and Finance summaries are included; the raw data is not. Not started.

## Last report of the agent

The question box is built, committed (acc14a3) and pushed. The "Ask the model" button will not work yet, because bigMike has no `/api/memory/ask` endpoint. I haven't opened the app in a browser.

**What I did**
- **Local search:** the existing Search panel is now the question box. It uses the free `/api/search` and shows sourced excerpts, with no tokens spent.
- **Model button:** "Ask the model" appears once there are results. It sends the question and up to 20 of those excerpts to `POST /api/memory/ask`. The answer and its source links show in the panel.
- **Validation:** the app checks the request before forwarding it: the question must be non-empty and at most 2000 characters, and there can be at most 20 excerpts. It also requires the `X-Second-Brain` header.
- **Health and Finance summaries:** as you chose (2a), I added no code. The box searches the whole root, so the summaries are found once `memory/health/` and `memory/finance/` are filled.

**What I did not do**
- I did not add the bigMike endpoint. It is in a different repository and needs its own task. Until it exists, the button shows an error like "The model could not answer: bigMike answered 404".
- I did not export the Health and Finance summaries. Those folders are still empty, so the box finds nothing there for now.

**What I assumed**
bigMike's endpoint will accept `{question, excerpts:[{path,line,excerpt}]}` and return `{answer, sources?: string[]}`. This is the contract for the bigMike task.

**For you**
- Create the bigMike task for `/api/memory/ask`.
- Create the Health and Finance summary-export tasks.
- Redeploy the app, because the build is done but I did not restart anything.

**Check:** 56 tests passed, including a new one for the ask validation, and `npm run build` succeeded. To see it, open the Search panel, search for a word, and press "Ask the model".
