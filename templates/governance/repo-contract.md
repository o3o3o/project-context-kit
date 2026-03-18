# Repository Collaboration Contract (v2.0 - GCC Model)

This contract defines how multiple AI agents collaborate in this repository using a **Git-Context-Controller (GCC)** memory model.

---

## 1. The Single Source of Truth

- The **GCC Memory Tree** in `.ai-governance/docs/task/active/` is the only durable memory.
- Ephemeral logs, chat history, and IDE artifacts are NOT canonical.

## 2. Active Task: The GCC Tree

- We don't use linear progress tracking. We use **commits** and **branches**.
- When you achieve a distinct milestone or finish a session, you MUST write a **commit**.
- When you want to explore a new approach, you MUST create a **branch**.

## 3. GCC Document Hierarchy

| Path | Purpose |
|------|---------|
| `.ai-governance/docs/project/metadata.yaml` | Essential execution constraints (env, structure, build cmds) |
| `.ai-governance/docs/project/context.md` | Background and domain logic |
| `.ai-governance/docs/task/active/task.md` | The core objective |
| `../branches/main/summary.md` | The aggregated current state of the main branch |
| `../branches/main/commits/` | The structured reasoning/execution chain |

## 4. Mandatory Write-Back (Commit Protocol)

At the end of a session, do NOT just append text somewhere:
1. **Create a Commit File**: Using the commit template, summarize *Intent*, *Changes Made*, *Decisions*, and *Next Steps*. Save it to `commits/YYYY-MM-DD-00X.md`.
2. **Update Branch Summary**: Ensure the `summary.md` in the current branch reflects reality.

## 5. Agent Skills for GCC

We provide CLI skills to manage this memory tree:
- `task-commit`: Write a commit and update summary.
- `task-branch`: Create an isolated exploration branch.
- `task-context`: Synthesize current GCC state into a flat view.
