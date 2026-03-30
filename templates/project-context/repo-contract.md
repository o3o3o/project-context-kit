# Repository Collaboration Contract (v3.2 - Project Context Model)

This contract defines how multiple AI agents (Codex, Antigravity, Claude, geminicli) collaborate using a **Project Context** memory layer.

> [!IMPORTANT]
> **Hermetic Rule**: All project-context records must be self-contained within `.project-context/`. Never link to ephemeral artifacts outside this directory.

> [!IMPORTANT]
> **Archive Rule**: `docs/task/active/` is for the single current task. Completed tasks do not stay in `active/`; move them to `docs/task/archive/`.

---

## 1. The Tiered Memory Tree

The only durable memory for this project is the Project Context tree.

| Tier | Object | Path | Purpose |
|------|--------|------|---------|
| **Project** | **Metadata** | `docs/project/metadata.yaml` | **READ FIRST**. Env, commands, and repo structure. |
| **Project** | **Context** | `docs/project/context.md` | Long-term brain: Architecture, Standards, and History. |
| **Project** | **Decisions** | `docs/decisions/*.md` | Lightweight long-lived design decisions that should outlive the current task. |
| **Task** | **Index** | `docs/task/active/index.md` | Fast launch summary for the current task. |
| **Task** | **Task** | `docs/task/active/task.md` | Scope and success criteria for the current task. |
| **Task** | **Summary** | `docs/task/active/summary.md` | Resumable image of the current task. |
| **Task** | **Verification** | `docs/task/active/verification.md` | Latest proof-of-work for the current task. |
| **Task** | **Assets** | `docs/task/active/assets/` | Captured evidence for the current task. |
| **Task** | **Commits** | `docs/task/active/commits/` | Milestone checkpoints for the current task. |
| **Task History** | **Archive** | `docs/task/archive/<task-id>/` | Completed-task snapshots moved out of `active/` to keep startup context small. |

## 2. Interaction Protocol

### Session Start (/ctx-load)
1. Read Metadata and Project Context first to establish a "worldview."
2. Read `docs/decisions/` when the current task depends on prior long-lived design choices.
3. Read `docs/task/active/index.md` for the fastest current-state view.
4. Read `docs/task/active/task.md`, `summary.md`, and `verification.md` as needed.

### Session End (/ctx-save)
- **Knowledge Promotion**: If a Session produces universal knowledge (bug fixes, infra patterns), the agent MUST update the **Project Tier** (`context.md`).
- **Decision Promotion**: If a Session produces a project-level design conclusion that should outlive the current task, the agent SHOULD add or update a file in `docs/decisions/`.
- **Hermetic Reference**: Move critical logs/evidence into `docs/task/active/assets/` before referencing them.
- **Checkpointing**: Update the active task files. Create a structured **Commit** only when a milestone is reached.
- **Task Completion**: When the active task is explicitly complete, move its snapshot into `archive/<YYYY-MM-DD>-<slug>/` and recreate `active/` from the templates.

## 3. Reasoning Integrity
Do not pollute the active task summary with failed experiments.

## 4. Task Lifecycle

### Active Task
- `docs/task/active/` is the startup surface for in-progress work.
- `docs/task/active/index.md` should describe the current goal, status, next step, latest verification, and latest milestone.
- The active tree should stay small so `/ctx-load` remains fast and reliable.

### Completed Task
- A completed task should be archived under `docs/task/archive/<YYYY-MM-DD>-<slug>/`.
- Archive the full active task snapshot: `index.md`, `task.md`, `summary.md`, `verification.md`, and any `commits/`, `assets/`, or `workstreams/`.

### Design Intent
- Keep the model simple and repo-native.
- Prevent completed work from accumulating in `active/` and degrading startup context.
