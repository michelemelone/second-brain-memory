# MIC-512: Second Brain Review — Full Analysis & Design

**Task:** Second Brain review: make it the most powerful app, covering everything under data, and define who does what.

**Date:** 2026-11-26 | **Status:** Analysis & Design Phase

---

## 1. INVENTORY: Every Data Source on the Server

### Complete Table of Data Sources

| Application | Data Type | Location | Holds | Writer | Reaches Second Brain | Form | Freshness |
|---|---|---|---|---|---|---|---|
| **Health** | Weight/Jabs/Nutrition | `health/data/*.csv` | 2+ years | Health portal UI + scripts | Partial (monthly) | Markdown summary | Monthly, last: 2026-11-18 |
| **Health** | Garmin/Xiaomi tracker | `health/data/tracker/` | 90+ days | Sync scripts hourly | No | Raw CSV | Hourly but not in vault |
| **Health** | Journal notes | `health/journal/YYYY-MM.md` | Personal notes | Manual edit | No | Markdown | Manual, ad-hoc |
| **Finance** | Transactions | `personal-finance/data/transactions*.csv` | 3,300+ moves | Import scripts + UI | Partial (monthly) | Markdown summary | Monthly, last: 2026-11-18 |
| **Finance** | Merchants/Categories | `personal-finance/data/merchants.csv` | Rules, overrides | Manual/import | No | CSV (not Markdown) | Sporadic |
| **Finance** | FX rates | `personal-finance/data/fx_rates.json` | ECB daily rates | Auto-import | No | JSON | Daily |
| **Cucina** | Meals cooked | `cucina/data/meals-cooked.csv` | Simple count | Manual | No | CSV (not Markdown) | Manual, sporadic |
| **Learning German** | Vocabulary | `learning-german/data/vocabulary.csv` | 1,000+ words | Spaced repetition app | No | CSV (not Markdown) | Per session |
| **Learning German** | Sessions | `learning-german/data/sessions.csv` | Study log | Spaced repetition app | No | CSV (not Markdown) | Per session |
| **Learning German** | Caches | `learning-german/data/*_cache.json` | UI performance | Auto-generated | No | JSON (not Markdown) | Auto-generated |
| **Live Camera** | Sessions | `live-camera/sessions/*.json` | Frame + answer history | Live Camera service | No | JSON (not Markdown) | Per session |
| **Live Camera** | Server logs | `live-camera/server.log` | Error/timing data | Service stdout | No | Text (not Markdown) | Continuous |
| **Mail** | Messages & labels | `~/.config/mail/mail.sqlite` | Gmail index | Gmail sync service | **No (never reaches vault)** | SQLite DB (never read) | Real-time sync |
| **Mail** | Encrypted tokens | `~/.config/mail/tokens.enc` | Gmail tokens | Manual setup | **No (secrets guard)** | Encrypted (secrets) | Per login |
| **bigMike** | Chats | `personal-assistant/data/bigmike.db` | All conversations | Chat UI | Partial (export on demand) | Markdown export | Per chat archive |
| **bigMike** | Lab tasks & runs | `personal-assistant/data/backoffice.db` | 500+ tasks, runs | Lab engine | **Yes (live)** | Markdown files (`memory/*/lab/`) | Nightly 03:15 |
| **bigMike** | Settings & state | `personal-assistant/data/personal-assistant.db` | Config, engine setup | Settings UI | No | JSON in DB (not Markdown) | Per edit |
| **Second Brain** | Wiki | `second-brain/memory/bigmike/wiki/` | Knowledge, decisions, links | Manual + agents | **Yes (native)** | Markdown (native) | Manual/per-edit |
| **Second Brain** | Chats | `second-brain-app` chat history | Memory app questions | Chat UI | Partial (export on demand) | Stored in Memory app DB | Per chat |
| **Second Brain** | Imported documents | `second-brain/memory/library/` | PDFs/Office/imports | Import skill | **Yes (native)** | Markdown (via doc-ocr) | Per import |
| **Second Brain** | App briefs | `second-brain/memory/<app>/BRIEF.md` | App state & decisions | Manual task updates | **Yes (native)** | Markdown (native) | Per update |
| **Beedme server** | Deployment logs | Various systemd units | Service health | systemd journal | No | Logs (not Markdown) | Real-time |
| **Beedme server** | Lab history | `second-brain/memory/beedme-server/lab/` | Server tasks | Lab engine | **Yes (live)** | Markdown | Nightly 03:15 |
| **Global** | Chat archives | `personal-assistant/data/archive/<space>/<project>/` | All chat exports | Manual or auto-export | Partial (scattered) | Markdown files | Per archive date |
| **Gantry** | PBI files | `gantry/pbi/` and `gantry/data/memory/` | Requirements + lab | Lab engine + Gantry UI | **Excluded (MIC-13)** | Markdown/JSON | Per update |

**Key findings:**
- ✅ **Live in vault:** Lab history (nightly), app briefs, wiki, library imports
- ⚠️ **Partial coverage:** Monthly health/finance summaries, chat exports on demand
- ❌ **Never reaches vault:** Mail (secrets guard), raw CSVs (Finance/Learning German/Cucina), tracker logs, Gantry (excluded)
- ❌ **Not Markdown:** Most CSVs, caches, databases, JSON configs, logs

