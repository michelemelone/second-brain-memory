# MIC-15: Second Brain app: fix Not found, show all file types, conversion inbox, modern UI

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Pegasus
- Parent: MIC-5
- Updated: 2026-11-17

## Request

Michele's report: Memory in the app says Not found; only Markdown files open; wants Obsidian-like viewing of any file, drag and drop of files/folders, an inbox that lists new files and lets him convert all or some to Markdown, a nicer modern UI, and bigMike reading/asking questions from this memory.

## Last report of the agent

Confirmed: seven tasks, with #1 first. I can't create them myself, because this run has no tool for creating Paperclip issues. The rules also say not to create other work in a run. I haven't changed any code.

**What I need from you:** create these seven issues in the Second Brain project, or have the intake agent "Michele" create them. Then assign #1 to me.

| # | Title | Acceptance criteria |
|---|---|---|
| 1 | Second Brain app: engines and sign-in inside the app | The app runs its own engine runners, starting with Claude and Codex, then OpenCode and Antigravity. Its credentials are kept in the app's own folder. The brain icon no longer shows "login required". You can sign in to an engine in the app. bigMike is not edited. |
| 2 | Second Brain app: serve `ask`, `wiki-agent` and `repo` locally | The app no longer calls bigMike for these three. |
| 3 | Second Brain app: serve `sync`, wiki generation and `schedules` locally | The app has no bigMike dependency left. |
| 4 | Second Brain app: viewer for any file type, plus drag and drop | All file types open, in an Obsidian-like view. You can drop files and folders into the app. |
| 5 | Second Brain app: conversion inbox | New files are listed. You can convert all of them, or only the ones you select, to Markdown. |
| 6 | Second Brain app: modern UI redesign | A cleaner look across the app. |
| 7 | bigMike reads and asks questions from the Second Brain | bigMike can read and query this memory. |

**Notes**
- Issue 1 ends with a restart of `second-brain.service`. I won't do that, so you will need to.
- Issues 1 to 3 copy and adapt bigMike's code into the app's server. I only read bigMike. I never copy its tokens.
- Issue 7 changes bigMike. Please confirm that is allowed, since you said you don't want bigMike's engines edited.

How to check: the seven issues appear in the Second Brain project in Paperclip, with #1 assigned to me.
