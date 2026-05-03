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
| **Project** | **Metadata** | `docs/project/metadata.yaml` | Env, commands, and repo structure; read when map or task needs command detail. |
| **Project** | **Context** | `docs/project/context.md` | Long-term brain: Architecture, Standards, and History. |
| **Project** | **Decisions** | `docs/decisions/*.md` | Lightweight long-lived design decisions that should outlive the current task. |
| **Runtime** | **Context Map** | `runtime/context-map.yaml` | Generated routing cache for `/ctx-load`; not source of truth. |
| **Project** | **Proposals** | `docs/proposals/*.md` | Drafts, discussion notes, and candidate changes that are not final yet. |
| **Task** | **Index** | `docs/task/active/index.md` | Fast launch summary for the current task. |
| **Task** | **Task** | `docs/task/active/task.md` | Scope and success criteria for the current task. |
| **Task** | **Task List** | `docs/task/active/tasklist.md` | Optional module list for scope control, ownership, WIP, and per-module verification. |
| **Task** | **Summary** | `docs/task/active/summary.md` | Resumable image of the current task. |
| **Task** | **Verification** | `docs/task/active/verification.md` | Latest proof-of-work for the current task. |
| **Task** | **Assets** | `docs/task/active/assets/` | Captured evidence for the current task. |
| **Task** | **Commits** | `docs/task/active/commits/` | Milestone checkpoints for the current task. |
| **Task History** | **Archive** | `docs/task/archive/<task-id>/` | Completed-task snapshots moved out of `active/` to keep startup context small. |

## 2. Interaction Protocol

### Session Start (/ctx-load)
1. Read `runtime/context-map.yaml` first if present and fresh.
2. If the map is missing, stale, or has placeholder `current` fields, read `docs/task/active/index.md` and `summary.md` first.
3. Read `docs/project/metadata.yaml` and `docs/project/context.md` when the map or task needs them.
4. Read `docs/decisions/` when the current task depends on prior long-lived design choices.
5. Read `docs/task/active/task.md`, `verification.md`, and `tasklist.md` only as needed.

### Session End (/ctx-save)
- **Knowledge Promotion**: If a Session produces universal knowledge (bug fixes, infra patterns), the agent MUST update the **Project Tier** (`context.md`).
- **Decision Promotion**: If a Session produces a project-level design conclusion that should outlive the current task, the agent SHOULD add or update a file in `docs/decisions/`.
- **Hermetic Reference**: Move critical logs/evidence into `docs/task/active/assets/` before referencing them.
- **Checkpointing**: Update the active task files first, then run `python .project-context/scripts/ctx_map.py build` and `python .project-context/scripts/ctx_map.py check` before ending. Create a structured **Commit** only when a milestone is reached.
- **Task Completion**: When the active task is explicitly complete, move its snapshot into `archive/<YYYY-MM-DD>-<slug>/` and recreate `active/` from the templates.

## 3. Reasoning Integrity
Do not pollute the active task summary with failed experiments.

## 4. Task Lifecycle

### Active Task
- `docs/task/active/` is the startup surface for in-progress work.
- `docs/task/active/index.md` should describe the current goal, status, next step, latest verification, and latest milestone.
- The active tree should stay small so `/ctx-load` remains fast and reliable.
- `tasklist.md` is deep context; do not treat it as default startup input.

### Completed Task
- A completed task should be archived under `docs/task/archive/<YYYY-MM-DD>-<slug>/`.
- Archive the full active task snapshot: `index.md`, `task.md`, `tasklist.md`, `summary.md`, `verification.md`, and any `commits/` or `assets/`.

### Design Intent
- Keep the model simple and repo-native.
- Prevent completed work from accumulating in `active/` and degrading startup context.