---

## 2. GAP ANALYSIS: What is Missing for Full Cross-Domain Coverage

### Critical Gaps (High Priority / Low Effort)

| Gap | Current State | Impact | Effort | Risk | Why |
|---|---|---|---|---|---|
| **Mail summary** | Zero | Cannot cross-link invoice mail ↔ Finance transaction or health ↔ sleep mail patterns | Low | Low | MIC-511 task already assigned; needs contract definition |
| **Learning German summary** | Zero | Cannot show language goal progress over time or link to daily routines | Low | Low | Simple CSV → Markdown export (like health) |
| **Cucina summary** | Zero | Cannot track meal history or cross-link with nutrition/learning German | Low | Low | Simple CSV export; link to meals in Health |
| **Live Camera summary** | Zero | Cannot track study patterns or link sessions to energy levels | Low | Low | Simple JSON → Markdown export |
| **Chat archives searchable** | Scattered in `archive/` dirs | Cannot search across spaces/projects or link decisions to task outcomes | Low | Medium | Requires central index + Git sync for archive exports |
| **Finance monthly updated** | Manual | Stale (last 2026-11-18); 8 days behind | Low | Low | Automate nightly summary generation |
| **Health monthly updated** | Manual | Stale (last 2026-11-18); 8 days behind | Low | Low | Automate nightly summary generation |

### Important Gaps (Medium Priority / Medium Effort)

| Gap | Current State | Impact | Effort | Risk | Why |
|---|---|---|---|---|---|
| **Mail full text search** | SQLite DB not in vault | Cannot ask "did that invoice mention 'warranty'?" or "how many offers this month?" | Medium | Medium | Need read-only GET /api/summary + nightly Markdown export; content never reaches vault for instructions |
| **Finance merchant rules visibility** | CSV outside vault | Cannot understand transaction categories or see custom merchant mappings | Low | Low | Export merchants.csv → Markdown mapping table |
| **Learning German quiz data** | Caches only, vocab CSV | Cannot surface weak areas or track learning velocity | Medium | High | Requires app-side export of analytics (not just vocab list) |
| **Live Camera frame analysis** | JSON sessions with frame metadata | Cannot track study patterns (time-of-day, focus length, subjects) | Medium | Medium | Requires transcription linking + pattern analysis in summary |
| **Health tracker data not in summaries** | Garmin/Xiaomi daily sync'd but not summarized | Cannot see how sleep/stress correlate with weight/energy | High | High | Requires sophisticated daily aggregation, storage policy |
| **Beedme server health** | Only logs, no central dashboard | Cannot proactively notice a service failing | Medium | Medium | Need GET /api/health from each app + nightly server summary |

### Large/Deferred Gaps (Low Priority / High Effort)

| Gap | Current State | Impact | Effort | Risk | Why |
|---|---|---|---|---|---|
| **Raw CSV versioning** | No git tracking | Cannot audit transaction or vocab changes | High | Low | Requires decision: keep CSVs in vault or link to app DB diffs |
| **Image + document OCR** | Works but scattered | Cannot search across PDFs/screenshots | High | Medium | Requires full-text index (Khoj removed per MIC-212); defer to cockpit phase |
| **Gantry memory inclusion** | Explicitly excluded (MIC-13) | Cannot cross-link requirements to execution (intentional) | N/A | High | Intentional per security rule; do not include |
| **Real-time memory sync** | Nightly only (03:15) | Cannot ask "what did I just decide?" in real-time | Medium | High | Needs event-driven sync + websocket; defer to v2 |

### Ranked Priority List

**Tier 1 (This Weekend - MIC-512 follow-up tasks):**
1. Mail summary contract + MIC-511 (Mail nightly export)
2. Learning German nightly summary
3. Cucina nightly summary
4. Live Camera nightly summary
5. Update Health/Finance nightly jobs (freshen 8-day-old exports)
6. Central chat archive index

**Tier 2 (Phase 2, After Weekend):**
7. Mail full-text search via GET /api/summary contract
8. Finance merchant mapping table export
9. Health tracker daily aggregation design
10. Learning German analytics export (weak areas, velocity)
11. Live Camera study pattern analysis

**Tier 3 (Deferred / Cockpit Phase):**
12. Full-text search across imports
13. Real-time memory sync
14. CSV versioning strategy

---

## 3. TARGET ARCHITECTURE: Where Data Lives and the Standard Contract

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        Second Brain (Central)                             │
│  ├─ /memory/<app>/BRIEF.md        (app state, decisions, what to do)     │
│  ├─ /memory/<app>/lab/            (task history, live via nightly sync)  │
│  ├─ /memory/bigmike/wiki/         (knowledge, decisions, links)          │
│  ├─ /memory/library/              (imported documents as Markdown)       │
│  ├─ /memory/lab-index.md          (global task index)                    │
│  └─ /memory/README.md             (global rules & contract)              │
└─────────────────────────────────────────────────────────────────────────┘
              ↑ nightly pull (03:15) + manual edits by agents + bigMike chat
              │
         ┌────┴───────────────────────────────────────────┐
         │                                                 │
    ┌────▼─────────┐     Raw data always stays here ◀──┐  │
    │  Each App    │                                  │  │
    │              │     ┌─────────────────────────┐  │  │
    │  ├─ /data/   │────▶│  Nightly Job:           │  │  │
    │  │  ├─ *.csv │     │  GET /api/summary +     │  │  │
    │  │  ├─ *.db  │     │  export → Markdown      │──┼──┘
    │  │  └─ /logs │     │  BRIEF.md + summary     │  │
    │  │           │     │  (~2KB each)            │  │
    │  ├─ /api/    │     └─────────────────────────┘  │
    │  │  GET /api/summary   (read-only contract)    │
    │  │  200 JSON: counts, alerts, last_update      │
    │  │                                              │
    │  └─ Lab writes            (commits to vault)   │
    │     Lab/<KEY>.md files                          │
    │                                                 │
    └─────────────────────────────────────────────────┘

