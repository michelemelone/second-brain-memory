# Warehouse Schema Manifest

Generated: 2026-11-27T10:15:34.870Z
Database: `/home/beedme/data/workspace/second-brain/memory/warehouse/warehouse.sqlite`

This file is generated automatically from `warehouse.sqlite` after every sync.
Agents should query `warehouse.sqlite` directly (read-only) for any factual or cross-application data question.

## Tables

| Table | App | Rows | Last Sync | Meaning |
|---|---|---:|---|---|
| `bigmike_activity` | bigmike | 4369 | 2026-11-27T10:09:29.544Z | Lab audit trail: who did what to which entity and when (a task status change is action=update, entity=issue, detail=status). |
| `bigmike_agent_revisions` | bigmike | 1 | 2026-11-27T10:09:29.544Z | History of edits to agent instructions. |
| `bigmike_agents` | bigmike | 24 | 2026-11-27T10:09:29.544Z | Lab agents (name, role, engine, model, instructions). |
| `bigmike_cron_jobs` | bigmike | 5 | 2026-11-27T10:09:29.544Z | Scheduled automations and reminders of bigMike (schedule, prompt, last run, status). |
| `bigmike_cron_runs` | bigmike | 0 | 2026-11-27T10:09:29.544Z | Every execution of a cron job. |
| `bigmike_decisions` | bigmike | 108 | 2026-11-27T10:09:29.544Z | Owner decisions on tasks in review (approved, replied, sent_back) with date. |
| `bigmike_drafts` | bigmike | 3 | 2026-11-27T10:09:29.544Z | Unsent composer drafts per chat. |
| `bigmike_goals` | bigmike | 32 | 2026-11-27T10:09:29.544Z | Company and project goals of the Lab. |
| `bigmike_issue_comments` | bigmike | 1450 | 2026-11-27T10:09:29.544Z | Every comment and agent report on a Lab task (author, body, created_at). |
| `bigmike_issue_status_events` | bigmike | 1334 | 2026-11-27T10:09:29.544Z | Status change events of Lab tasks (issue_id, key, actor, at ISO); the source records the field changed, not the new value. |
| `bigmike_issues` | bigmike | 506 | 2026-11-27T10:09:29.544Z | Every Lab task (key MIC-n, title, description, status, priority, project, assignee) plus done_at = when it became done. |
| `bigmike_lab_chat` | bigmike | 14 | 2026-11-27T10:09:29.544Z | Messages of the Lab agent chats. |
| `bigmike_messages` | bigmike | 6047 | 2026-11-27T10:09:29.544Z | Every chat message, full text, by role (user = the owner, assistant = bigMike), with ts (ISO) and thread_id. |
| `bigmike_projects` | bigmike | 16 | 2026-11-27T10:09:29.544Z | Lab projects (applications) with folder and status. |
| `bigmike_routine_runs` | bigmike | 0 | 2026-11-27T10:09:29.544Z | Every routine firing and its outcome. |
| `bigmike_routines` | bigmike | 5 | 2026-11-27T10:09:29.544Z | Lab routines (scheduled agent work). |
| `bigmike_runs` | bigmike | 793 | 2026-11-27T10:09:29.544Z | Every agent run (task, agent, status, start/finish, cost, tokens, summary, result). |
| `bigmike_threads` | bigmike | 352 | 2026-11-27T10:09:29.544Z | Every bigMike chat thread (title, scope/project, engine, model, created/updated/archived/deleted dates). |
| `camera_sessions` | camera | 79 | 2026-11-27T10:09:29.586Z | Camera session metadata with AI analysis, questions, and answers |
| `finance_fx_rates` | finance | 3354 | 2026-11-27T10:15:15.668Z | Daily exchange rates to CHF (ECB via frankfurter.dev) for multi-currency conversion. |
| `finance_imports` | finance | 1 | 2026-11-27T10:15:15.668Z | Metadata audit log of imported statement files, raw uploads, date bounds, and import counts. |
| `finance_merchants` | finance | 341 | 2026-11-27T10:15:15.668Z | Merchant classification rules mapping raw name patterns to canonical merchant and spending categories. |
| `finance_overrides` | finance | 27 | 2026-11-27T10:15:15.668Z | Manual per-transaction classification and note overrides that supersede imported classification. |
| `finance_spending_chf` | finance | 3319 | 2026-11-27T10:15:15.668Z | Convenience view with amounts converted to CHF at daily FX rate, original currency/amount preserved, overrides applied. |
| `finance_transactions` | finance | 3319 | 2026-11-27T10:15:15.668Z | Atomic ledger transactions across all accounts with classification, direction, and review status. |
| `finance_transactions_import_revolut` | finance | 2233 | 2026-11-27T10:15:15.668Z | Filtered view of transactions imported from Revolut statement files. |
| `gantry_reference_index` | gantry | 5474 | 2026-11-27T10:09:29.926Z | Reference data index for Gantry requirements |
| `german_sessions` | german | 5 | 2026-11-27T10:09:29.571Z | Study sessions with duration, activity type, topic, and score |
| `german_vocabulary` | german | 96 | 2026-11-27T10:09:29.571Z | German vocabulary words with translations, examples, and learning status |
| `health_analysis` | health | 33 | 2026-11-27T10:15:34.826Z | Daily analysis notes (markdown body) in data/analysis, one row per day. |
| `health_boosts` | health | 1 | 2026-11-27T10:15:34.826Z | Dose-boost schedule entries (start date, dose, interval). |
| `health_chat_messages` | health | 14 | 2026-11-27T10:15:34.826Z | Messages of the Health chat threads (thread, ts, role, text). |
| `health_config` | health | 253 | 2026-11-27T10:15:34.826Z | Flattened JSON settings: profile.json, jab_settings.json, personal_trainer_plan.json, integrations.json (credentials/tokens/e-mails dropped), tracker/garmin/today.json, analysis/energy_reserve_params.json. One row per leaf value (file, path, value). |
| `health_energy_history` | health | 1764 | 2026-11-27T10:15:34.826Z | Energy need per day (bmr_kcal + active_kcal = total_burn_kcal), with weight, intake_kcal and net_deficit_kcal where known. |
| `health_food_catalog` | health | 82 | 2026-11-27T10:15:34.826Z | Food catalog: per-100 g (or per-label) kcal, protein, carbs and fat of known products, with Nutri-Score and category. |
| `health_garmin_activities` | health | 510 | 2026-11-27T10:15:34.826Z | Garmin activities (type, duration, distance, heart rate, kcal, training effect). |
| `health_garmin_daily` | health | 1958 | 2026-11-27T10:15:34.826Z | Garmin daily indicators. |
| `health_garmin_exercise_sets` | health | 6616 | 2026-11-27T10:15:34.826Z | Every strength set recorded by Garmin (exercise, reps, weight, duration). |
| `health_garmin_raw_daily` | health | 6279 | 2026-11-27T10:15:34.826Z | Scalar values of the Garmin daily API dumps (tracker/garmin/raw/YYYY-MM/*_stats|sleep|readiness|training_status.json), one row per (date, kind) with the non-null scalar values as a JSON object in `data` (query with json_extract); long time series are not stored. |
| `health_garmin_training` | health | 1757 | 2026-11-27T10:15:34.826Z | Garmin readiness score and training status per day. |
| `health_jabs` | health | 9 | 2026-11-27T10:15:34.826Z | Every injection (date, time, dose_mg, site, side effects). |
| `health_meal_catalog_match` | health | 18 | 2026-11-27T10:15:34.826Z | View linking each meal to the food-catalog products whose name appears in the meal description (meal_row, product, catalog protein/kcal per 100 g). |
| `health_nutrition` | health | 239 | 2026-11-27T10:15:34.826Z | Every logged meal (date ISO, meal, description, kcal, protein_g, carbs_g, fat_g, notes). CAUTION: meal='daily_total' rows are the day's own total, not a meal: sum meals only (see view health_nutrition_daily). |
| `health_nutrition_daily` | health | 53 | 2026-11-27T10:15:34.826Z | View: per day sums of the real meals (daily_total rows excluded): kcal, protein_g, carbs_g, fat_g and number of meals. Use it for grams of protein per day. |
| `health_protein_vs_energy` | health | 53 | 2026-11-27T10:15:34.826Z | View: per day protein_g and kcal eaten next to the energy need (total_burn_kcal) and protein share of the need (kcal*4/need). |
| `health_side_effects` | health | 0 | 2026-11-27T10:15:34.826Z | Side effects log (symptom, severity, resolution). |
| `health_tracker_conflicts` | health | 0 | 2026-11-27T10:15:34.826Z | Indicator values that disagreed between devices. |
| `health_tracker_daily` | health | 2941 | 2026-11-27T10:15:34.826Z | Merged daily wearable indicators (steps, sleep hours, resting HR, distance, weight) with the source of each value. |
| `health_tracker_devices` | health | 4 | 2026-11-27T10:15:34.826Z | Wearable devices used (Garmin, Xiaomi) with first/last date. |
| `health_weight` | health | 131 | 2026-11-27T10:15:34.826Z | Body measurements (weight, waist, body fat, muscle, water, circumferences) with source and context; deleted flags removed entries. |
| `health_weight_outbox` | health | 115 | 2026-11-27T10:15:34.826Z | Weights queued for pushing to Garmin, with the time they were pushed. |
| `health_workouts` | health | 1 | 2026-11-27T10:15:34.826Z | Strength workouts logged by hand: session, exercise, sets, reps, load, RPE, duration. |
| `health_xiaomi_activities` | health | 17 | 2026-11-27T10:15:34.826Z | Xiaomi/Zepp activities. |
| `health_xiaomi_activity_segments` | health | 6161 | 2026-11-27T10:15:34.826Z | Xiaomi/Zepp activity segments (steps, distance, kcal per time span). |
| `health_xiaomi_body` | health | 75 | 2026-11-27T10:15:34.826Z | Xiaomi scale body measurements. |
| `health_xiaomi_daily` | health | 1327 | 2026-11-27T10:15:34.826Z | Xiaomi daily indicators (steps, sleep, heart rate). |
| `health_xiaomi_heartrate_manual` | health | 80 | 2026-11-27T10:15:34.826Z | Heart-rate readings taken manually on the Xiaomi band. |
| `mail_messages` | mail | 10000 | 2026-11-27T10:09:29.722Z | Email messages with metadata (sender, recipients, date, subject, labels, preview) |
| `sync_log` | warehouse | 51 | 2026-11-27T10:15:34.870Z | Audit log of every warehouse sync run (app, timestamps, row counts, errors, status). |
| `warehouse_tables` | warehouse | 61 | 2026-11-27T10:15:34.870Z | Registry of warehouse tables with owning app and one-line meaning. |

## Column Definitions

### `bigmike_activity`

Lab audit trail: who did what to which entity and when (a task status change is action=update, entity=issue, detail=status).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `agent_id` | TEXT | no | no |  |
| `instructions` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |

### `bigmike_agents`

Lab agents (name, role, engine, model, instructions).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `issue_id` | TEXT | no | no |  |
| `kind` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |

### `bigmike_drafts`

Unsent composer drafts per chat.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `key` | TEXT | no | yes |  |
| `text` | TEXT | no | no |  |
| `attachments` | TEXT | no | no |  |
| `updated_at` | TEXT | no | no |  |

### `bigmike_goals`

Company and project goals of the Lab.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `issue_id` | TEXT | no | no |  |
| `author` | TEXT | no | no |  |
| `body` | TEXT | no | no |  |
| `created_at` | TEXT | no | no |  |

### `bigmike_issue_status_events`

Status change events of Lab tasks (issue_id, key, actor, at ISO); the source records the field changed, not the new value.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
| `issue_id` | TEXT | no | no |  |
| `issue_key` | TEXT | no | no |  |
| `actor` | TEXT | no | no |  |
| `at` | TEXT | no | no |  |
| `field` | TEXT | no | no |  |

### `bigmike_issues`

Every Lab task (key MIC-n, title, description, status, priority, project, assignee) plus done_at = when it became done.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `timestamp` | TEXT | no | no |  |
| `resolved_by` | TEXT | no | no |  |
| `has_question` | INTEGER | no | no |  |
| `speech_text` | TEXT | no | no |  |
| `details` | TEXT | no | no |  |
| `image_file` | TEXT | no | no |  |

### `finance_fx_rates`

Daily exchange rates to CHF (ECB via frankfurter.dev) for multi-currency conversion.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
| `currency` | TEXT | yes | no |  |
| `date` | TEXT | yes | no |  |
| `rate_to_chf` | REAL | yes | no |  |

### `finance_imports`

Metadata audit log of imported statement files, raw uploads, date bounds, and import counts.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
| `filename` | TEXT | yes | no |  |
| `stored` | TEXT | yes | no |  |
| `size` | INTEGER | yes | no |  |
| `mime` | TEXT | yes | no |  |
| `uploaded_at` | TEXT | yes | no |  |
| `account` | TEXT | yes | no |  |
| `status` | TEXT | yes | no |  |
| `method` | TEXT | yes | no |  |
| `count` | INTEGER | yes | no |  |
| `skipped_duplicates` | INTEGER | yes | no |  |
| `review` | INTEGER | yes | no |  |
| `date_min` | TEXT | yes | no |  |
| `date_max` | TEXT | yes | no |  |

### `finance_merchants`

Merchant classification rules mapping raw name patterns to canonical merchant and spending categories.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `pattern` | TEXT | no | yes |  |
| `merchant` | TEXT | yes | no |  |
| `spending_type` | TEXT | yes | no |  |
| `spending_item_type` | TEXT | yes | no |  |
| `source_of_class` | TEXT | yes | no |  |

### `finance_overrides`

Manual per-transaction classification and note overrides that supersede imported classification.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `source_file` | TEXT | yes | no |  |
| `source` | TEXT | yes | no |  |
| `account` | TEXT | yes | no |  |
| `date` | TEXT | yes | no |  |
| `amount` | REAL | yes | no |  |
| `currency` | TEXT | yes | no |  |
| `merchant_raw` | TEXT | no | no |  |
| `merchant` | TEXT | no | no |  |
| `locality` | TEXT | no | no |  |
| `direction` | TEXT | yes | no |  |
| `spending_type` | TEXT | yes | no |  |
| `spending_item_type` | TEXT | yes | no |  |
| `note` | TEXT | no | no |  |
| `needs_review` | TEXT | yes | no |  |

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

### `gantry_reference_index`

Reference data index for Gantry requirements

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
| `table_name` | TEXT | no | no |  |
| `data` | TEXT | no | no |  |

### `german_sessions`

Study sessions with duration, activity type, topic, and score

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `session_id` | TEXT | no | yes |  |
| `date` | TEXT | yes | no |  |
| `duration_min` | TEXT | no | no |  |
| `activity` | TEXT | no | no |  |
| `topic` | TEXT | no | no |  |
| `score` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `german_vocabulary`

German vocabulary words with translations, examples, and learning status

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `german` | TEXT | no | yes |  |
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
| `file` | TEXT | no | yes |  |
| `date` | TEXT | no | no |  |
| `body` | TEXT | no | no |  |

### `health_boosts`

Dose-boost schedule entries (start date, dose, interval).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `thread_id` | TEXT | yes | no |  |
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
| `id` | TEXT | no | yes |  |
| `file` | TEXT | yes | no |  |
| `path` | TEXT | yes | no |  |
| `value` | TEXT | no | no |  |

### `health_energy_history`

Energy need per day (bmr_kcal + active_kcal = total_burn_kcal), with weight, intake_kcal and net_deficit_kcal where known.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `id` | TEXT | no | yes |  |
| `date` | TEXT | yes | no |  |
| `kind` | TEXT | yes | no |  |
| `data` | TEXT | yes | no |  |

### `health_garmin_training`

Garmin readiness score and training status per day.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
| `date` | TEXT | no | no |  |
| `readiness_score` | REAL | no | no |  |
| `readiness_level` | TEXT | no | no |  |
| `training_status` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `health_jabs`

Every injection (date, time, dose_mg, site, side effects).

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
| `indicator` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `values` | TEXT | no | no |  |

### `health_tracker_daily`

Merged daily wearable indicators (steps, sleep hours, resting HR, distance, weight) with the source of each value.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
| `date` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `weight_kg` | REAL | no | no |  |
| `pushed` | TEXT | no | no |  |

### `health_workouts`

Strength workouts logged by hand: session, exercise, sets, reps, load, RPE, duration.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
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
| `row_no` | INTEGER | no | yes |  |
| `date` | TEXT | no | no |  |
| `source` | TEXT | no | no |  |
| `time` | TEXT | no | no |  |
| `bpm` | TEXT | no | no |  |
| `notes` | TEXT | no | no |  |

### `mail_messages`

Email messages with metadata (sender, recipients, date, subject, labels, preview)

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `id` | TEXT | no | yes |  |
| `account` | TEXT | no | no |  |
| `message_id` | TEXT | no | no |  |
| `sender` | TEXT | no | no |  |
| `recipients` | TEXT | no | no |  |
| `cc` | TEXT | no | no |  |
| `bcc` | TEXT | no | no |  |
| `date` | TEXT | no | no |  |
| `subject` | TEXT | no | no |  |
| `labels` | TEXT | no | no |  |
| `body_preview` | TEXT | no | no |  |
| `is_draft` | INTEGER | no | no |  |
| `created_at` | TEXT | no | no |  |

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

### `warehouse_tables`

Registry of warehouse tables with owning app and one-line meaning.

| Column | Type | Not Null | PK | Default |
|---|---|---|---|---|
| `table_name` | TEXT | no | yes |  |
| `app` | TEXT | yes | no |  |
| `description` | TEXT | yes | no |  |
