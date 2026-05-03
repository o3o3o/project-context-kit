---
name: context-load
description: Load and synthesize the current Project Context state (v3.2).
---

# context-load Skill

## Purpose
Reconstruct the project and task state by reading the Project Context tree when durable context recovery is explicitly needed, such as a handoff, resume, or state validation.

## Instructions

1. **Map-First Safety Check**:
   - If `.project-context/runtime/context-map.yaml` exists, read it first.
   - Treat `runtime/context-map.yaml` as a generated routing cache, not source of truth.
   - Use the map's routes and read policy to decide what else is needed.

2. **Fallback Fast Context**:
   - If the map is missing, stale, or has empty/placeholder current fields, read `.project-context/docs/task/active/index.md` first.
   - Then read `.project-context/docs/task/active/summary.md` if it exists.
   - Verify `.project-context/docs/project/metadata.yaml` exists; read it only when command/runtime detail is needed.
   - Read `.project-context/docs/project/context.md` only when durable project background is needed.

3. **Expand Only If Needed**:
   - Read `.project-context/docs/task/active/task.md` when task scope or success criteria are needed.
   - Read `.project-context/docs/task/active/verification.md` when validation state is needed.
   - Read relevant files in `.project-context/docs/decisions/` when the task depends on prior long-lived design choices.
   - Read `.project-context/docs/task/active/tasklist.md` only when claiming module work, inspecting active/blocked module detail, or doing global scheduling.

4. **Compatibility Fallback**:
   - If `index.md` or `summary.md` are missing, look for a legacy branch-based summary under `.project-context/docs/task/active/branches/main/summary.md`.
   - Treat any branch-based summary as compatibility input, not the preferred source of truth.

5. **Milestone Context**:
   - Read the 1-2 most recent commits in `.project-context/docs/task/active/commits/` only when milestone context is needed.

6. **Output Structured View**:
   ```text
   ## PROJECT CONTEXT v3.2 VIEW
   - **Env**: [Runtime from map or metadata, if needed]
   - **Commands**: [Run/Test cmds from map route or metadata, if needed]
   - **Decisions**: [Relevant long-lived design choices, if any]
   - **Goal**: [Objective from context-map current or task.md]
   - **State**: [Current state from context-map current, index.md, or summary.md]
   - **Modules**: [Module summary/current_focus from map, or tasklist only if needed]
   - **Next Action**: [From context-map current, index.md, or summary.md]
   ```

7. **Ask**: *"Shall I proceed with [Next Action] or do you have a different direction?"*