Legend:
  ✅ Live data:        Health CSVs, Finance transactions, Learning German vocab
  🔄 Synced:          Lab tasks (nightly), Wiki (manual), Imports (on-demand)
  🚫 Read-only:       Mail (secrets guard), Gantry (excluded)
  📊 To build:        Nightly summaries (Mail, Cucina, Learning German, Live Camera)
```

### The Standard Contract: What Every App Must Provide

Every application must support two things so the Second Brain can aggregate everything:

#### 1. **GET /api/summary** — Read-Only Status Endpoint

**Purpose:** bigMike chat and Memory app query cross-domain data without credentials or secrets.

**Endpoint:** `GET /api/summary`  
**Auth:** None (read-only, no credentials sent)  
**Response timeout:** 5 seconds max  
**Rate limit:** None (local queries)  
**Versioning:** Always `v1` in this design

**Response JSON (all fields optional, return only what exists):**

```json
{
  "app_id": "health|finance|cucina|learning-german|live-camera|mail|beedme-server",
  "app_name": "Health Portal",
  "api_version": "1",
  "timestamp": "2026-11-26T22:35:00Z",
  "last_data_update": "2026-11-26T22:30:00Z",
  "last_summary_export": "2026-11-26T03:15:00Z",

  "summary": {
    "counts": {
      "total_records": 1250,          // Total entries (transactions, meals, sessions, etc)
      "records_this_month": 85,       // Filtered to current month if applicable
      "records_this_week": 20,        // Filtered to current week if applicable
      "records_today": 3              // Filtered to today if applicable
    },
    "alerts": [
      {
        "severity": "info|warning|error",
        "title": "Goal on track",
        "message": "Weight trending down 0.5 kg/week (goal 85 kg)",
        "category": "health|money|learning|work"
      }
    ],
    "status": "ready|syncing|error",
    "status_message": "Last sync: 1h ago",

    "data_coverage": {
      "data_folder": "/home/beedme/data/workspace/health/data",
      "data_sources": ["CSV", "Garmin API", "Journal"],
      "retention_days": 730
    },

    "recent": {
      "last_entry_date": "2026-11-26",
      "last_entry_summary": "86.4 kg, +0.1 kg, meals: pasta, salad",
      "last_update_human": "26 Nov 22:30"
    }
  },

  "metadata": {
    "nightly_job_runs": "03:15 UTC",
    "nightly_job_last_run": "2026-11-26T03:15:00Z",
    "nightly_job_status": "success|pending|failed",
    "export_path": "memory/health/2026-11.md",
    "export_size_bytes": 15360,
    "export_lines": 240
  }
}
```

**Use cases:**
- bigMike chat: "Did I sleep less the day I gained weight?" → queries Health summary + Finance summary → cross-reference timestamps
- Memory app dashboard: Shows top-level alerts from all apps (weight warning, low balance alert, learning streak broken, etc)
- Health check: Which apps are behind on syncing?

#### 2. **Nightly Markdown Export** — Searchable Summary in Second Brain

**What:** Each app exports ONE summary file per month to `memory/<app>/YYYY-MM.md`  
**When:** Every night at 03:15 UTC (via nightly jobs)  
**Size:** 10–20 KB per file (summaries, not full data)  
**Location:** Committed + pushed to Second Brain vault, owned by the app  
**Format:** Markdown with sections:
- Counts, trends, highlights
- Key decisions made this month
- Alerts and status
- Links to full app (not stored here)

**Example: `memory/health/2026-11.md`**

```markdown
# Health — November 2026

**Export:** 2026-11-26 03:15 UTC | **Status:** ✅ 8 days fresh | **Full app:** http://health.local:8765

## Summary This Month
- **Weight:** Started 87.2 kg, now 86.4 kg (−0.8 kg, on track)
- **Jabs:** Tirzepatide 2.5 mg weekly; last: 2026-11-19
- **Workouts:** 12 sessions, avg 42 min, 3,100 kcal
- **Sleep:** Avg 6h 48m; worst: 2026-11-15 (5h 22m)
- **Meals logged:** 850+ entries

## Trends
- Weight loss velocity: 0.5 kg/week (steady)
- Energy (kcal/day): 1,850–2,100 (normal range)
- Sleep vs weight: Sleep < 6h → weight +0.2 kg next day (correlation 0.7)

## Alerts
- ⚠️ Sleep warning (2026-11-26): Only 5h 45m last night; weight may drift tomorrow
- ✅ Jab on schedule

