# Warehouse Schema Manifest

Generated: 2026-11-27T17:26:25.281Z
Location: `/home/beedme/data/workspace/second-brain/memory/warehouse`

## Database Files Map

| File | Tables | Why that group |
|---|---|---|
| `core.sqlite` | `sync_log`, `warehouse_apps`, `warehouse_coverage`, `warehouse_generic_tables`, `warehouse_jobs`, `warehouse_tables` | Central metadata, audit log, job scheduler, coverage check, and table registry. |
| `bigmike.sqlite` | `bigmike_activity`, `bigmike_agent_revisions`, `bigmike_agents`, `bigmike_cron_jobs`, `bigmike_cron_runs`, `bigmike_decisions`, `bigmike_drafts`, `bigmike_goals`, `bigmike_issue_comments`, `bigmike_issue_status_events`, `bigmike_issues`, `bigmike_lab_chat`, `bigmike_messages`, `bigmike_projects`, `bigmike_routine_runs`, `bigmike_routines`, `bigmike_runs`, `bigmike_threads` | BigMike assistant & Lab coordination (tasks, agents, runs, chats, issues). |
| `mail.sqlite` | `mail_accounts`, `mail_actions_log`, `mail_classifications`, `mail_drafts`, `mail_labels`, `mail_message_labels`, `mail_sync_log`, `mail_sync_state` | Mail personal communications: accounts, classifications, actions, drafts, labels and sync logs. |
| `mail_messages.sqlite` | `mail_messages` | Mail messages table (`mail_messages`, with snippet text), split from `mail.sqlite` to keep every file under 50 MiB. |
| `health.sqlite` | `health_analysis`, `health_boosts`, `health_chat_messages`, `health_config`, `health_energy_history`, `health_food_catalog`, `health_garmin_activities`, `health_garmin_daily`, `health_garmin_exercise_sets`, `health_garmin_raw_daily`, `health_garmin_training`, `health_jabs`, `health_meal_catalog_match`, `health_nutrition`, `health_nutrition_daily`, `health_protein_vs_energy`, `health_side_effects`, `health_tracker_conflicts`, `health_tracker_daily`, `health_tracker_devices`, `health_weight`, `health_weight_outbox`, `health_workouts`, `health_xiaomi_activities`, `health_xiaomi_activity_segments`, `health_xiaomi_body`, `health_xiaomi_daily`, `health_xiaomi_heartrate_manual` | Health & biometrics data (Garmin telemetry, nutrition, Xiaomi imports, body composition, medical logs). |
| `finance.sqlite` | `finance_fx_rates`, `finance_imports`, `finance_merchants`, `finance_overrides`, `finance_spending_chf`, `finance_transactions`, `finance_transactions_import_revolut` | Personal finance ledger, bank transactions, FX rates, merchant rules, and spending views. |
| `apps.sqlite` | `camera_sessions`, `cucina_meals`, `gantry_chat_messages`, `gantry_chats`, `gantry_requirements`, `german_sessions`, `german_vocabulary` | Application adapters (Gantry, Cucina, German learning, Live camera) and generic workspace folder tables. |

This file is generated automatically from the warehouse databases after every sync.
Agents should query the warehouse via `programs/bin/bigmike-data` (read-only) for any factual or cross-application data question; table names are plain (no schema prefix) and resolve to the file above.

## Storage policy

- **Where:** the seven files above live in git on GitHub, in `second-brain` under `memory/warehouse/`; one file per application group (with `mail_messages.sqlite` split from `mail.sqlite`), so no single file exceeds 50 MiB. Codeberg is used only if the GitHub per-file limit becomes a real problem (owner decision 2026-11-27, MIC-537/MIC-539).
- **Thresholds:** GitHub warns above 50 MiB per file and blocks above 100 MiB (push refused). A file above 25 MiB is flagged in the weekly check.
- **When a file gets close:** at 50 MiB split the heaviest table of that group into its own file (or drop what is rebuildable, then `VACUUM`); never commit a file near 100 MiB, because the push would fail and the warehouse would stop being saved.
- **Sync:** one weekly job, Friday 03:00 (`warehouse_jobs` row `0 3 * * 5`), covering every application; this manifest is rewritten at the end of each run.

## Tables

