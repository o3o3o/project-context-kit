---
name: task-branch
description: Fork the current active context into a new experimental branch.
---

# task-branch Skill

## Purpose
Create an isolated reasoning/exploration path within the active GCC task without polluting the `main` branch.

## Instructions

1. **Ask for Branch Name**: Request a simple, descriptive name (e.g., `feature-auth`, `refactor-db`, `explore-api`).
2. **Create Branch Directories**: Create `.ai-governance/docs/task/active/branches/<branch-name>/commits/`.
3. **Copy Main Summary**: Duplicate the `summary.md` from `main` to the new branch as a starting point.
4. **Update New Branch Summary**: Open `.ai-governance/docs/task/active/branches/<branch-name>/summary.md`. Add a note or prefix indicating this is an experimental branch and update the "Intent".
5. **Switch Context**: Tell the user you have moved focus to the new branch. All subsequent `task-commit` actions should explicitly point to this branch's `commits/` directory until `task-merge` is invoked.
6. **Confirm**: *"Switched to branch `<branch-name>`. You are now exploring an isolated context."*
