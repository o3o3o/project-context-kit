---
name: task-bootstrap
description: Initialize the active task directory with all required template files.
---

# task-bootstrap Skill

## Purpose
Create a fresh `docs/task/active/` directory with all required state files.
Use this when starting a new task from scratch.

## Instructions

1. **Check if `docs/task/active/` already exists.**
   - If it exists and has content, ask the user: *"An active task already exists. Do you want to archive it and start a new one, or continue the existing task?"*
   - If the user wants to archive: run the `task-archive` skill first, then proceed.
   - If the user wants to continue: stop here and suggest running `task-resume` instead.

2. **Create the directory** `docs/task/active/`.

3. **Create the following files** by copying from `docs/task/_template/` if it exists, otherwise create from scratch:
   - `task.md` — ask the user for: Task name, objective, success criteria
   - `plan.md` — ask the user for or draft: key implementation steps
   - `progress.md` — initialize with: `## Session Log\n_No progress yet._`
   - `handoff.md` — initialize with: `## Status\nTask just started. See task.md for objective.`
   - `verification.md` — initialize with: `## Verification Log\n_No verification yet._`

4. **Confirm** to the user: *"Active task created at docs/task/active/. I've read the task and I'm ready to start work."*

## Constraints
- Do not overwrite `docs/task/active/` without explicit user confirmation.
- Always create all 5 files — never leave the directory partially initialized.
