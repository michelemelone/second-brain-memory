# MIC-12: Cross-domain pages: Proteins and Nutrition, and the protein intake versus cost question

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Pegasus
- Parent: MIC-5
- Updated: 2026-11-17

## Request

Pages in second-brain/wiki that link health nutrition data and finance food spending, and answer how protein intake relates to cost.

## Last report of the agent

MIC-12 is done: I added two pages in `second-brain/wiki/` and pushed them to `main` (commit fad6362). I didn't run any tests or a link check, and it's all Markdown.

- **`proteins-and-nutrition.md`** is the hub. It says where each kind of data lives: nutrition and weight in the Health monthly summaries, food spending in the Finance summaries, and the meal log and protein target in the bigMike wiki.
- **`protein-intake-vs-cost.md`** answers the question. A real cost per gram of protein can't be worked out from the current summaries, so it gives a rough monthly method and lists why the result is only indicative:
  - Only 2026-10 and 2026-11 (partial) have nutrition logged.
  - The Food category mixes protein with everything else, including eating out.
  - CHF and EUR amounts aren't converted.
  - Meal logs are estimates.

Following `wiki/SCHEMA.md`, the pages link to the source summaries and copy no raw figures.

**For Michele:** a real answer needs either itemised supermarket receipts or a price per product for the recurring protein foods (whey, cottage cheese, chicken, cod), plus a CHF/EUR rate. The second page records this as an open question for you.

How to check: open `second-brain/wiki/protein-intake-vs-cost.md` and follow its links to the Health and Finance monthly files.
