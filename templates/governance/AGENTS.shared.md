# Shared Agent Governance Rules (v2.0 - GCC Memory Model)

This file is the single governing instruction for all agents operating in this repository.
Codex, Antigravity, Claude, and geminicli all follow the same protocol.

We use a **Git-Context-Controller (GCC) Model**. 
There is no linear `progress.md` or `handoff.md`. We use `commits/` and `branches/`.

---

## 🚀 STARTUP INSTRUCTIONS — Execute on Every Session Start

> These are mandatory, not optional. Do them before doing anything else.

1. **Read project context**: Open `.ai-governance/docs/project/context.md` and `.ai-governance/docs/project/metadata.yaml`.
2. **Read active task state**: Run the `task-context` skill to get an aggregated view of the current task, active branch, and latest commits.
3. **Announce your understanding**: Briefly tell the user:
   - What the active branch is.
   - What the latest commit achieved.
   - What your next action is based on `summary.md`.

> If `.ai-governance/docs/task/active/` does not exist, tell the user to run `task-bootstrap`.

---

## 🛑 SHUTDOWN INSTRUCTIONS — Execute Before Every Session End or Agent Switch

> These are mandatory. A session without a commit is lost context.

1. **Create a Commit**: Always run the `task-commit` skill to summarize your work into a structured commit file under `.ai-governance/docs/task/active/branches/<branch-name>/commits/`.
2. **Do Not Append**: Do not write to linear log files. Commit your context.
3. **Branching**: If you are trying a new experimental approach, run `task-branch` to create an isolated context before modifying code.

---

## 📋 Canonical State Rules

| Where | What goes here |
|-------|---------------|
| `.ai-governance/docs/project/` | Global context: architecture, metadata, standards |
| `.ai-governance/docs/task/active/` | Current active task tree |
| `../branches/<name>/commits/` | Granular intelligence: reasoning, changes made, blockers |
| `../branches/<name>/summary.md` | The current active status of that branch |

- **IDE artifacts / chat history** = ephemeral drafts only, **not canonical**.
