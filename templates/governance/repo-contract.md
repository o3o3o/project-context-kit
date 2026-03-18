# Repository Collaboration Contract (v2.1 - GCC Model)

This contract defines how multiple AI agents (Codex, Antigravity, Claude, geminicli) collaborate using a **Git-Context-Controller (GCC)** memory model.

> [!WARNING]
> **GCC is Governance, not VCS**: GCC commits/branches are local files in `.ai-governance/docs/`. They track "Cognitive State" (Intent/Decisions). They do **not** replace project source control (Git), but should be updated alongside it.

---

## 1. The GCC Memory Tree

The only durable memory for this project is the GCC tree under `.ai-governance/docs/task/active/`. 

| Object | Path | Purpose |
|--------|------|---------|
| **Metadata** | `docs/project/metadata.yaml` | **READ FIRST**. Env, commands, and repo structure. |
| **Task** | `docs/task/active/task.md` | The current overall objective. |
| **Verification** | `docs/task/active/verification.md` | Final validation evidence. |
| **Summary** | `branches/<name>/summary.md` | The current status/risk/action for a branch. |
| **Commits** | `branches/<name>/commits/` | The history of intent and decisions. |

## 2. Interaction Protocol

### session Start
1. Read `metadata.yaml` first.
2. Run `task-context` to build a mental model of the active branch and recent milestones.

### Session End (The Write-Back Contract)
- **Milestone Reached**: Run `task-commit`. This creates a structured file and updates the summary.
- **Partial Progress**: Directly update the branch's `summary.md` (Current State / Next Action).
- **Evidence**: Ensure verification data is recorded in the commit or `verification.md`.

## 3. Branching for Exploration
Do not pollute the `main` branch with failed experiments. Use `task-branch` to create an isolated reasoning folder for radical changes or hypothesis tests.
