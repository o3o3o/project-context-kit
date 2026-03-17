---
name: task-bootstrap
description: Initialize a new task directory based on the current Git branch.
---

# task-bootstrap Skill

## Purpose
Automate the creation of a task directory and its required files (`task.md`, `plan.md`, `progress.md`, `handoff.md`, `verification.md`) based on the current Git branch name.

## Instructions
1. Get the current branch name using `git branch --show-current`.
2. Extract the Ticket ID from the branch name (e.g., from `feat/T-123-login`, extract `T-123`).
3. If no Ticket ID is found, ask the user for one.
4. Check if `docs/task/<ticket-id>/` exists.
5. If it doesn't exist, create it and copy templates from `.ai-governance/docs/task/_template/` (if available) or create default empty files.
6. Initialize `task.md` with the ticket ID and a brief summary from the branch name.
7. Notify the user once the task directory is ready.

## Constraints
- Do not overwrite existing files with valid content.
- Always use the `docs/task/` root as specified in the repository contract.
