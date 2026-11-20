# MIC-10: Nightly generators: Health and Finance monthly summaries as Markdown (no AI)

- Project: Second Brain
- Status: done
- Priority: medium
- Agent: Sirius
- Parent: MIC-5
- Updated: 2026-11-17

## Request

A script per application writes readable monthly summaries into second-brain/health and second-brain/finance. No model call. Raw data stays in each application.

## Last report of the agent

**Report MIC-10**

**Done**
- I added `scripts/gen_finance_summary.py` and `scripts/gen_health_summary.py`. Both use only the Python standard library and make no model call.
- I ran them once.
  - Finance wrote 19 monthly files plus `index.md` in `memory/finance/`.
  - Health wrote 16 monthly files plus `index.md` in `memory/health/`.
- Both scripts rewrite every file each time, so they can be re-run safely.
- The commit is pushed to `main` (`cf346f0`).

**Finance summary, per month**
- Counts for transactions, items needing review and accounts.
- Totals by currency: money in, money out and net. Currencies are not converted.
- Spending by category.
- Top 8 merchants.

**Health summary, per month**
- Weight: first, last, change, min, max and average.
- Nutrition: average kcal and macros per logged day.
- Training days and sessions.
- Jab injections: date, dose and site.
- Side-effect counts.

The summaries contain only aggregates. No single transaction and no free-text notes are copied.

**Not done**
- **No nightly schedule yet.** The scripts only run when someone starts them. I did not create a timer or cron job, because that is a service change and the rules say nothing runs by itself. A job that runs both scripts at night is still to be set up.
- I did not read the database content of any app. I only read the CSV headers and the generated output.

**Assumptions**
- The sources are `personal-finance/data/transactions.csv` and `health/data/*.csv`. Both paths can be overridden with arguments.
- Weight rows marked `deleted` are skipped.

**For Michele**
- Should the nightly run be a systemd timer, or part of the existing nightly wiki job?
- Should Finance amounts also be converted to one currency using `fx_rates.json`?

**How to check:** run `python3 -I scripts/gen_health_summary.py && python3 -I scripts/gen_finance_summary.py` in `second-brain`, then open `memory/health/2026-10.md` and `memory/finance/2026-10.md`. The October Finance file should show 52 transactions: 36 in CHF and 16 in EUR.
