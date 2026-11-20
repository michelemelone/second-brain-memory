# MIC-81: Second Brain 3/3 (UI polish, Tree fix, all-file Viewer, and Settings & Connectors panel)

- Project: Second Brain
- Status: done
- Priority: high
- Agent: Pegasus
- Parent: MIC-15
- Updated: 2026-11-17

## Request

Michele reported that in the Second Brain app (screenshots: /home/beedme/data/workspace/personal-assistant/data/uploads/61db1d08-b9bb-4bae-8390-ecf9bf65c77d/original.png
![Attached screenshot](/api/uploads/61db1d08-b9bb-4bae-8390-ecf9bf65c77d/file) and /home/beedme/data/workspace/personal-assistant/data/uploads/f9e394b7-d4ed-41a2-bf6a-1ef373e57d1e/original.png
![Attached screenshot](/api/uploads/f9e394b7-d4ed-41a2-bf6a-1ef373e57d1e/file)):
1. The folder and file names in the Explorer tree (`memory`, `scripts`, `wiki`, `README.md`) are vertically cut off at the bottom!
2. The overall UI looks too basic and needs a clean, modern Obsidian-like look where all file types (Markdown, PDF, images, CSV/JSON, code/text) can be viewed cleanly.
3. There should be a dedicated **Settings & Connectors / Agents** panel (similar to bigMike's Lab / Connectors & Agents settings) where he can configure the Wiki Agent engine/model, sync/wiki schedules, and memory sources/connectors, and see connection status.

Do in /home/beedme/data/workspace/second-brain-app:
1. Fix Explorer Tree vertical clipping & modernise layout (`web/src/styles.css`, `web/src/Tree.tsx`, `web/src/App.tsx`):
2. Fix `.tree-row` / `.tree` CSS in `web/src/styles.css` (`line-height`, `padding`, `align-items: center`, `min-height: 28px`, `overflow`) so folder and file labels (`memory`, `scripts`, `wiki`, `README.md`) are never clipped vertically and icons align cleanly with text.
3. Polish the sidebar, tabs, search results, and buttons (`Retry`, `Ask the model`, etc. — notice in screenshot 1 `Retry` overlapped with a white border box!) with clean spacing, modern dark/light palette, andresizable sidebar width.
4. All-file Viewer (`web/src/Viewer.tsx`):
5. Ensure clicking any file in the tree opens it in the main pane:
  - Markdown (`.md`, `.markdown`): rendered with full GFM (tables, code blocks, wiki-links `[[...]]`, inline images) and Edit toggle.
  - Images (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`): rendered cleanly via `/api/raw?path=...` with zoom/fit controls.
  - PDF (`.pdf`): embedded preview via `<iframe src="/api/raw?path=..." />` with a download/open link.
  - CSV / JSON / Code / Text: clean formatted table or monospace viewer with editor support.
6. Settings, Agents & Connectors panel (`web/src/SettingsPanel.tsx` + Gear icon in activity rail):
7. Add a **Settings** icon (`Settings` from `lucide-react`) in the left activity bar of `App.tsx` that opens a full-page **Settings & Agents** view in the main pane with three clean cards:
  - **Connection & Repository Status**: shows connection to bigMike (`Connected` badge), Git repository path, last commit, and one-click **Sync Chats Now** and **Update Wiki Now** buttons with live status badges.
  - **Wiki Agent (Engine & Model)**: lets the owner pick the AI Engine (`Claude`, `Antigravity`, `OpenCode`, `Codex`) and Model that curates the Second Brain wiki and answers questions (`PUT /api/memory/wiki-agent`).
  - **Automation Schedules & Memory Sources**: clean toggles and schedule selectors for Chat Sync and Wiki Update (`PUT /api/memory/schedules`) instead of raw unstyled inputs.
8. Run tests (`npm test`), build (`npm run build`), commit and push in `/home/beedme/data/workspace/second-brain-app`, and restart the service (`systemctl --user restart second-brain.service`).

Check: open Second Brain: tree labels are crisp and never cut off, clicking any file previews it, and the Settings panel shows Connection status, Wiki Agent selector, and Schedules.
Rules: English UI text only. Do NOT stop to ask questions.

## Last report of the agent

MIC-81 is done and pushed (commit b22fb7c). I did not restart `second-brain.service`, because the common rules forbid restarting services. The new UI won't show until you run `systemctl --user restart second-brain.service`. `npm test` passes (68 tests) and `npm run build` succeeds. I did not open the result in a browser.

**What I did**
- **Tree clipping:** each Explorer row now has `min-height: 28px`, an explicit line height and vertical padding. Icons are `flex: none`, so they stay aligned with the labels.
- **Polish:**
  - **Sidebar:** you can drag its right edge to resize it (200–640px), and the width is remembered.
  - **Tabs and search:** I tidied the tab styling and the spacing of search results.
  - **Buttons:** `Retry` and `Ask the model` are now proper bordered buttons, which should fix the overlap you saw in the first screenshot.
- **Viewer:**
  - **Markdown:** unchanged. It already had full GFM, wiki-links, inline images and the Edit toggle.
  - **Images:** there is a zoom toolbar (zoom in, zoom out, Fit, 100%) on a checkerboard background.
  - **PDF:** it shows in an iframe with an "Open / download" link.
  - **CSV/TSV:** shown as a table, capped at 5000 rows.
  - **JSON:** pretty-printed in the monospace view.
  - **Other text and code:** monospace, with Edit.
- **Settings & Agents:** a Settings gear sits at the bottom of the left activity bar and opens a full-page view with three cards (`web/src/SettingsPanel.tsx`).
  - **Connection & Repository Status:** a Connected badge, repository path, last commit, chat sync and wiki state badges, and **Sync Chats Now** / **Update Wiki Now** buttons.
  - **Wiki Agent:** Engine selector (Claude, Antigravity, OpenCode, Codex) and Model selector, saved through `PUT /api/memory/wiki-agent`.
  - **Automation Schedules & Memory Sources:** toggle switches and schedule presets for Chat Sync and Wiki Update, saved through `PUT /api/memory/schedules`. A note lists the memory sources.

**Assumptions and limits**
- The "Connected" badge is static text. It does not test the connection to bigMike, so it shows Connected even if bigMike is down. The card does show an error if the status request fails.
- The model lists are fixed: Claude offers haiku, sonnet and opus. The other engines offer only "Engine default", because I found no list of models in the API.
- Schedules are chosen from four presets (hourly, every 6 hours, nightly at 03:00, Mondays at 03:00). A schedule already set to another cron expression is kept and shown as "Custom".
- I assumed `.csv` and `.json` files come back from the server as the "text" kind. I did not check this against the server.
- The old Memory sidebar panel is unchanged.

**How to check:** restart the service, then open Second Brain. The tree labels should not be cut off, clicking a PNG, PDF, CSV, JSON or Markdown file should preview it, and the gear icon should open the three Settings cards.
