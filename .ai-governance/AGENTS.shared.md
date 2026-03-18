# Shared Agent Governance Rules (v1.1)

This file is the single governing instruction for all agents operating in this repository.
Codex, Antigravity, Claude, and geminicli all follow the same protocol.

---

## 🚀 STARTUP INSTRUCTIONS — Execute on Every Session Start

> These are mandatory, not optional. Do them before doing anything else.

1. **Read project context**: Open and read `.ai-governance/docs/project/context.md`. This is your grounding document.
2. **Read active task**: Open and read `.ai-governance/docs/task/active/task.md` and `.ai-governance/docs/task/active/progress.md`.
3. **Announce your understanding**: Briefly tell the user what the current task is and where work left off.
4. **Check for blockers**: Read `.ai-governance/docs/task/active/handoff.md` to see if the previous agent left any critical notes.

> If `.ai-governance/docs/task/active/` does not exist, tell the user: "No active task found. Please create one by running the `task-bootstrap` skill or creating `.ai-governance/docs/task/active/`."

---

## 🛑 SHUTDOWN INSTRUCTIONS — Execute Before Every Session End or Agent Switch

> These are mandatory. A handoff without written state is a broken handoff.

1. **Update progress**: Append what you completed this session to `.ai-governance/docs/task/active/progress.md`.
2. **Update handoff**: Rewrite `.ai-governance/docs/task/active/handoff.md` so the next agent knows exactly where to continue.
   - What was accomplished
   - Where we are now
   - What to do next
   - Any blockers or risks
3. **Do NOT leave an empty handoff.md**. Even "no changes made" is useful.

---

## 📋 Canonical State Rules

| Where | What goes here |
|-------|---------------|
| `.ai-governance/docs/project/` | Long-term project memory: architecture, standards, verify runbook |
| `.ai-governance/docs/task/active/` | Current active task: plan, progress, handoff, verification |
| `.ai-governance/docs/task/archive/` | Completed tasks (moved here when a task closes) |

- **AGENTS.md / CLAUDE.md / GEMINI.md** = entry points only, not state
- **IDE artifacts / scratchpads / chat history** = ephemeral drafts only, **not canonical**
- If you discover something important about the project architecture, write it to `.ai-governance/docs/project/architecture.md`

---

## 🤝 Multi-Agent Handoff Protocol

When switching from one agent to another (e.g., Codex → geminicli, or geminicli → Antigravity):
1. The **outgoing agent** must complete the Shutdown Instructions above.
2. The **incoming agent** must complete the Startup Instructions above.
3. The handoff file is the contract between them. Treat it seriously.
