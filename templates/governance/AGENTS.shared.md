# Shared Agent Governance Rules (v2.1 - GCC Memory Model)

This file is the single governing instruction for all agents operating in this repository.
Codex, Antigravity, Claude, and geminicli all follow the same protocol.

> [!IMPORTANT]
> **Governance != VCS**: GCC commits and branches are governance-level records stored in files. They do **not** replace Git's native commit/branch history, although they should ideally align with them. GCC records the "Why" (intent/decisions), whereas Git records the "What" (code changes).

---

## 🚀 STARTUP INSTRUCTIONS — Execute on Every Session Start

1. **Read Metadata**: Open `.ai-governance/docs/project/metadata.yaml` to understand repository-wide execution constraints (commands, build system, structure).
2. **Read Project Context**: Read `.ai-governance/docs/project/context.md`.
3. **Load GCC Context**: Activate the `task-context` skill to get an aggregated view of:
   - The active branch objective.
   - The current code state and latest milestones.
   - Any open risks or blockers.
4. **Announce**: Briefly tell the user: *"GCC Context loaded. Active branch: [name]. Latest milestone: [summary]. Next action: [action]."*

---

## 🛑 SHUTDOWN INSTRUCTIONS — Execute Before Every Session End

Every agent **must** leave the active task in a resumable state.

1. **If a milestone was reached**: Activate the `task-commit` skill to serialize your reasoning, decisions, and evidence into a structured commit file.
2. **If no milestone was reached**: Update the current branch's `summary.md` directly. Ensure the `Current State` and `Next Action` fields accurately reflect your progress or failure.
3. **Branches**: If you explore an alternative idea, activate the `task-branch` skill first to create an isolated context.

---

## 📋 Canonical State Rules

| Path | Contents |
|------|----------|
| `docs/project/metadata.yaml` | Execution constraints (env, commands, structure). |
| `docs/task/active/task.md` | High-level objective. |
| `docs/task/active/verification.md` | Final proof-of-work evidence for the entire task. |
| `branches/<name>/summary.md` | The "memory image" of the branch (state, risks, next action). |
| `branches/<name>/commits/` | The structured chain of cognition and decisions. |

- IDE artifacts / chat history are **ephemeral drafts**. The GCC tree is the **only durable memory**.