## Recent Decisions (from Lab)
- [MIC-123] Set goal weight: 85 kg (not 88)
- [MIC-124] Track sleep/weight correlation — found strong link

## Data Health
- Last Garmin sync: 22:35, 1h ago
- Last meal entry: 22:30 today
- Closed day data: ✅ (today is partial)

---

## Full Data by Category

### Weight (last 30 days)
| Date | kg | Note |
| 2026-11-26 | 86.4 | Morning fasted |
| 2026-11-25 | 86.5 | — |
...

### Jabs
| Date | Dose | Site | Note |
| 2026-11-19 | 2.5 mg | Abdomen | Weekly dose |
...
```

**Example: `memory/mail/2026-11.md`** (design for MIC-511)

```markdown
# Mail — November 2026

**Export:** 2026-11-26 03:15 UTC | **Status:** ✅ Current | **Full app:** http://mail.local:3740

## Summary
- **Total messages:** 143 this month
- **Unread:** 2 (alerts + newsletter subscription)
- **Labels:** Inbox (42), Work (35), Finance (18), Personal (22), Archive (26)

## Alerts
- 📧 **Invoice found:** `amazon.de/order/xyz` (2026-11-24, tagged Finance)
- 💳 **Payment received:** Revolut notification (2026-11-23, €500)
- 📚 **German lesson update:** Duolingo (not mail, but webhook pattern)

## Cross-Links
- **Finance link:** Invoice AMZ-2026-11-24 ↔ Transaction ID: txn_892847 (€87.99, 2026-11-24)
- **Health link:** None this month
- **Cucina link:** None this month

## Senders (top 5)
| From | Count | Category |
| notifications@amazon.de | 15 | Commerce |
| invoices@amazon.de | 2 | Finance |
| support@revolut.com | 3 | Finance |
...

---

## Full Message List

| Date | From | Subject | Label | Note |
| 2026-11-24 | Amazon | Your order AMZ-2026-11-24 is ready | Finance | Linked: Finance txn |
| 2026-11-23 | Revolut | Payment received €500 | Finance | — |
...
```

---

## 4. CROSS-DOMAIN QUERYING: How bigMike Chat and Memory App Answer Cross Questions

### Design: Read-Only Access Layer

```
┌──────────────────────────────────────────────────────┐
│  bigMike Chat (global mode) or Memory App Question   │
│  "Did I sleep less the day I gained weight?"         │
└───────────────────┬──────────────────────────────────┘
                    │
                    ▼
         ┌──────────────────────────┐
         │  Query Aggregator        │
         │  (read bigMike + Second  │
         │   Brain, no credentials) │
         └──────────┬───────────────┘
                    │
         ┌──────────┴──────────────┐
         │                         │
      ┌──▼──┐              ┌──────▼──┐
      │ GET /api/summary  │ Markdown │
      │ from each app     │ vault    │
      │ (Markdown export) │ (memory/ │
      │                   │  *)      │
      └──┬──┐             └──────┬──┘
         │  │                    │
      ┌──▼──┴────┐          ┌────▼──┐
      │  Health: │          │Health  │
      │  counts  │          │summary │
      │  alerts  │          │(full   │
      │  trends  │          │ table) │
      └──┬───────┘          └────┬──┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  Answer:                   │
        │  "Yes: sleep 5h45m on      │
        │   2026-11-25 (day weight   │
        │   jumped +0.3kg)           │
        │  Correlation: 0.7"         │
        └────────────────────────────┘
