# Warehouse Schema Manifest

Generated: 2026-11-27T10:03:12.195Z
Database: `/home/beedme/data/workspace/second-brain/memory/warehouse/warehouse.sqlite`

This file is generated automatically from `warehouse.sqlite` after every sync.
Agents should query `warehouse.sqlite` directly (read-only) for any factual or cross-application data question.

## Tables

| Table | App | Rows | Last Sync | Meaning |
|---|---|---:|---|---|
| `camera_sessions` | camera | 79 | 2026-11-27T10:03:11.679Z | Camera session metadata with AI analysis, questions, and answers |
| `gantry_reference_index` | gantry | 5474 | 2026-11-27T10:03:12.129Z | Reference data index for Gantry requirements |
| `german_sessions` | german | 5 | 2026-11-27T10:03:11.648Z | Study sessions with duration, activity type, topic, and score |
| `german_vocabulary` | german | 96 | 2026-11-27T10:03:11.648Z | German vocabulary words with translations, examples, and learning status |
| `mail_messages` | mail | 10000 | 2026-11-27T10:03:11.903Z | Email messages with metadata (sender, recipients, date, subject, labels, preview) |
| `sync_log` | warehouse | 20 | 2026-11-27T10:03:12.195Z | Audit log of every warehouse sync run (app, timestamps, row counts, errors, status). |
| `warehouse_tables` | warehouse | 8 | 2026-11-27T10:03:12.195Z | Registry of warehouse tables with owning app and one-line meaning. |

## Column Definitions

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
