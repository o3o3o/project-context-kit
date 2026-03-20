---
name: task-branch
description: Fork the Project Context reasoning tree into an isolated exploration path (v3.2 advanced mode).
---

# task-branch Skill

## Purpose
Isolate an experimental context within the active task to avoid polluting the default active summary with failed reasoning or hypothesis tests.

## Instructions

1. **Ask for Workstream Name**: e.g., `experiment-db-v2`.
2. **Create Tree**: `.project-context/docs/task/active/workstreams/<name>/commits/`.
3. **Initialize Summary**:
   - Copy `docs/task/active/summary.md` to `workstreams/<name>/summary.md`.
   - Update `Workstream Intent`: "Exploring [specific hypothesis]".
   - Update `Current State`: "Forked from active summary at [time or commit ID]".
   - Update `Next Action`: "Validating first prototype".
4. **Confirm**: *"Switched focus to GCC workstream `<name>`. Commits will be isolated here until you run `task-merge`."*
