---
name: task-merge
description: Consolidate exploration findings back into the main Project Context timeline (v3.2 advanced mode).
---

# task-merge Skill

## Purpose
Summarize the successful outcomes of an exploration workstream and integrate them back into the main active task timeline.

## Instructions

1. **Summarize Source Branch**:
   - Read `workstreams/<source>/summary.md` and the final commits.
2. **Create Merge Commit on Main**:
   - Run `task-commit` logic targeting `docs/task/active/commits/`.
   - **Intent**: Merge workstream `<source>`.
   - **Decisions**: Summarize WHY the findings of `<source>` were accepted and what was learned.
3. **Update Main Summary**:
   - Refresh `docs/task/active/summary.md` and `docs/task/active/index.md` to reflect the integrated result.
   - Update `Next Action`.
4. **Cleanup**: Ask the user if the `workstreams/<source>` directory should be deleted or kept as an archived reference.
