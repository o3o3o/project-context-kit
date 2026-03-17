# Shared Agent Governance Rules

## Core Principles
1. **Repository as Truth**: The Git repository is the sole durable source of truth. Internal IDE memory, conversation history, and temporary artifacts are secondary and transient.
2. **Context Persistence**: Any discovery about the codebase or architecture must be updated in `docs/project/`.
3. **Task Atomic States**: Every task must have its own directory in `docs/task/<ticket-id>/`.
4. **Handoff First**: No agent should leave a task in an ambiguous state. Always update `handoff.md` and `progress.md`.

## Operation Workflow
1. **Initialize**: Check current branch. If it matches `feat/T-<id>` or similar, the task directory is `docs/task/T-<id>/`. If it doesn't exist, run `task-bootstrap`.
2. **Sync**: Read `docs/project/` to understand the project landscape. Read `docs/task/<id>/` to understand the specific mission.
3. **Execute**: Perform work. If `AGENTS.md` rules conflict with this shared layer, the shared layer takes precedence for multi-IDE coordination.
4. **Finalize**: 
   - Update `progress.md` with what was actually done.
   - Update `verification.md` with test results.
   - Update `handoff.md` for the next agent (Antigravity, Codex, or Claude).

## Artifacts Rule (Antigravity)
Artifacts are for presentation and drafting. **Approved** plans and **final** documentation must be copied from artifacts into the `docs/` folder.
