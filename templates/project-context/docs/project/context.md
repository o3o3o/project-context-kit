# Project Context

## Purpose
[Describe what this project does, who uses it, and its core value proposition.]

## Cold-start Map
- **What this project is**: [One sentence product/domain summary]
- **How it is organized**: See `architecture.md` and `metadata.yaml`.
- **How to run it**: See `metadata.yaml` execution commands.
- **How to verify it**: See `verify-runbook.md`.
- **What is in progress**: See `.project-context/docs/task/active/index.md`.

## Tech Stack
- **Language**: [e.g., TypeScript, Python]
- **Framework**: [e.g., Next.js, FastAPI]
- **Database**: [e.g., PostgreSQL, Redis]
- **Infrastructure**: [e.g., AWS, Docker]

## Key Directories
- `src/`: Source code
- `tests/`: Test suites
- `docs/`: Project documentation
- `.project-context/`: Agent-readable project memory and task state

## Common Commands
- Canonical commands live in `metadata.yaml`.
- Keep this section as a human-readable summary only.

## Current Priorities
1. [Highest priority item]
2. [Secondary priority item]

## Durable Facts
- [Project fact or domain rule that should survive across tasks]

## Related Project Docs
- `metadata.yaml`: runtime, commands, repo structure, branch convention
- `architecture.md`: system shape and module boundaries
- `coding-standards.md`: stable style and safety constraints
- `verify-runbook.md`: verification order and proof standard

## Definition of Done (DoD)
- [ ] Code follows coding standards
- [ ] Tests pass
- [ ] Relevant project docs are updated when behavior, commands, or architecture change
- [ ] Handoff state is updated in `.project-context/docs/task/active/`