| Table | App | Rows | Last Sync | Meaning |
|---|---|---:|---|---|
| `bigmike_activity` | bigmike | 4559 | 2026-11-27T16:44:19.322Z | Lab audit trail: who did what to which entity and when (a task status change is action=update, entity=issue, detail=status). |
| `bigmike_agent_revisions` | bigmike | 1 | 2026-11-27T16:44:19.322Z | History of edits to agent instructions. |
| `bigmike_agents` | bigmike | 24 | 2026-11-27T16:44:19.322Z | Lab agents (name, role, engine, model, instructions). |
| `bigmike_cron_jobs` | bigmike | 5 | 2026-11-27T16:44:19.322Z | Scheduled automations and reminders of bigMike (schedule, prompt, last run, status). |
| `bigmike_cron_runs` | bigmike | 0 | 2026-11-27T16:44:19.322Z | Every execution of a cron job. |
| `bigmike_decisions` | bigmike | 108 | 2026-11-27T16:44:19.322Z | Owner decisions on tasks in review (approved, replied, sent_back) with date. |
| `bigmike_drafts` | bigmike | 3 | 2026-11-27T16:44:19.322Z | Unsent composer drafts per chat. |
| `bigmike_goals` | bigmike | 32 | 2026-11-27T16:44:19.322Z | Company and project goals of the Lab. |
| `bigmike_issue_comments` | bigmike | 1528 | 2026-11-27T16:44:19.322Z | Every comment and agent report on a Lab task (author, body, created_at). |
| `bigmike_issue_status_events` | bigmike | 1388 | 2026-11-27T16:44:19.322Z | Status change events of Lab tasks (issue_id, key, actor, at ISO); the source records the field changed, not the new value. |
| `bigmike_issues` | bigmike | 525 | 2026-11-27T16:44:19.322Z | Every Lab task (key MIC-n, title, description, status, priority, project, assignee) plus done_at = when it became done. |
| `bigmike_lab_chat` | bigmike | 20 | 2026-11-27T16:44:19.322Z | Messages of the Lab agent chats. |
| `bigmike_messages` | bigmike | 6115 | 2026-11-27T16:44:19.322Z | Every chat message, full text, by role (user = the owner, assistant = bigMike), with ts (ISO) and thread_id. |
| `bigmike_projects` | bigmike | 16 | 2026-11-27T16:44:19.322Z | Lab projects (applications) with folder and status. |
| `bigmike_routine_runs` | bigmike | 0 | 2026-11-27T16:44:19.322Z | Every routine firing and its outcome. |
| `bigmike_routines` | bigmike | 5 | 2026-11-27T16:44:19.322Z | Lab routines (scheduled agent work). |
| `bigmike_runs` | bigmike | 823 | 2026-11-27T16:44:19.322Z | Every agent run (task, agent, status, start/finish, cost, tokens, summary, result). |
| `bigmike_threads` | bigmike | 367 | 2026-11-27T16:44:19.322Z | Every bigMike chat thread (title, scope/project, engine, model, created/updated/archived/deleted dates). |
| `camera_sessions` | camera | 79 | 2026-11-27T16:44:19.792Z | Camera session metadata with AI analysis, questions, and answers |
| `cucina_meals` | cucina | 0 | 2026-11-27T16:44:19.533Z | Cooked meals log with recipes, servings, and ratings |
| `finance_fx_rates` | finance | 3354 | 2026-11-27T16:43:53.887Z | Daily exchange rates to CHF (ECB via frankfurter.dev) for multi-currency conversion. |
| `finance_imports` | finance | 1 | 2026-11-27T16:43:53.887Z | Metadata audit log of imported statement files, raw uploads, date bounds, and import counts. |
| `finance_merchants` | finance | 341 | 2026-11-27T16:43:53.887Z | Merchant classification rules mapping raw name patterns to canonical merchant and spending categories. |
| `finance_overrides` | finance | 27 | 2026-11-27T16:43:53.887Z | Manual per-transaction classification and note overrides that supersede imported classification. |
| `finance_spending_chf` | finance | 3319 | 2026-11-27T16:43:53.887Z | Convenience view with amounts converted to CHF at daily FX rate, original currency/amount preserved, overrides applied. |
| `finance_transactions` | finance | 3319 | 2026-11-27T16:43:53.887Z | Atomic ledger transactions across all accounts with classification, direction, and review status. |
| `finance_transactions_import_revolut` | finance | 2233 | 2026-11-27T16:43:53.887Z | Filtered view of transactions imported from Revolut statement files. |
| `gantry_chat_messages` | gantry | 416 | 2026-11-27T16:44:33.120Z | Every message of every Gantry chat, full text, with proposals, actions, cost and engine used. |
| `gantry_chats` | gantry | 105 | 2026-11-27T16:44:33.120Z | One row per Gantry ask-ai chat (active, archived and trash views): title, kind, engine, model, links to requirement and space. |
| `gantry_requirements` | gantry | 69 | 2026-11-27T16:44:33.120Z | Gantry backlog: one row per requirement, bug or task with state, assignee, dates, description, acceptance criteria and validation history. |
| `german_sessions` | german | 5 | 2026-11-27T16:44:19.598Z | Study sessions with duration, activity type, topic, and score |
| `german_vocabulary` | german | 96 | 2026-11-27T16:44:19.598Z | German vocabulary words with translations, examples, and learning status |
| `health_analysis` | health | 33 | 2026-11-27T16:44:18.444Z | Daily analysis notes (markdown body) in data/analysis, one row per day. |
| `health_boosts` | health | 1 | 2026-11-27T16:44:18.444Z | Dose-boost schedule entries (start date, dose, interval). |
| `health_chat_messages` | health | 14 | 2026-11-27T16:44:18.444Z | Messages of the Health chat threads (thread, ts, role, text). |
| `health_config` | health | 249 | 2026-11-27T16:44:18.444Z | Flattened JSON settings: profile.json, jab_settings.json, personal_trainer_plan.json, integrations.json (credentials/tokens/e-mails dropped), tracker/garmin/today.json, analysis/energy_reserve_params.json. One row per leaf value (file, path, value). |
| `health_energy_history` | health | 1764 | 2026-11-27T16:44:18.444Z | Energy need per day (bmr_kcal + active_kcal = total_burn_kcal), with weight, intake_kcal and net_deficit_kcal where known. |
| `health_food_catalog` | health | 82 | 2026-11-27T16:44:18.444Z | Food catalog: per-100 g (or per-label) kcal, protein, carbs and fat of known products, with Nutri-Score and category. |
| `health_garmin_activities` | health | 511 | 2026-11-27T16:44:18.444Z | Garmin activities (type, duration, distance, heart rate, kcal, training effect). |
| `health_garmin_daily` | health | 1958 | 2026-11-27T16:44:18.444Z | Garmin daily indicators. |
| `health_garmin_exercise_sets` | health | 6633 | 2026-11-27T16:44:18.444Z | Every strength set recorded by Garmin (exercise, reps, weight, duration). |
| `health_garmin_raw_daily` | health | 6280 | 2026-11-27T16:44:18.444Z | Scalar values of the Garmin daily API dumps (tracker/garmin/raw/YYYY-MM/*_stats|sleep|readiness|training_status.json), one row per (date, kind) with the non-null scalar values as a JSON object in `data` (query with json_extract); long time series are not stored. |
| `health_garmin_training` | health | 1757 | 2026-11-27T16:44:18.444Z | Garmin readiness score and training status per day. |
| `health_jabs` | health | 9 | 2026-11-27T16:44:18.444Z | Every injection (date, time, dose_mg, site, side effects). |
| `health_meal_catalog_match` | health | 18 | 2026-11-27T16:44:18.444Z | View linking each meal to the food-catalog products whose name appears in the meal description (meal_row, product, catalog protein/kcal per 100 g). |
| `health_nutrition` | health | 241 | 2026-11-27T16:44:18.444Z | Every logged meal (date ISO, meal, description, kcal, protein_g, carbs_g, fat_g, notes). CAUTION: meal='daily_total' rows are the day's own total, not a meal: sum meals only (see view health_nutrition_daily). |
| `health_nutrition_daily` | health | 54 | 2026-11-27T16:44:18.444Z | View: per day sums of the real meals (daily_total rows excluded): kcal, protein_g, carbs_g, fat_g and number of meals. Use it for grams of protein per day. |
| `health_protein_vs_energy` | health | 54 | 2026-11-27T16:44:18.444Z | View: per day protein_g and kcal eaten next to the energy need (total_burn_kcal) and protein share of the need (kcal*4/need). |
| `health_side_effects` | health | 0 | 2026-11-27T16:44:18.444Z | Side effects log (symptom, severity, resolution). |
| `health_tracker_conflicts` | health | 0 | 2026-11-27T16:44:18.444Z | Indicator values that disagreed between devices. |
| `health_tracker_daily` | health | 2941 | 2026-11-27T16:44:18.444Z | Merged daily wearable indicators (steps, sleep hours, resting HR, distance, weight) with the source of each value. |
| `health_tracker_devices` | health | 4 | 2026-11-27T16:44:18.444Z | Wearable devices used (Garmin, Xiaomi) with first/last date. |
| `health_weight` | health | 131 | 2026-11-27T16:44:18.444Z | Body measurements (weight, waist, body fat, muscle, water, circumferences) with source and context; deleted flags removed entries. |
| `health_weight_outbox` | health | 115 | 2026-11-27T16:44:18.444Z | Weights queued for pushing to Garmin, with the time they were pushed. |
| `health_workouts` | health | 1 | 2026-11-27T16:44:18.444Z | Strength workouts logged by hand: session, exercise, sets, reps, load, RPE, duration. |
| `health_xiaomi_activities` | health | 17 | 2026-11-27T16:44:18.444Z | Xiaomi/Zepp activities. |
| `health_xiaomi_activity_segments` | health | 6161 | 2026-11-27T16:44:18.444Z | Xiaomi/Zepp activity segments (steps, distance, kcal per time span). |
| `health_xiaomi_body` | health | 75 | 2026-11-27T16:44:18.444Z | Xiaomi scale body measurements. |
| `health_xiaomi_daily` | health | 1327 | 2026-11-27T16:44:18.444Z | Xiaomi daily indicators (steps, sleep, heart rate). |
| `health_xiaomi_heartrate_manual` | health | 80 | 2026-11-27T16:44:18.444Z | Heart-rate readings taken manually on the Xiaomi band. |
| `mail_accounts` | mail | 1 | 2026-11-27T17:26:25.061Z | Connected mailboxes (provider, address, status, access level); OAuth tokens are never copied. |
| `mail_actions_log` | mail | 5 | 2026-11-27T17:26:25.061Z | Log of actions proposed or applied on messages (action, detail JSON, actor, status, undo time). |
| `mail_classifications` | mail | 77761 | 2026-11-27T17:26:25.061Z | AI/rule classification of messages: category, confidence, source, reason and time. |
| `mail_drafts` | mail | 1 | 2026-11-27T17:26:25.061Z | Reply drafts prepared for messages (recipient, subject, body, tone, status). |
| `mail_labels` | mail | 29 | 2026-11-27T17:26:25.061Z | Labels of each mailbox (provider label id, name, system or user kind). |
| `mail_message_labels` | mail | 0 | 2026-11-27T17:26:25.061Z | Link table message to label (id = message_id:label_id); the source link table is empty, so see mail_messages.label_ids. |
| `mail_messages` | mail | 77761 | 2026-11-27T17:26:25.061Z | Every email message with real source columns (from_addr, from_email, to_addrs JSON, subject, snippet, received_at ISO, unread, label_ids JSON, size, thread_id, ai_checked); no bodies. |
| `mail_sync_log` | mail | 24 | 2026-11-27T17:26:25.061Z | History of the mail app's own Gmail sync runs (trigger, kind, fetched, removed, classified, status, detail). |
| `mail_sync_state` | mail | 1 | 2026-11-27T17:26:25.061Z | Per-mailbox sync progress (history id, full sync done, last sync time, status, error); page tokens are not copied. |
| `sync_log` | warehouse | 154 | 2026-11-27T17:26:25.281Z | Audit log of every warehouse sync run (app, timestamps, row counts, errors, status). |
| `warehouse_apps` | warehouse | 22 | 2026-11-27T17:26:25.281Z | Registry of every workspace folder: adapter, status (ok, no_structured_data, error, ignored), source paths, last sync, rows, last error and the scan proof. |
| `warehouse_coverage` | warehouse | 0 | 2026-11-27T17:26:25.281Z | Coverage check result of the last sync: workspace folders without a warehouse_apps entry or with status error (empty = full coverage). |
| `warehouse_generic_tables` | warehouse | 0 | 2026-11-27T17:26:25.281Z | Tables created by the generic adapter: folder, source file, kind and row count. |
| `warehouse_jobs` | warehouse | 1 | 2026-11-27T17:26:25.281Z | Scheduled warehouse sync jobs (default: weekly, Friday 03:00): app (empty = all), cron, enabled flag and last run result. |
| `warehouse_tables` | warehouse | 75 | 2026-11-27T17:26:25.281Z | Registry of warehouse tables with owning app and one-line meaning. |

## Column Definitions

### `bigmike_activity`

Lab audit trail: who did what to which entity and when (a task status change is action=update, entity=issue, detail=status).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `action` | TEXT | no | no |  |
| `entity` | TEXT | no | no |  |
| `entity_id` | TEXT | no | no |  |
| `detail` | TEXT | no | no |  |

### `bigmike_agent_revisions`

History of edits to agent instructions.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `agent_id` | TEXT | no | no |  |
| `instructions` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |

### `bigmike_agents`

Lab agents (name, role, engine, model, instructions).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `role` | TEXT | no | no |  |
| `reports_to` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `cwd` | TEXT | no | no |  |
| `instructions` | TEXT | no | no |  |
| `capabilities` | TEXT | no | no |  |
| `avatar` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `edited_at` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `skills` | TEXT | no | no |  |
| `budget_cents` | INTEGER | no | no |  |
| `fallbacks` | TEXT | no | no |  |

### `bigmike_cron_jobs`

Scheduled automations and reminders of bigMike (schedule, prompt, last run, status).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `schedule_type` | TEXT | no | no |  |
| `schedule_value` | TEXT | no | no |  |
| `timezone` | TEXT | no | no |  |
| `scope_key` | TEXT | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `prompt` | TEXT | no | no |  |
| `target_mode` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `notify_push` | INTEGER | no | no |  |
| `delete_after_run` | INTEGER | no | no |  |
| `enabled` | INTEGER | no | no |  |
| `next_run_at` | TEXT | no | no |  |
| `last_run_at` | TEXT | no | no |  |
| `last_status` | TEXT | no | no |  |
| `last_error` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `notify_mobile` | INTEGER | no | no |  |
| `notify_desktop` | INTEGER | no | no |  |
| `fallback_models` | TEXT | no | no |  |
| `file_mode` | TEXT | no | no |  |
| `archived_at` | TEXT | no | no |  |

### `bigmike_cron_runs`

Every execution of a cron job.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `job_id` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `started_at` | TEXT | no | no |  |
| `finished_at` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |
| `error` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `summary` | TEXT | no | no |  |

### `bigmike_decisions`

Owner decisions on tasks in review (approved, replied, sent_back) with date.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `issue_id` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |

### `bigmike_drafts`

Unsent composer drafts per chat.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `key` | TEXT | no | no |  |
| `text` | TEXT | no | no |  |
| `attachments` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |

### `bigmike_goals`

Company and project goals of the Lab.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `level` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `parent_id` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `edited_at` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `project_id` | TEXT | no | no |  |

### `bigmike_issue_comments`

Every comment and agent report on a Lab task (author, body, created_at).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `issue_id` | TEXT | no | no |  |
| `author` | TEXT | no | no |  |
| `body` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |

### `bigmike_issue_status_events`

Status change events of Lab tasks (issue_id, key, actor, at ISO); the source records the field changed, not the new value.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `issue_id` | TEXT | no | no |  |
| `issue_key` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |
| `field` | TEXT | no | no |  |

### `bigmike_issues`

Every Lab task (key MIC-n, title, description, status, priority, project, assignee) plus done_at = when it became done.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `key` | TEXT | no | no |  |
| `number` | INTEGER | no | no |  |
| `title` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `priority` | TEXT | no | no |  |
| `project_id` | TEXT | no | no |  |
| `assignee_id` | TEXT | no | no |  |
| `reviewer_id` | TEXT | no | no |  |
| `parent_id` | TEXT | no | no |  |
| `created_by` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `edited_at` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `blocked_by` | TEXT | no | no |  |
| `deleted_at` | TEXT | no | no |  |
| `done_at` | TEXT | no | no |  |

### `bigmike_lab_chat`

Messages of the Lab agent chats.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `role` | TEXT | no | no |  |
| `agent_id` | TEXT | no | no |  |
| `agent_name` | TEXT | no | no |  |
| `text` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |
| `session_id` | TEXT | no | no |  |

### `bigmike_messages`

Every chat message, full text, by role (user = the owner, assistant = bigMike), with ts (ISO) and thread_id.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `role` | TEXT | no | no |  |
| `text` | TEXT | no | no |  |
| `attachments` | TEXT | no | no |  |
| `ts` | TEXT | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |

### `bigmike_projects`

Lab projects (applications) with folder and status.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `goal_ids` | TEXT | no | no |  |
| `cwd` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `edited_at` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |

### `bigmike_routine_runs`

Every routine firing and its outcome.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `routine_id` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `outcome` | TEXT | no | no |  |
| `issue_id` | TEXT | no | no |  |
| `note` | TEXT | no | no |  |

### `bigmike_routines`

Lab routines (scheduled agent work).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `folder_id` | TEXT | no | no |  |
| `agent_id` | TEXT | no | no |  |
| `project_id` | TEXT | no | no |  |
| `prompt` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `triggers` | TEXT | no | no |  |
| `variables` | TEXT | no | no |  |
| `concurrency` | TEXT | no | no |  |
| `catchup` | TEXT | no | no |  |
| `notify` | INTEGER | no | no |  |
| `last_run_at` | TEXT | no | no |  |
| `checked_at` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `edited_at` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |

### `bigmike_runs`

Every agent run (task, agent, status, start/finish, cost, tokens, summary, result).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `issue_id` | TEXT | no | no |  |
| `agent_id` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `started_at` | TEXT | no | no |  |
| `finished_at` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |
| `summary` | TEXT | no | no |  |
| `error` | TEXT | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `steps` | TEXT | no | no |  |
| `last_activity_at` | TEXT | no | no |  |
| `result` | TEXT | no | no |  |
| `request_key` | TEXT | no | no |  |

### `bigmike_threads`

Every bigMike chat thread (title, scope/project, engine, model, created/updated/archived/deleted dates).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `scope_key` | TEXT | no | no |  |
| `session_id` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `external_id` | TEXT | no | no |  |
| `context_window` | INTEGER | no | no |  |
| `context_from` | TEXT | no | no |  |
| `context_summary` | TEXT | no | no |  |
| `archived_at` | TEXT | no | no |  |
| `deleted_at` | TEXT | no | no |  |
| `pin` | TEXT | no | no |  |
| `pin_order` | INTEGER | no | no |  |
| `read_files` | INTEGER | no | no |  |
| `file_mode` | TEXT | no | no |  |
| `session_file_mode` | TEXT | no | no |  |
| `muted` | INTEGER | no | no |  |
| `memories` | TEXT | no | no |  |
| `auto_resume` | INTEGER | no | no |  |
| `title_auto` | INTEGER | no | no |  |
| `held_until` | TEXT | no | no |  |

### `camera_sessions`

Camera session metadata with AI analysis, questions, and answers

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `timestamp` | TEXT | no | no |  |
| `resolved_by` | TEXT | no | no |  |
| `has_question` | INTEGER | no | no |  |
| `speech_text` | TEXT | no | no |  |
| `details` | TEXT | no | no |  |
| `image_file` | TEXT | no | no |  |

### `cucina_meals`

Cooked meals log with recipes, servings, and ratings

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `date` | TEXT | no | no |  |
| `meal` | TEXT | no | no |  |
| `recipe` | TEXT | no | no |  |
| `servings` | TEXT | no | no |  |
| `kcal_per_serving` | TEXT | no | no |  |
| `rating` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `finance_fx_rates`

Daily exchange rates to CHF (ECB via frankfurter.dev) for multi-currency conversion.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `currency` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `rate_to_chf` | REAL | no | no |  |

### `finance_imports`

Metadata audit log of imported statement files, raw uploads, date bounds, and import counts.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `filename` | TEXT | no | no |  |
| `stored` | TEXT | no | no |  |
| `size` | INTEGER | no | no |  |
| `mime` | TEXT | no | no |  |
| `uploaded_at` | TEXT | no | no |  |
| `account` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `method` | TEXT | no | no |  |
| `count` | INTEGER | no | no |  |
| `skipped_duplicates` | INTEGER | no | no |  |
| `review` | INTEGER | no | no |  |
| `date_min` | TEXT | no | no |  |
| `date_max` | TEXT | no | no |  |

### `finance_merchants`

Merchant classification rules mapping raw name patterns to canonical merchant and spending categories.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `pattern` | TEXT | no | no |  |
| `merchant` | TEXT | no | no |  |
| `spending_type` | TEXT | no | no |  |
| `spending_item_type` | TEXT | no | no |  |
| `source_of_class` | TEXT | no | no |  |

### `finance_overrides`

Manual per-transaction classification and note overrides that supersede imported classification.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `merchant` | TEXT | no | no |  |
| `spending_type` | TEXT | no | no |  |
| `spending_item_type` | TEXT | no | no |  |
| `note` | TEXT | no | no |  |
| `needs_review` | TEXT | no | no |  |

### `finance_spending_chf`

Convenience view with amounts converted to CHF at daily FX rate, original currency/amount preserved, overrides applied.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `source_file` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `account` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `orig_amount` | REAL | no | no |  |
| `orig_currency` | TEXT | no | no |  |
| `amount` | REAL | no | no |  |
| `currency` | TEXT | no | no |  |
| `fx_rate` | ANY | no | no |  |
| `amount_chf` | ANY | no | no |  |
| `merchant_raw` | TEXT | no | no |  |
| `merchant` | ANY | no | no |  |
| `locality` | TEXT | no | no |  |
| `direction` | TEXT | no | no |  |
| `spending_type` | ANY | no | no |  |
| `spending_item_type` | ANY | no | no |  |
| `note` | ANY | no | no |  |
| `needs_review` | ANY | no | no |  |

### `finance_transactions`

Atomic ledger transactions across all accounts with classification, direction, and review status.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `source_file` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `account` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `amount` | REAL | no | no |  |
| `currency` | TEXT | no | no |  |
| `merchant_raw` | TEXT | no | no |  |
| `merchant` | TEXT | no | no |  |
| `locality` | TEXT | no | no |  |
| `direction` | TEXT | no | no |  |
| `spending_type` | TEXT | no | no |  |
| `spending_item_type` | TEXT | no | no |  |
| `note` | TEXT | no | no |  |
| `needs_review` | TEXT | no | no |  |

### `finance_transactions_import_revolut`

Filtered view of transactions imported from Revolut statement files.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `source_file` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `account` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `amount` | REAL | no | no |  |
| `currency` | TEXT | no | no |  |
| `merchant_raw` | TEXT | no | no |  |
| `merchant` | TEXT | no | no |  |
| `locality` | TEXT | no | no |  |
| `direction` | TEXT | no | no |  |
| `spending_type` | TEXT | no | no |  |
| `spending_item_type` | TEXT | no | no |  |
| `note` | TEXT | no | no |  |
| `needs_review` | TEXT | no | no |  |

### `gantry_chat_messages`

Every message of every Gantry chat, full text, with proposals, actions, cost and engine used.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `chat_id` | TEXT | no | no |  |
| `id` | TEXT | no | no |  |
| `seq` | INTEGER | no | no |  |
| `role` | TEXT | no | no |  |
| `text` | TEXT | no | no |  |
| `ts` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `error` | TEXT | no | no |  |
| `proposal` | TEXT | no | no |  |
| `proposal_state` | TEXT | no | no |  |
| `proposal_created_id` | INTEGER | no | no |  |
| `actions` | TEXT | no | no |  |
| `action_state` | TEXT | no | no |  |
| `action_result` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `effort` | TEXT | no | no |  |
| `attachments` | TEXT | no | no |  |

### `gantry_chats`

One row per Gantry ask-ai chat (active, archived and trash views): title, kind, engine, model, links to requirement and space.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `view` | TEXT | no | no |  |
| `feature_id` | INTEGER | no | no |  |
| `requirement_id` | INTEGER | no | no |  |
| `space_id` | TEXT | no | no |  |
| `instance_id` | TEXT | no | no |  |
| `agent` | TEXT | no | no |  |
| `pin` | TEXT | no | no |  |
| `pin_order` | INTEGER | no | no |  |
| `archived_at` | TEXT | no | no |  |
| `deleted_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `group_key` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |
| `engine` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `effort` | TEXT | no | no |  |
| `live_edit` | INTEGER | no | no |  |
| `context_tokens` | INTEGER | no | no |  |
| `context_window` | INTEGER | no | no |  |
| `message_count` | INTEGER | no | no |  |

### `gantry_requirements`

Gantry backlog: one row per requirement, bug or task with state, assignee, dates, description, acceptance criteria and validation history.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | INTEGER | no | no |  |
| `type` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `state` | TEXT | no | no |  |
| `reason` | TEXT | no | no |  |
| `assigned_to` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `acceptance_criteria` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |
| `created_by` | TEXT | no | no |  |
| `feature_id` | INTEGER | no | no |  |
| `feature_name` | TEXT | no | no |  |
| `iteration_id` | INTEGER | no | no |  |
| `iteration_name` | TEXT | no | no |  |
| `iteration_start` | TEXT | no | no |  |
| `iteration_end` | TEXT | no | no |  |
| `area_path` | TEXT | no | no |  |
| `iteration_path` | TEXT | no | no |  |
| `priority` | INTEGER | no | no |  |
| `risk` | TEXT | no | no |  |
| `story_points` | REAL | no | no |  |
| `tags` | TEXT | no | no |  |
| `complexity` | TEXT | no | no |  |
| `depends_on` | TEXT | no | no |  |
| `related_to` | TEXT | no | no |  |
| `application_key` | TEXT | no | no |  |
| `application_name` | TEXT | no | no |  |
| `application_scope` | TEXT | no | no |  |
| `instance_id` | TEXT | no | no |  |
| `delivery_slug` | TEXT | no | no |  |
| `delivery_started_at` | TEXT | no | no |  |
| `delivered_at` | TEXT | no | no |  |
| `delivered_revision` | TEXT | no | no |  |
| `release_status` | TEXT | no | no |  |
| `run_count` | INTEGER | no | no |  |
| `run_failure` | TEXT | no | no |  |
| `cost_usd` | REAL | no | no |  |
| `validated_at` | TEXT | no | no |  |
| `validation_outcome` | TEXT | no | no |  |
| `validation_rounds` | INTEGER | no | no |  |
| `validation_log` | TEXT | no | no |  |
| `validated_content` | TEXT | no | no |  |
| `proposed_content` | TEXT | no | no |  |
| `attachments` | TEXT | no | no |  |
| `follow_ups` | TEXT | no | no |  |
| `raw` | TEXT | no | no |  |

### `german_sessions`

Study sessions with duration, activity type, topic, and score

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `session_id` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `duration_min` | TEXT | no | no |  |
| `activity` | TEXT | no | no |  |
| `topic` | TEXT | no | no |  |
| `score` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `german_vocabulary`

German vocabulary words with translations, examples, and learning status

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `german` | TEXT | no | no |  |
| `italian` | TEXT | no | no |  |
| `part_of_speech` | TEXT | no | no |  |
| `gender` | TEXT | no | no |  |
| `plural` | TEXT | no | no |  |
| `example` | TEXT | no | no |  |
| `date_added` | TEXT | no | no |  |
| `last_reviewed` | TEXT | no | no |  |
| `times_correct` | INTEGER | no | no |  |
| `times_wrong` | INTEGER | no | no |  |
| `status` | TEXT | no | no |  |

### `health_analysis`

Daily analysis notes (markdown body) in data/analysis, one row per day.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `file` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `body` | TEXT | no | no |  |

### `health_boosts`

Dose-boost schedule entries (start date, dose, interval).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `start_date` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `dose_mg` | REAL | no | no |  |
| `interval_days` | REAL | no | no |  |
| `end_date` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_chat_messages`

Messages of the Health chat threads (thread, ts, role, text).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `title` | TEXT | no | no |  |
| `n` | INTEGER | no | no |  |
| `ts` | TEXT | no | no |  |
| `role` | TEXT | no | no |  |
| `text` | TEXT | no | no |  |
| `rid` | TEXT | no | no |  |

### `health_config`

Flattened JSON settings: profile.json, jab_settings.json, personal_trainer_plan.json, integrations.json (credentials/tokens/e-mails dropped), tracker/garmin/today.json, analysis/energy_reserve_params.json. One row per leaf value (file, path, value).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `file` | TEXT | no | no |  |
| `path` | TEXT | no | no |  |
| `value` | TEXT | no | no |  |

### `health_energy_history`

Energy need per day (bmr_kcal + active_kcal = total_burn_kcal), with weight, intake_kcal and net_deficit_kcal where known.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `bmr_kcal` | REAL | no | no |  |
| `active_kcal` | REAL | no | no |  |
| `total_burn_kcal` | REAL | no | no |  |
| `intake_kcal` | REAL | no | no |  |
| `net_deficit_kcal` | REAL | no | no |  |

### `health_food_catalog`

Food catalog: per-100 g (or per-label) kcal, protein, carbs and fat of known products, with Nutri-Score and category.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `product` | TEXT | no | no |  |
| `category` | TEXT | no | no |  |
| `primary_macro` | TEXT | no | no |  |
| `nutri_score` | TEXT | no | no |  |
| `kcal` | REAL | no | no |  |
| `protein_g` | REAL | no | no |  |
| `carbs_g` | REAL | no | no |  |
| `fat_g` | REAL | no | no |  |
| `notes` | TEXT | no | no |  |
| `added` | TEXT | no | no |  |

### `health_garmin_activities`

Garmin activities (type, duration, distance, heart rate, kcal, training effect).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `activity_type` | TEXT | no | no |  |
| `duration_min` | REAL | no | no |  |
| `distance_km` | REAL | no | no |  |
| `avg_hr` | REAL | no | no |  |
| `max_hr` | REAL | no | no |  |
| `kcal` | REAL | no | no |  |
| `training_effect` | REAL | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_garmin_daily`

Garmin daily indicators.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `steps` | TEXT | no | no |  |
| `resting_hr` | TEXT | no | no |  |
| `sleep_hours` | TEXT | no | no |  |
| `sleep_score` | TEXT | no | no |  |
| `stress_avg` | TEXT | no | no |  |
| `body_battery_max` | TEXT | no | no |  |
| `active_kcal` | TEXT | no | no |  |
| `total_kcal` | TEXT | no | no |  |
| `vo2max` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_garmin_exercise_sets`

Every strength set recorded by Garmin (exercise, reps, weight, duration).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `activity_id` | TEXT | no | no |  |
| `set_no` | REAL | no | no |  |
| `exercise` | TEXT | no | no |  |
| `reps` | REAL | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `duration_s` | REAL | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_garmin_raw_daily`

Scalar values of the Garmin daily API dumps (tracker/garmin/raw/YYYY-MM/*_stats|sleep|readiness|training_status.json), one row per (date, kind) with the non-null scalar values as a JSON object in `data` (query with json_extract); long time series are not stored.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `data` | TEXT | no | no |  |

### `health_garmin_training`

Garmin readiness score and training status per day.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `readiness_score` | REAL | no | no |  |
| `readiness_level` | TEXT | no | no |  |
| `training_status` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_jabs`

Every injection (date, time, dose_mg, site, side effects).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `dose_mg` | REAL | no | no |  |
| `injection_site` | TEXT | no | no |  |
| `side_effects` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_meal_catalog_match`

View linking each meal to the food-catalog products whose name appears in the meal description (meal_row, product, catalog protein/kcal per 100 g).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `meal_row` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `meal` | TEXT | no | no |  |
| `product` | TEXT | no | no |  |
| `category` | TEXT | no | no |  |
| `catalog_kcal` | REAL | no | no |  |
| `catalog_protein_g` | REAL | no | no |  |
| `catalog_carbs_g` | REAL | no | no |  |
| `catalog_fat_g` | REAL | no | no |  |

### `health_nutrition`

Every logged meal (date ISO, meal, description, kcal, protein_g, carbs_g, fat_g, notes). CAUTION: meal='daily_total' rows are the day's own total, not a meal: sum meals only (see view health_nutrition_daily).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `meal` | TEXT | no | no |  |
| `description` | TEXT | no | no |  |
| `kcal` | REAL | no | no |  |
| `protein_g` | REAL | no | no |  |
| `carbs_g` | REAL | no | no |  |
| `fat_g` | REAL | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_nutrition_daily`

View: per day sums of the real meals (daily_total rows excluded): kcal, protein_g, carbs_g, fat_g and number of meals. Use it for grams of protein per day.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `date` | TEXT | no | no |  |
| `kcal` | ANY | no | no |  |
| `protein_g` | ANY | no | no |  |
| `carbs_g` | ANY | no | no |  |
| `fat_g` | ANY | no | no |  |
| `meals` | ANY | no | no |  |

### `health_protein_vs_energy`

View: per day protein_g and kcal eaten next to the energy need (total_burn_kcal) and protein share of the need (kcal*4/need).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `date` | TEXT | no | no |  |
| `protein_g` | ANY | no | no |  |
| `kcal_eaten` | ANY | no | no |  |
| `energy_need_kcal` | REAL | no | no |  |
| `protein_share_of_need` | ANY | no | no |  |

### `health_side_effects`

Side effects log (symptom, severity, resolution).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `symptom_type` | TEXT | no | no |  |
| `severity` | TEXT | no | no |  |
| `resolved_at` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_tracker_conflicts`

Indicator values that disagreed between devices.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `indicator` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `values` | TEXT | no | no |  |

### `health_tracker_daily`

Merged daily wearable indicators (steps, sleep hours, resting HR, distance, weight) with the source of each value.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `steps` | REAL | no | no |  |
| `steps_source` | TEXT | no | no |  |
| `sleep_hours` | REAL | no | no |  |
| `sleep_hours_source` | TEXT | no | no |  |
| `resting_hr` | REAL | no | no |  |
| `resting_hr_source` | TEXT | no | no |  |
| `hr_avg` | REAL | no | no |  |
| `hr_avg_source` | TEXT | no | no |  |
| `distance_km` | REAL | no | no |  |
| `distance_km_source` | TEXT | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `weight_kg_source` | TEXT | no | no |  |
| `body_fat_pct` | REAL | no | no |  |
| `body_fat_pct_source` | TEXT | no | no |  |

### `health_tracker_devices`

Wearable devices used (Garmin, Xiaomi) with first/last date.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `source` | TEXT | no | no |  |
| `brand` | TEXT | no | no |  |
| `type` | TEXT | no | no |  |
| `model` | TEXT | no | no |  |
| `first_date` | TEXT | no | no |  |
| `last_date` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_weight`

Body measurements (weight, waist, body fat, muscle, water, circumferences) with source and context; deleted flags removed entries.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `waist_cm` | REAL | no | no |  |
| `body_fat_pct` | REAL | no | no |  |
| `source` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `context` | TEXT | no | no |  |
| `muscle_kg` | REAL | no | no |  |
| `water_pct` | REAL | no | no |  |
| `deleted` | TEXT | no | no |  |
| `chest_cm` | REAL | no | no |  |
| `hips_cm` | REAL | no | no |  |
| `thigh_cm` | REAL | no | no |  |
| `arm_cm` | REAL | no | no |  |
| `neck_cm` | REAL | no | no |  |
| `glutes_cm` | REAL | no | no |  |

### `health_weight_outbox`

Weights queued for pushing to Garmin, with the time they were pushed.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `pushed` | TEXT | no | no |  |

### `health_workouts`

Strength workouts logged by hand: session, exercise, sets, reps, load, RPE, duration.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `session` | TEXT | no | no |  |
| `exercise` | TEXT | no | no |  |
| `sets` | REAL | no | no |  |
| `reps` | REAL | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `rpe` | REAL | no | no |  |
| `duration_min` | REAL | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_xiaomi_activities`

Xiaomi/Zepp activities.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `start_time` | TEXT | no | no |  |
| `activity_type` | TEXT | no | no |  |
| `duration_min` | TEXT | no | no |  |
| `distance_km` | TEXT | no | no |  |
| `kcal` | TEXT | no | no |  |
| `avg_pace_s_per_km` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_xiaomi_activity_segments`

Xiaomi/Zepp activity segments (steps, distance, kcal per time span).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `start` | TEXT | no | no |  |
| `stop` | TEXT | no | no |  |
| `distance_km` | TEXT | no | no |  |
| `kcal` | TEXT | no | no |  |
| `steps` | TEXT | no | no |  |

### `health_xiaomi_body`

Xiaomi scale body measurements.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `weight_kg` | TEXT | no | no |  |
| `bmi` | TEXT | no | no |  |
| `body_fat_pct` | TEXT | no | no |  |
| `water_pct` | TEXT | no | no |  |
| `muscle_kg` | TEXT | no | no |  |
| `bone_kg` | TEXT | no | no |  |
| `visceral_fat` | TEXT | no | no |  |
| `bmr_kcal` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_xiaomi_daily`

Xiaomi daily indicators (steps, sleep, heart rate).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `steps` | TEXT | no | no |  |
| `distance_km` | TEXT | no | no |  |
| `run_distance_km` | TEXT | no | no |  |
| `kcal` | TEXT | no | no |  |
| `sleep_hours` | TEXT | no | no |  |
| `deep_sleep_min` | TEXT | no | no |  |
| `light_sleep_min` | TEXT | no | no |  |
| `rem_min` | TEXT | no | no |  |
| `awake_min` | TEXT | no | no |  |
| `sleep_start` | TEXT | no | no |  |
| `sleep_end` | TEXT | no | no |  |
| `hr_avg` | TEXT | no | no |  |
| `hr_min` | TEXT | no | no |  |
| `hr_max` | TEXT | no | no |  |
| `hr_samples` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_xiaomi_heartrate_manual`

Heart-rate readings taken manually on the Xiaomi band.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | no |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `bpm` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `mail_accounts`

Connected mailboxes (provider, address, status, access level); OAuth tokens are never copied.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `provider` | TEXT | no | no |  |
| `email` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `access_level` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `compose` | INTEGER | no | no |  |

### `mail_actions_log`

Log of actions proposed or applied on messages (action, detail JSON, actor, status, undo time).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `account_id` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `action` | TEXT | no | no |  |
| `detail` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `undone_at` | TEXT | no | no |  |

### `mail_classifications`

AI/rule classification of messages: category, confidence, source, reason and time.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `category` | TEXT | no | no |  |
| `confidence` | REAL | no | no |  |
| `source` | TEXT | no | no |  |
| `reason` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |

### `mail_drafts`

Reply drafts prepared for messages (recipient, subject, body, tone, status).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `account_id` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `provider_draft_id` | TEXT | no | no |  |
| `provider_message_id` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `to_addr` | TEXT | no | no |  |
| `subject` | TEXT | no | no |  |
| `body` | TEXT | no | no |  |
| `tone` | TEXT | no | no |  |
| `status` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |

### `mail_labels`

Labels of each mailbox (provider label id, name, system or user kind).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `account_id` | TEXT | no | no |  |
| `provider_label_id` | TEXT | no | no |  |
| `name` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |

### `mail_message_labels`

Link table message to label (id = message_id:label_id); the source link table is empty, so see mail_messages.label_ids.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `label_id` | TEXT | no | no |  |

### `mail_messages`

Every email message with real source columns (from_addr, from_email, to_addrs JSON, subject, snippet, received_at ISO, unread, label_ids JSON, size, thread_id, ai_checked); no bodies.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | no |  |
| `account_id` | TEXT | no | no |  |
| `provider_message_id` | TEXT | no | no |  |
| `thread_id` | TEXT | no | no |  |
| `from_addr` | TEXT | no | no |  |
| `from_email` | TEXT | no | no |  |
| `to_addrs` | TEXT | no | no |  |
| `subject` | TEXT | no | no |  |
| `snippet` | TEXT | no | no |  |
| `received_at` | TEXT | no | no |  |
| `unread` | INTEGER | no | no |  |
| `label_ids` | TEXT | no | no |  |
| `size` | INTEGER | no | no |  |
| `list_unsubscribe` | TEXT | no | no |  |
| `ai_checked` | INTEGER | no | no |  |

### `mail_sync_log`

History of the mail app's own Gmail sync runs (trigger, kind, fetched, removed, classified, status, detail).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | INTEGER | no | no |  |
| `account_id` | TEXT | no | no |  |
| `trigger` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `started_at` | TEXT | no | no |  |
| `finished_at` | TEXT | no | no |  |
| `fetched` | INTEGER | no | no |  |
| `removed` | INTEGER | no | no |  |
| `classified` | INTEGER | no | no |  |
| `ai_used` | INTEGER | no | no |  |
| `status` | TEXT | no | no |  |
| `detail` | TEXT | no | no |  |

### `mail_sync_state`

Per-mailbox sync progress (history id, full sync done, last sync time, status, error); page tokens are not copied.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `account_id` | TEXT | no | no |  |
| `history_id` | TEXT | no | no |  |
| `full_done` | INTEGER | no | no |  |
| `last_sync_at` | TEXT | no | no |  |
| `last_status` | TEXT | no | no |  |
| `last_error` | TEXT | no | no |  |

### `sync_log`

Audit log of every warehouse sync run (app, timestamps, row counts, errors, status).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | INTEGER | no | yes |  |
| `app` | TEXT | yes | no |  |
| `started_at` | TEXT | yes | no |  |
| `finished_at` | TEXT | yes | no |  |
| `rows_read` | INTEGER | yes | no | 0 |
| `rows_written` | INTEGER | yes | no | 0 |
| `rows_removed` | INTEGER | yes | no | 0 |
| `errors` | TEXT | yes | no | '[]' |
| `status` | TEXT | yes | no |  |

### `warehouse_apps`

Registry of every workspace folder: adapter, status (ok, no_structured_data, error, ignored), source paths, last sync, rows, last error and the scan proof.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `folder` | TEXT | no | yes |  |
| `app` | TEXT | yes | no |  |
| `adapter` | TEXT | yes | no |  |
| `status` | TEXT | yes | no |  |
| `source_paths` | TEXT | yes | no | '[]' |
| `last_sync` | TEXT | no | no |  |
| `rows` | INTEGER | yes | no | 0 |
| `last_error` | TEXT | no | no |  |
| `proof` | TEXT | no | no |  |

### `warehouse_coverage`

Coverage check result of the last sync: workspace folders without a warehouse_apps entry or with status error (empty = full coverage).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `folder` | TEXT | yes | no |  |
| `issue` | TEXT | yes | no |  |
| `detail` | TEXT | no | no |  |
| `checked_at` | TEXT | yes | no |  |

### `warehouse_generic_tables`

Tables created by the generic adapter: folder, source file, kind and row count.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `table_name` | TEXT | no | yes |  |
| `folder` | TEXT | yes | no |  |
| `source_path` | TEXT | yes | no |  |
| `kind` | TEXT | yes | no |  |
| `rows` | INTEGER | yes | no | 0 |

### `warehouse_jobs`

Scheduled warehouse sync jobs (default: weekly, Friday 03:00): app (empty = all), cron, enabled flag and last run result.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | INTEGER | no | yes |  |
| `name` | TEXT | yes | no |  |
| `app` | TEXT | no | no |  |
| `cron` | TEXT | yes | no |  |
| `enabled` | INTEGER | yes | no | 1 |
| `created_at` | TEXT | yes | no |  |
| `last_run_at` | TEXT | no | no |  |
| `last_status` | TEXT | no | no |  |
| `last_message` | TEXT | no | no |  |

### `warehouse_tables`

Registry of warehouse tables with owning app and one-line meaning.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `table_name` | TEXT | no | yes |  |
| `app` | TEXT | yes | no |  |
| `description` | TEXT | yes | no |  |
