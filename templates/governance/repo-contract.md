# Repository Collaboration Contract (v1.1)

This contract defines how multiple AI agents collaborate in this repository: Antigravity, Codex, Claude, and geminicli.

---

## 1. The Single Source of Truth

- The **Git repository** is the only durable memory.
- IDE chat history, scratchpads, and artifacts are **ephemeral** — they will not survive an agent switch.
- Every piece of information the next agent needs **must be written to the repository before you stop**.

## 2. Active Task: One at a Time

- There is always one "active task" in `docs/task/active/`.
- No branch mapping. No ticket IDs in paths. All agents read from the same `docs/task/active/`.
- When a task ends, it is moved to `docs/task/archive/<date-name>/` via the `task-archive` skill.

## 3. Document Hierarchy

| Path | Purpose |
|------|---------|
| `docs/project/context.md` | Long-term: What the project is, tech stack, commands |
| `docs/project/architecture.md` | Long-term: How the code is structured |
| `docs/project/coding-standards.md` | Long-term: How code should be written |
| `docs/project/verify-runbook.md` | Long-term: How to verify changes |
| `docs/task/active/task.md` | Current: Task objective and success criteria |
| `docs/task/active/plan.md` | Current: How we plan to do it |
| `docs/task/active/progress.md` | Current: Running log of what's been done |
| `docs/task/active/handoff.md` | Current: State and next steps for the incoming agent |
| `docs/task/active/verification.md` | Current: Test results and evidence |

## 4. Mandatory Write-Back

Before ending any session:
1. **Append** to `docs/task/active/progress.md` — what you did this session
2. **Rewrite** `docs/task/active/handoff.md` — where we are and what to do next

This is **non-negotiable**. A session that ends without updating these two files is an incomplete session.

## 5. Agent Entry Points

| Agent | Entry File | Shared Rules |
|-------|------------|-------------|
| Antigravity | `AGENTS.md` | `.ai-governance/AGENTS.shared.md` |
| Claude | `CLAUDE.md` | `.ai-governance/CLAUDE.shared.md` |
| geminicli | `GEMINI.md` | `.ai-governance/GEMINI.shared.md` |
| Codex | `AGENTS.md` | `.ai-governance/AGENTS.shared.md` |

## 6. Anti-Regression

- All changes must be verified per `docs/project/verify-runbook.md`.
- Verification evidence goes to `docs/task/active/verification.md`.
