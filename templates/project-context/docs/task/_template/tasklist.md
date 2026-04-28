# Active Task Module List

Use this file when the active task has modules that may be assigned separately.
It is the scope and state surface for manual multi-agent handoff.

## Usage Rules
- Keep the main chain in `task.md`; list only decomposed modules here.
- Update `Status`, `Owner`, `Branch`, `Last Update`, and `Notes` whenever a module changes state.
- Use `Todo`, `In Progress`, `Blocked`, or `Done` for module status.
- Keep at most one module `In Progress` per agent unless the user explicitly asks for parallel work.
- Keep each module small enough to review and verify independently.
- Do not mark `Done` without verification evidence.

## Module Template

## Mx [Module Title]
- Priority: P1
- Status: Todo
- Owner:
- Branch:
- Goal:
- Allowed Paths:
  - `[path-or-glob]`
- Do Not Touch:
  - `[path-or-boundary]`
- Acceptance:
  - `[What must be true to mark this module done]`
- Suggested Agent Profile:
- Dependencies:
  - `none`
- Last Update:
- Notes:
- Verification:

## Example

## M2 Backend Logs
- Priority: P1
- Status: Todo
- Owner:
- Branch:
- Goal: Normalize backend log output for the current phase without changing the core state machine.
- Allowed Paths:
  - `backend/logging/**`
  - `tests/logging/**`
- Do Not Touch:
  - `backend/planning/**`
  - `backend/contracts/**`
- Acceptance:
  - Backend logs use the agreed shape for the targeted flow.
  - Existing logging tests are updated or added for the changed surface.
- Suggested Agent Profile: backend-observability
- Dependencies:
  - `M0 contract baseline finalized`
- Last Update:
- Notes:
- Verification:
