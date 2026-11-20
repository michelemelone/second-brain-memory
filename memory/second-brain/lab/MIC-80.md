# MIC-80: Second Brain 2/3 (Import & Staging view): dedicated folder/file drag-and-drop staging area with per-file analysis and target folder selection

- Project: Second Brain
- Status: done
- Priority: high
- Agent: Pegasus
- Parent: MIC-15
- Updated: 2026-11-17

## Request

Michele asked to remove the basic inline "Upload to the top: drop files on a folder, or [Choose files]" from the Explorer sidebar (screenshot: /home/beedme/data/workspace/personal-assistant/data/uploads/61db1d08-b9bb-4bae-8390-ecf9bf65c77d/original.png
![Attached screenshot](/api/uploads/61db1d08-b9bb-4bae-8390-ecf9bf65c77d/file)) and replace it with a dedicated, modern Import & Staging section where he can drag & drop an entire folder or files from his computer/device, see an analysis/staging plan of what will happen to each file and where it will be imported, adjust if needed, and run the batch import.

Do in /home/beedme/data/workspace/second-brain-app:
1. Remove `<UploadPanel ... />` from inside the Explorer sidebar (`web/src/App.tsx` line 76) so the Explorer sidebar is a clean, uncluttered file tree.
2. Add a dedicated **Import & Staging** view in the left activity bar (`Upload` / `FolderUp` icon in `App.tsx`, opening a full-width Staging view in the main pane or a dedicated panel):
3. **Dropzone for Folders & Files**:
  - Supports dragging and dropping **entire folders** (recursively traversing directories via `DataTransferItem.webkitGetAsEntry()` to preserve relative folder paths like `my-notes/2026/scan.pdf`) as well as multiple files, plus two clear buttons: **Select Folder** (`webkitdirectory`) and **Select Files**.
4. **Smart Staging & Analysis Table (before uploading!)**:
  - When a folder or files are dropped/selected, do NOT upload immediately. Instead, analyze them and display a clean **Staging Plan Table** showing every file with:
    1. **File & relative path** (e.g. `project-docs/spec.pdf`, `notes/idea.md`, `scan.png`) and file size.
    2. **Detected kind** badge (`PDF Document`, `Word / EPUB`, `Image / Scan`, `Markdown`, `Data / Code`, `Ignored / System` for `.DS_Store`, `Thumbs.db`, `.git`, etc., which default to `Skip`).
    3. **Planned Action** dropdown per file (plus a bulk selector at the top):
      - `Convert to Markdown` (default for PDF, EPUB, DOCX, DOC, RTF)
      - `Import as-is` (default for `.md`, `.txt`, `.csv`, `.json`, images, code)
      - `Skip` (default for hidden/system files)
    4. **Target folder in Second Brain** (editable base target folder at the top, defaulting to the currently selected Explorer folder or `wiki/inbox`, with option `[x] Preserve subfolder structure`, plus per-row target path preview showing exactly what file will be created, e.g. `wiki/inbox/project-docs/spec.md`).
5. **Batch Execution & Progress**:
  - A primary **"Import N files"** button (and **"Clear staging"** button) that executes the staged actions one by one with a progress bar and per-row live status (`Waiting` -> `Converting / Uploading…` -> `Imported → <path>` or `Error`), then refreshes the file tree!
6. Add tests in `/home/beedme/data/workspace/second-brain-app/web/tests/` covering the staging analysis table, action selection (`Convert to Markdown`, `Import as-is`, `Skip`), target folder preview, and batch import execution.

Check: open Second Brain -> Import & Staging; drop a folder or select multiple files; verify the staging table lists each file with its proposed action and target folder, and clicking Import imports them cleanly.
Rules: English UI text only. Do NOT stop to ask questions. Run tests (`npm test`), build (`npm run build`), commit and push in `/home/beedme/data/workspace/second-brain-app`.

## Last report of the agent

I added the Import & Staging view and removed the inline upload panel from the Explorer sidebar. `npm test` passes (68 tests) and `npm run build` succeeds. The work is committed (a01c54e) and pushed. I did not try it in a browser, so drag-and-drop of a real folder is untested.

**What I did**
- **Explorer:** the sidebar now only has the file tree. Dropping files on a folder in the tree still uploads them, as before.
- **New view:** a folder-up icon in the left activity bar opens Import & Staging in the main pane.
- **Dropzone:**
  - Drop a whole folder (read recursively, keeping paths like `my-notes/2026/scan.pdf`) or several files.
  - **Select Folder** and **Select Files** buttons do the same.
  - Nothing is uploaded at this stage.
- **Staging table:** one row per file with the following columns.
  - **File:** relative path and size.
  - **Kind:** a badge reading PDF Document, Word / EPUB, Image / Scan, Markdown, Data / Code or Ignored / System.
  - **Action:** a per-row dropdown (Convert to Markdown, Import as-is, Skip). A bulk selector at the top sets all rows at once.
  - **Target:** the exact path the file will be created at, e.g. `wiki/inbox/project-docs/spec.md`.
- **Defaults:**
  - PDF, EPUB, DOCX, DOC and RTF default to Convert to Markdown.
  - Markdown, text, CSV, JSON, images and code default to Import as-is.
  - `.DS_Store`, `Thumbs.db`, `.git`, `node_modules` and similar default to Skip.
- **Target folder:** editable, defaulting to the selected Explorer folder or `wiki/inbox`, with a "Preserve subfolder structure" checkbox.
- **Import:**
  - The "Import N files" button runs one file at a time, with a progress bar and a status on each row: Waiting, Converting / Uploading…, then Imported → path, Skipped or Error.
  - The file tree refreshes at the end. "Clear staging" empties the list.
- **Tests:** `web/tests/staging.test.ts` covers kind detection and default actions, target previews, and a batch run with convert, as-is, skip, an error row and folder creation.

**What I assumed**
- The server needs the destination folder to exist, so the import creates missing folders, one level at a time, before each upload.
- File types the server rejects, such as unknown binaries or `.json` and `.csv`, show as Error on their row. I did not change the server.
- The server never overwrites: if a name is taken it appends a number, so the path shown in the Target column can differ slightly from the final one. The status column shows the real path.

How to check: open Second Brain, click the folder-up icon in the left bar, and drop a folder or use Select Folder. Confirm the table, change an action, and press Import.
