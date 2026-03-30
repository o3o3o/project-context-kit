# Shared Agent Project Context Rules (v3.2)

This file is the single governing instruction for all agents operating in this repository.
Codex, Antigravity, Claude, and geminicli all follow the same protocol.

> [!IMPORTANT]
> **Hermeticity Rule**: You are a self-contained agent. Never link to files (logs, artifacts) outside `.project-context/`. 
> - If evidence is important: Inline the text into `verification.md` or a commit.
> - If data is large: Copy it into `.project-context/docs/task/active/assets/` before referencing it.

---

## 🚀 STARTUP INSTRUCTIONS (/ctx-load)

1. **Read Metadata**: Open `.project-context/docs/project/metadata.yaml` to understand repository-wide execution constraints.
2. **Read Project Context**: Read `.project-context/docs/project/context.md` for架构, coding standards, and project history.
3. **Read Decisions If Relevant**: Read `.project-context/docs/decisions/` when the current task depends on prior long-lived design choices.
4. **Read Fast Task View**: Open `.project-context/docs/task/active/index.md` first.
5. **Load Project Context**: Activate the `context-load` skill to synthesize current task state and risks.
6. **Bootstrap If Needed**: If the active task files do not exist yet, initialize them from `.project-context/docs/task/_template/` or activate `context-bootstrap`.
7. **Announce**: Briefly tell the user: *"Project context loaded. Architecture and task state synchronized."*

---

## 🛑 SHUTDOWN INSTRUCTIONS (/ctx-save)

Every agent **must** leave the active task in a resumable and hermetic state.

1. **Knowledge Extraction**: If you learned universal project patterns or fixes, update `docs/project/context.md`.
2. **Checkpointing**:
   - **Always**: Refresh `docs/task/active/index.md`, `task.md`, `summary.md`, and `verification.md` as needed.
   - **Milestone Reached**: Activate the `context-checkpoint` skill to serialize reasoning and evidence.
   - **Task Completed**: If `verification.md` explicitly says `Status: Complete` or `Status: Done`, move the active task snapshot into `docs/task/archive/<YYYY-MM-DD>-<slug>/`, then recreate `active/` from the task templates.
3. **Decision Capture**: If you reached a conclusion that should remain true across future tasks, add or update a file in `docs/decisions/` instead of leaving it only in `summary.md`.
4. **Hermetic Verification**: Ensure all references in your summaries are internal to `.project-context/`.

---

## 📋 Canonical State Rules

| Path | Contents |
|------|----------|
| `docs/project/metadata.yaml` | Execution constraints (env, commands, structure). |
| `docs/project/context.md` | Architecture, Domain context, and Permanent Knowledge. |
| `docs/decisions/*.md` | Lightweight long-lived design decisions that should outlive the current task. |
| `docs/task/active/index.md` | Fast launch summary for the current task. |
| `docs/task/active/task.md` | High-level objective for the current task. |
| `docs/task/active/summary.md` | Default resumable image of the current state. |
| `docs/task/active/verification.md` | Latest validation state for the current task. |
| `docs/task/active/assets/` | Large artifacts captured for the current task. |
| `docs/task/active/commits/` | Structured milestone checkpoints for the current task. |
| `docs/task/archive/<task-id>/` | Immutable snapshots of completed tasks, including task docs, verification, commits, and assets. |

- IDE artifacts / chat history are **ephemeral drafts**. The Project Context tree is the **only durable memory**.
- `active/` is for the single current task.
- Completed tasks must not remain in `active/`.
