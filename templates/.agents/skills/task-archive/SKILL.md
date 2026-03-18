---
name: task-archive
description: Archive the current active GCC tree and clear for a new task.
---

# task-archive Skill

## Purpose
When a task is complete (or put on hold), move the entire GCC memory tree from `.ai-governance/docs/task/active/` to `.ai-governance/docs/task/archive/<name>/`.

## Instructions

1. **Read `.ai-governance/docs/task/active/task.md`** to get the task name.
2. **Ask the user to confirm** the archive name (suggest: `YYYY-MM-DD-<task-slug>`).
3. **Create the archive directory**: `.ai-governance/docs/task/archive/<archive-name>/`
4. **Move all files/directories** from `active/` to `archive/<archive-name>/`.
5. **Write a final archive commit**: In `archive/<archive-name>/branches/main/summary.md`, update the status to "Archived" and note the final outcome.
6. **Clear `.ai-governance/docs/task/active/`**.
7. **Confirm**: *"Task archived. Run `task-bootstrap` to start a new task."*