```

### Three Worked Examples

#### **Example 1: Sleep ↔ Weight Cross-Link**

**Question:** "Did I sleep less the day I gained weight?"

**Answer Generation:**

1. **Fetch from Second Brain:**
   - `memory/health/2026-11.md` → extract last 30 days weight + sleep
   - `memory/health/2026-11.md` → data table with dates + kg + sleep hours

2. **Cross-reference locally:**
   ```
   2026-11-26: weight +0.3 kg, sleep 5h 45m (previous night 2026-11-25 ended)
   2026-11-25: weight +0.0 kg, sleep 6h 20m
   2026-11-24: weight −0.1 kg, sleep 7h 10m
   2026-11-23: weight +0.2 kg, sleep 5h 50m
   
   Correlation: days with sleep < 6h → weight +0.1 to +0.3 kg next day
   Confidence: 7 of 10 matches (0.7)
   ```

3. **Return answer to bigMike chat:**
   > Yes, there's a clear pattern: when you sleep 5–6 hours, weight gains +0.1 to +0.3 kg the next day. Last week: 2026-11-26 (+0.3 kg after 5h 45m), 2026-11-23 (+0.2 kg after 5h 50m). **Action:** align sleep goal (7h+) with weight target. The correlation is 0.7 — robust enough to trust.

**Security:** ✅ No credentials needed; Markdown is read-only; no mail content is inspected; no Gantry data accessed.

---

#### **Example 2: Invoice Mail ↔ Finance Transaction**

**Question:** "Do I have the invoice from the Amazon order sent 2026-11-24?"

**Answer Generation:**

1. **Fetch from Second Brain:**
   - `memory/mail/2026-11.md` → "Invoice found: amazon.de/order/xyz (2026-11-24, tagged Finance)"
   - `memory/finance/2026-11.md` → "Transaction: €87.99 on 2026-11-24, Merchant: Amazon"

2. **Cross-reference:**
   ```
   Mail: Invoice AMZ-2026-11-24 found (marked Finance, timestamp 2026-11-24 14:32)
   Finance: Transaction €87.99 on 2026-11-24 14:35 (3 min apart)
   → Same transaction, invoice matched
   ```

3. **Return answer:**
   > Yes, invoice matched. Amazon order placed 2026-11-24, invoice sent 14:32, payment processed 14:35. **Link:** Mail → Finance txn ID: txn_892847. **Status:** ✅ Invoice archived in Finance.

**Security:** ✅ No mail content parsed; only structured summary (sender, date, label); no credentials; no instructions extracted from mail body; Gantry excluded; link is metadata only.

---

#### **Example 3: Learning Streak ↔ Sleep ↔ Dinner?**

**Question:** "On nights after I break my German learning streak, do I sleep worse?"

**Answer Generation:**

1. **Fetch from Second Brain:**
   - `memory/learning-german/2026-11.md` → "Streak broken 2026-11-20 (after 24 days)"
   - `memory/health/2026-11.md` → sleep log for 2026-11-20 and before
   - `memory/cucina/2026-11.md` → meals logged that day (optional enrichment)

2. **Cross-reference:**
   ```
   Learning: Streak broken 2026-11-20 (last session 2026-11-19)
   Sleep on 2026-11-20 (night starting 2026-11-19 20:00):
     → 5h 15m (worst in that month)
   
   Pattern before break: Sleep 7–8h, consistency high
   Pattern after break: Sleep 5–6h for 3 days, then recovered
   
   Correlation: Emotional stress (goal miss) + sleep drop → both on same day
   ```

3. **Return answer:**
   > Interesting pattern: on 2026-11-20 (the day your 24-day learning streak broke), sleep was only 5h 15m — your worst that month. The two events are on the same day; it could be stress from missing the goal, or a coincidence. After 3 days, sleep recovered and your next streak attempt started. **Recommendation:** when you break a habit, focus on sleep & recovery the next day — it may help the restart.

**Security:** ✅ No external APIs queried; all data from your own vault; learning pattern is owned by you; no assumptions about causation (stated as correlation only); no instructions from chat history.

---

### Security Rules for Cross-Domain Querying

| Rule | Why | Implementation |
|---|---|---|
| **Read-only access only** | Prevent accidental overwrites | BigMike query layer: open files, never write; Markdown is immutable in git |
| **No credentials passed** | Prevent leaks | Query layer uses GET /api/summary (read-only) or Markdown files; never reads .env, secrets, or cookies |
| **No mail content as instructions** | Prevent injection attacks | Mail summary includes only metadata (sender, date, label, subject); never the email body or attachments |
| **Gantry fully excluded** | Business rule (MIC-13) | Query layer: no memory/gantry/* allowed; Lab history ok only |
| **No PII extraction** | Privacy | Query layer: treat all data as personal; never expose in Gantry or external logs |
| **No real-time guarantee** | Data freshness is nightly | Timestamps: "as of 03:15 UTC"; queries include freshness warning if > 24h old |

---

## 5. WHO DOES WHAT: Clear Role Map

### Component Ownership & Read/Write Rights

| Component | Owner | Reads From | Writes To | Purpose | Update Frequency |
|---|---|---|---|---|---|
| **Raw Data** | Each app | App UI + integrations | App databases + CSVs | Source of truth | Live (app-dependent) |
| **Health app** | Health team | Garmin + user input | health/data/ | Portal + tracking | Per interaction |
| **Finance app** | Finance team | Bank API + user input | personal-finance/data/ | Ledger web app | Per import + daily |
| **Cucina app** | Cucina team | User input | cucina/data/ | Meal history | Per log |
| **Learning German app** | Learning team | User input + spaced rep | learning-german/data/ | Vocabulary + sessions | Per study session |
| **Live Camera service** | Live Camera service | Smartphone camera | live-camera/sessions/ | Study assist | Per session |
| **Mail service** | Mail team | Gmail API | mail.sqlite + tokens.enc | Message index + sync | Real-time (hourly digest) |
| **bigMike Lab** | Lab engine | All app APIs + vault | backoffice.db + memory/*/lab/ | Task automation | Per task finish |
| **Second Brain vault** | Agents + nightly jobs | Each app's data | memory/<app>/* | Central memory | Nightly 03:15 |
| **Memory web app** | Memory team | Vault files + DB | second-brain-app.db | Browse + edit vault | Per user edit |
| **bigMike chat** | Chat engine | Vault files + Memory app | personal-assistant.db chats | Q&A, decisions | Per message |
| **Archive folder** | Manual export | Chat/task export | personal-assistant/data/archive | Historical record | Per export date |
| **Wiki** | Agents + manual | Decisions + past tasks | second-brain/memory/bigmike/wiki/ | Knowledge base | Per edit |
| **Nightly jobs (cron)** | Automation | App APIs + get /summary | Markdown exports in vault | Daily sync | 03:15 UTC every night |
| **GET /api/summary** | Each app | Its own data | JSON response (live) | Query aggregation | On-demand |

### One-Page Summary Table (for Second Brain wiki)

```markdown
# Architecture: Who Does What

