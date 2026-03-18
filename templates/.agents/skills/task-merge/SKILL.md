---
name: task-merge
description: Merge an experimental branch back into the main GCC context.
---

# task-merge Skill

## Purpose
When an experimental branch succeeds or fails, merge its findings back into the `main` branch and summarize the outcome.

## Instructions

1. **Ask for Source Branch**: Request the name of the branch to merge (e.g., `feature-auth`).
2. **Read Branch Commits**: Summarize the final decisions and outcomes from the branch's `commits/` directory and `summary.md`.
3. **Write a Merge Commit on Main**:
   - Run the `task-commit` logic.
   - Point the commit to `.ai-governance/docs/task/active/branches/main/commits/<id>.md`.
   - In the "Changes Made" and "Decisions" sections, summarize the outcomes of the merged branch.
4. **Update Main Summary**: Update `.ai-governance/docs/task/active/branches/main/summary.md` with the new aggregated status and next steps.
5. **Close Branch**: Optionally rename the merged branch to `_merged_<branch-name>` or ask the user if they'd like to delete the branch directory entirely to clean the workspace.
6. **Confirm**: *"Branch `<branch-name>` merged into `main`. The `main` context is updated."*
