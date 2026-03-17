# Repository Collaboration Contract (v1.0)

This contract defines how multiple AI agents and human developers collaborate within this repository across different IDEs (VS Code, Cursor, Windsurf, etc.).

## 1. Single Source of Truth
- The **Git Repository** is the only durable memory.
- IDE-specific features (Artifacts, Composites, Chat History, Scratchpads) are **Ephemeral Drafts**.
- Any information required for the next agent to continue work must be committed to the repository.

## 2. Document Hierarchy
- `AGENTS.md` / `CLAUDE.md`: Entry points and IDE-specific grounding.
- `.ai-governance/`: Shared rules and logic.
- `docs/project/`: Long-term project memory (Architecture, Standards, Context).
- `docs/task/<ticket-id>/`: Short-term task memory (Plan, Progress, Verification, Handoff).

## 3. Branch-to-Task Mapping
- Branch format: `(feature|bugfix|task)/[T-]<id>[-description]`
- Example: `feat/T-123-auth` -> `docs/task/T-123/`
- Every non-trivial change should happen in a branch mapped to a task directory.

## 4. Continuity & Handoff
- Before finishing a session, an agent MUST update `docs/task/<id>/handoff.md`.
- Handoff must include:
  - **What was achieved**
  - **Where we left off**
  - **Unresolved blockers**
  - **Next suggested steps**

## 5. Anti-Regression & Verification
- All changes must be verified according to `docs/project/verify-runbook.md`.
- Evidence of verification must be recorded in `docs/task/<id>/verification.md`.
