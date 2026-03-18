# GCC (Git-Context-Controller) Model v2.1

This kit installs a **Git-Context-Controller (GCC)** memory layer. It treats AI agent context as an engineering artifact—versioned, branched, and structured—allowing multiple agents to collaborate seamlessly across sessions.

> [!WARNING]
> **Governance != VCS**: GCC records capture the "Cognitive State" (Intent/Decisions) of AI agents. They are stored in `.ai-governance/docs/` and do **not** replace Git's code history.

---

## The GCC Hierarchy

### 1. Global Awareness (`docs/project/`)
- **`metadata.yaml`**: Mandatory execution constraints. Agents **read this first** to know paths and commands.
- **`context.md`**: Long-term domain knowledge and background.

### 2. Active Task (`docs/task/active/`)
- **`task.md`**: The mission objective.
- **`verification.md`**: Global proof-of-work evidence for the entire task.
- **`branches/`**: The reasoning tree.
  - **`summary.md`**: The branch's current state and next step.
  - **`commits/`**: Structured snapshots of reasoning (`Intent`, `Decision`, `Verification`).

---

## The Write-Back Contract (Reality Check)
Agents MUST leave the task in a resumable state at the end of every session:
1. **Milestones**: achieved a valid change? -> Run `task-commit`.
2. **Partial Progress**: no milestone but made progress? -> Update `summary.md` directly (State/Next Action).

---

## Available Skills
- `task-bootstrap`: Init new GCC task tree.
- `task-context`: Reconstruct view from Metadata + Summary + Commits.
- `task-commit`: Create a milestone commit.
- `task-branch` / `task-merge`: Manage exploration paths.
- `task-archive`: Archive completed task tree.

---

## Migration from Linear Model (v1.x)
If your project uses `progress.md` or `handoff.md`:
1. Run the installer again (v2.1+).
2. `task-bootstrap` will create the new GCC tree.
3. Move your current `handoff.md` content to `branches/main/summary.md`.
4. Create an `initial-commit.md` in `commits/` reflecting the current progress.

---

## Minimum Schema Requirements

#### `metadata.yaml` must contain:
- `repo_structure`
- `execution_context` (runtime, commands)
- `governance_rules`

#### `summary.md` must contain:
- `Branch Intent`
- `Current State`
- `Known Risks`
- `Next Action`

#### `commit` must contain:
- `Intent`
- `Changes Made`
- `Decisions` (The **WHY**)
- `Verification` (Evidence)
