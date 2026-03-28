# Task Archive

`docs/task/archive/` stores completed task snapshots moved out of the active task area.

## Why This Exists
- `docs/task/active/` is only for the current in-progress task.
- Completed tasks should move here so `/ctx-load` stays fast and focused.
- Archive entries preserve rich history without bloating startup context.

## Archive Shape
- Recommended folder name: `YYYY-MM-DD-short-slug`
- Each archived task snapshot should usually contain:
  - `task.md`
  - `summary.md`
  - `verification.md`
  - `commits/` if milestone checkpoints exist
  - `assets/` if durable evidence exists
  - Any task-specific design notes that lived with the task

## Completion Rule
When the current task is complete, move its active snapshot into `archive/`, then recreate `active/` from the task templates.