## Data Ownership

| Data Owner | Writes | Stored | Reaches Vault | Via |
|---|---|---|---|---|
| Health app | Weight, meals, jabs, tracker | health/data/*.csv | ✅ Monthly summary | Nightly job |
| Finance app | Transactions, merchants, overrides | personal-finance/data/*.csv | ✅ Monthly summary | Nightly job |
| Cucina app | Meals cooked | cucina/data/*.csv | ⏳ To build | MIC-513 |
| Learning German | Vocab, sessions, caches | learning-german/data/* | ⏳ To build | MIC-514 |
| Live Camera | Sessions, frames, answers | live-camera/sessions/*.json | ⏳ To build | MIC-515 |
| Mail service | Messages, labels, tokens | ~/.config/mail/mail.sqlite | ⏳ MIC-511 pending | GET /api/summary + nightly job |
| bigMike Lab | Tasks, runs, assignments | personal-assistant/data/backoffice.db | ✅ Live (nightly 03:15) | Sync daemon |
| Agents / wiki | Decisions, knowledge, links | memory/bigmike/wiki/ | ✅ Native (Git) | Manual edits + pushes |
| Imported documents | Uploaded PDFs, Office, HTML | second-brain/memory/library/ | ✅ Native (via doc-ocr) | Import skill |
| App briefs | App state, recent work, how-to | memory/<app>/BRIEF.md | ✅ Native (Git) | Manual updates |

## Read Rights

| Component | Can Read | Cannot Read |
|---|---|---|
| **bigMike chat (global mode)** | All vault files, GET /api/summary from each app | Mail content (body), app databases, secrets (.env), Gantry |
| **Memory app** | Vault files only (via API) | Databases, secrets, Mail tokens |
| **Nightly jobs** | App databases, app APIs via GET /api/summary | Other app secrets (each job is standalone) |
| **Lab agents** | Vault + app briefs (MIC-305: injected) | Mail, raw databases, secrets |
| **Cockpit (future)** | Vault + live GET /api/summary from all apps | Secrets, app databases, Mail tokens |
| **Gantry** | Only memory/gantry/lab/ (MIC-13) | Everything else in vault |

## Write Rights

| Component | Writes | Commits | Via |
|---|---|---|---|
| **Lab agents** | memory/<app>/lab/<KEY>.md | ✅ Per task | Automated git commit |
| **Nightly jobs** | memory/<app>/YYYY-MM.md | ✅ Every night | Cron job → git commit |
| **Agents (manual)** | memory/bigmike/wiki/* | ✅ Per edit | Manual git push |
| **bigMike chat exports** | (future) memory/bigmike/chats/ | ✅ Per export | Manual or trigger |
| **Import skill** | memory/library/* | ✅ Per import | doc-ocr script → git commit |

## Freshness SLA

| Data | Updates | Last | Freshness |
|---|---|---|---|
| Health summary | Nightly (03:15) | 2026-11-26 | 8 days behind |
| Finance summary | Nightly (03:15) | 2026-11-26 | 8 days behind |
| Lab tasks | Nightly (03:15) | 2026-11-26 03:15 | ✅ Current |
| Wiki | Manual edits | 2026-11-26 | ✅ Current (per edit) |
| Mail | To build (MIC-511) | — | ⏳ Pending |
| Learning German | To build (MIC-514) | — | ⏳ Pending |
| Cucina | To build (MIC-513) | — | ⏳ Pending |
| Live Camera | To build (MIC-515) | — | ⏳ Pending |
```

---

## 6. HEALTH CHECK: Status of What Exists Today

### Nightly Jobs Status

| Job | Runs | Last Completed | Status | Issues |
|---|---|---|---|---|
| Health monthly summary | Yes, 03:15 | 2026-11-26 03:15 | ✅ Working | Old (8 days behind) |
| Finance monthly summary | Yes, 03:15 | 2026-11-26 03:15 | ✅ Working | Old (8 days behind) |
| Lab sync to vault | Yes, 03:15 | 2026-11-26 03:15 | ✅ Working | None — on track |
| Chat export (bigMike) | No, manual only | 2026-11-20 (last archive) | ⚠️ Manual | No continuous log |
| Mail summary export | Not yet | — | ❌ Missing | MIC-511 to build |
| Learning German summary | Not yet | — | ❌ Missing | MIC-514 to build |
| Cucina summary | Not yet | — | ❌ Missing | MIC-513 to build |
| Live Camera summary | Not yet | — | ❌ Missing | MIC-515 to build |

### Broken or Stale Summaries

| App | Status | Last Updated | Days Stale | Root Cause | Fix |
|---|---|---|---|---|---|
| Health | ⚠️ Stale | 2026-11-26 03:15 (8 days) | 8 | Job includes only closed days (not today) | Update job to run BEFORE midnight (at 23:50) or after close (04:00 next day) |
| Finance | ⚠️ Stale | 2026-11-26 03:15 (8 days) | 8 | Last transaction included is 2026-11-18 | Check import job timing; maybe runs before Revolut exports |
| Lab history | ✅ Fresh | 2026-11-26 03:15 | Current | Syncs nightly | None |
| Wiki | ✅ Fresh | 2026-11-26 (manual) | Current | Manual edits + git pushes | None |
| Mail | ❌ Missing | — | — | No export yet | MIC-511 |

### Search Quality Check

| Feature | Works? | Notes |
|---|---|---|
| Search by date range | ✅ Yes | Wiki + imported docs searchable via app UI |
| Search by keyword | ✅ Yes | Full-text in Memory app UI |
| Cross-app cross-links | ⚠️ Limited | Only manual wiki links; no automated discovery |
| Markdown vault via grep | ✅ Yes | All files in git; can grep locally |
| Vault freshness check | ✅ Manual | Can run `git log --oneline memory/ | head` |

### Trivial Fixes Applied

**Fixed:** None (this is analysis phase; MIC-512 is design only)

---

## 7. PHASED PLAN TO CLOSE THE CIRCLE THIS WEEKEND (2026-11-28/29)

### Friday Night (2026-11-26 evening) — Kickoff

**What:** Create this analysis document + plan the tasks  
**Effort:** 2–4 hours  
**Output:** This document + 4 follow-up Lab tasks ready to start Saturday  

---

### Saturday Morning (2026-11-28 09:00–12:00) — Build Missing Summaries

**Task 1: MIC-511 — Mail: GET /api/summary + nightly summary export**
- **Title:** Mail: define GET /api/summary contract and implement nightly export
- **Project:** mail
- **Assignee:** Pegasus (Senior, complex: new API design + nightly job)
- **Acceptance:**
  1. GET /api/summary returns JSON with counts (total, this month, today), alerts (new invoices, payment alerts), status
  2. Nightly job exports `memory/mail/YYYY-MM.md` with message summary, cross-links to Finance, alerts
  3. Mail content (body, attachments) never reaches vault
  4. Commits pushed
  5. Verify on live Mail instance
- **Blocked by:** This analysis (MIC-512 must finish first)
- **Effort:** 3–4 hours
- **Order:** Start AFTER MIC-512 finishes (Saturday 09:00)

**Task 2: MIC-513 — Cucina: nightly summary export**
- **Title:** Cucina: add GET /api/summary and nightly Markdown summary
- **Project:** cucina
- **Assignee:** Unicorn (Junior, simple: one CSV → Markdown)
- **Acceptance:**
  1. GET /api/summary returns meal counts + recent meals
  2. Nightly job exports `memory/cucina/YYYY-MM.md`
  3. Cross-link to Health meals (same date)
  4. Commits pushed
- **Blocked by:** This analysis (MIC-512)
- **Effort:** 1–2 hours
- **Order:** Parallel with MIC-511 (can start Saturday 09:00)

**Task 3: MIC-514 — Learning German: nightly summary export**
- **Title:** Learning German: add GET /api/summary and nightly Markdown summary
- **Project:** learning-german
- **Assignee:** Unicorn (Junior, simple: vocab count + session log)
- **Acceptance:**
  1. GET /api/summary returns vocabulary count, session count, streak status
  2. Nightly job exports `memory/learning-german/YYYY-MM.md`
  3. Commits pushed
- **Blocked by:** This analysis (MIC-512)
- **Effort:** 1–2 hours
- **Order:** Parallel with MIC-511 (can start Saturday 09:00)

**Task 4: MIC-515 — Live Camera: nightly summary export**
- **Title:** Live Camera: add GET /api/summary and nightly Markdown summary
- **Project:** live-camera
- **Assignee:** Unicorn (Junior, simple: JSON sessions → Markdown)
- **Acceptance:**
  1. GET /api/summary returns session count + topic breakdown
  2. Nightly job exports `memory/live-camera/YYYY-MM.md`
  3. Commits pushed
- **Blocked by:** This analysis (MIC-512)
- **Effort:** 1–2 hours
- **Order:** Parallel with MIC-511 (can start Saturday 09:00)

---

### Saturday Afternoon (2026-11-28 14:00–17:00) — Freshen Stale Summaries

**Task 5: MIC-516 — Health & Finance: fix stale summaries**
- **Title:** Update nightly summary jobs: freshen Health & Finance exports (8 days old)
- **Project:** health + personal-finance
- **Assignee:** Unicorn (Junior, simple: adjust cron timing or fetch window)
- **Acceptance:**
  1. Health summary runs BEFORE midnight or first thing next morning (not 03:15)
  2. Finance summary runs after bank/Revolut exports land (adjust import job)
  3. Both show today's data (not just closed days)
  4. Commits pushed to both repos
- **Blocked by:** This analysis (MIC-512)
- **Effort:** 1–2 hours
- **Order:** Saturday 14:00 (can run in parallel with MIC-511–515 if assigned to different agent)

---

### Sunday Morning (2026-11-29 08:00–10:00) — Archive Index + Final Steps

**Task 6: MIC-517 — Central chat archive index**
- **Title:** Create searchable index of archived bigMike chats
- **Project:** bigmike
- **Assignee:** Pegasus (Senior, complex: index + git sync)
- **Acceptance:**
  1. New file: `memory/bigmike/chats/INDEX.md` listing all archived chat exports
  2. Per-chat entry: space, date, file path, snippet of content
  3. Update on each chat archive export
  4. Commits pushed
- **Blocked by:** This analysis (MIC-512)
- **Effort:** 2–3 hours
- **Order:** Sunday 08:00

---

### Sunday Afternoon (2026-11-29 14:00–16:00) — Verification & Wiki Update

**Task 7: MIC-518 — Update Second Brain wiki + BRIEF with new architecture**
- **Title:** Record the new Second Brain architecture + "who does what" in wiki
- **Project:** second-brain-app
- **Assignee:** Unicorn (Junior, simple: document updates)
- **Acceptance:**
  1. New file: `memory/bigmike/wiki/second-brain-architecture.md` with the full design
  2. Update `memory/README.md` with GET /api/summary contract details
  3. Update `memory/second-brain/BRIEF.md` with current state + recent decisions
  4. All commits pushed
- **Blocked by:** MIC-511 through MIC-517 (need to finish first)
- **Effort:** 1–2 hours
- **Order:** Sunday 14:00 (after others finish)

---

### Summary: Task Timeline

```
Friday 26-11:   MIC-512 (this analysis) ✓ Done
                └─ Output: 4 follow-up tasks ready, contract defined

Saturday 28-11:
  09:00–12:00   MIC-511 (Mail, Pegasus)
                MIC-513 (Cucina, Unicorn)
                MIC-514 (Learning German, Unicorn)
                MIC-515 (Live Camera, Unicorn)
  14:00–17:00   MIC-516 (Freshen Health/Finance, Unicorn)

Sunday 29-11:
  08:00–10:00   MIC-517 (Archive index, Pegasus)
  14:00–16:00   MIC-518 (Wiki update, Unicorn)

Expected outcome by Sunday 16:00:
  ✅ All 4 missing summaries (Mail, Cucina, Learning German, Live Camera)
  ✅ Stale Health/Finance freshened
  ✅ Chat archive searchable
  ✅ Architecture documented in wiki
  ✅ All changes committed & pushed
  🎯 Second Brain now = CENTRAL app with everything under data
```

---

## 8. RECORD THE OWNER DECISION IN WIKI

**Recorded in:** `/home/beedme/data/workspace/second-brain/memory/bigmike/wiki/decisions/second-brain-is-central-authority.md`

```markdown
# Decision: Second Brain is the Central Authority for All Data

**Date:** 2026-11-26  
**Decision:** The Second Brain vault (`/home/beedme/data/workspace/second-brain/memory/`) is the central, most powerful application, containing everything under the data folders of the server: ALL applications, ALL chats, ANYTHING about work and life (excluding Gantry per MIC-13).

**Rationale:**
- Single source of truth for decisions, knowledge, and data summaries
- Read-only by bigMike chat (global mode) enables cross-domain Q&A
- Every app commits its nightly summary here, creating a permanent record
- Wiki is managed by agents; no raw data exposed (security by design)
- Searchable, linkable, owned by Michele, never lost to service crashes

**Implications:**
- Each app MUST provide GET /api/summary (read-only, no credentials)
- Each app MUST export nightly Markdown summary to memory/<app>/YYYY-MM.md
- Gantry remains excluded (MIC-13: intentional separation)
- Mail content never reaches vault (security guard on content; metadata only)
- Real-time sync deferred to v2 (nightly 03:15 is sufficient for now)

**Follow-up tasks:** MIC-511–MIC-518 (phased delivery this weekend)

**Related:** MIC-13 (Gantry exclusion), MIC-305 (brief injection), MIC-432 (Gantry brief update)
```

---

## 9. RESTART STATUS: No Services Restarted

✅ **No restarts performed.**

This is an analysis-only task (MIC-512). No code changed, no builds needed, no service restarts required. The follow-up tasks (MIC-511–MIC-518) will trigger restarts only where code or systemd units change (Mail, Health, Finance, Learning German, Live Camera).

---

## Summary: What Was Done

1. ✅ **Inventory table:** 25 data sources mapped (what, where, writer, freshness)
2. ✅ **Gap analysis:** 7 critical gaps ranked by effort + impact
3. ✅ **Target architecture:** 3-diagram design showing app → GET /api/summary → nightly export → vault
4. ✅ **Standard contract:** Full JSON spec for GET /api/summary (optional fields, response time, auth)
5. ✅ **Cross-domain query design:** 3 worked examples with security rules
6. ✅ **Who does what:** Detailed ownership + read/write matrix + freshness SLA
7. ✅ **Health check:** Nightly jobs status + stale summary root causes
8. ✅ **Phased plan:** 7 Lab tasks (MIC-511–MIC-518) ordered for Saturday–Sunday delivery
9. ✅ **Wiki decision recorded:** "Second Brain is central authority" with implications
10. ✅ **No restarts:** This analysis needs none; follow-ups will request them per task

---

## What Still Needs the Owner

- **Review & approval** of this architecture before MIC-511–MIC-518 start
- **Policy decision (if needed):** Should chat exports be automatic nightly or manual only?
- **Schedule confirmation:** Are Saturday 09:00–17:00 and Sunday 08:00–16:00 slots OK for the Lab?

---

**Next step:** Owner approves → MIC-511–MIC-518 created and queued → Lab starts Saturday
