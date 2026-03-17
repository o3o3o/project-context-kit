# Repo Governance Kit

A standardized governance layer for multi-agent and multi-IDE collaboration.

## Overview
This kit solves the "fragmented memory" problem in AI-driven development. Instead of project context being trapped in private IDE sessions, chat histories, or temporary artifacts, this kit enforces a **Repository-as-Truth** model.

By installing this kit, you enable different agents (Antigravity, Codex, Claude) to work on the same task across different platforms while maintaining a perfect, durable record of plans, progress, and handoffs.

## Core Philosophy
1. **Durable over Ephemeral**: Git is the only source of truth.
2. **Standardized Context**: All agents look at the same `docs/project/` and `docs/task/` folders.
3. **Atomic Task States**: Every branch maps to a specific task directory.
4. **Non-Destructive Integration**: Works alongside existing `AGENTS.md` and `CLAUDE.md` files.

## Installation
To install the governance kit into your current project:

```bash
# Clone the kit (or point to the local path)
path/to/repo-governance-kit/installer/install.sh .
```

## How to Collaborate

### Recommended Agent Roles
- **Antigravity**: Strategy, repo research, planning, and final diff review.
- **Codex**: Rapid implementation and boilerplate generation.
- **Claude**: Review, debugging, code hardening, and verification.

### Workflow
1. **New Task**: Create a branch `feat/T-123-auth`.
2. **Bootstrap**: Run the `task-bootstrap` skill to create `docs/task/T-123/`.
3. **Plan**: Write your approach to `docs/task/T-123/plan.md`.
4. **Implement**: Code as usual.
5. **Handoff**: If switching agents (e.g., from VS Code to Claude.ai), update `docs/task/T-123/handoff.md`.
6. **Verify**: Use the `verify-change` skill to record test results in `docs/task/T-123/verification.md`.

## Directory Structure (Post-Installation)
```text
target-repo/
  .ai-governance/        # Shared rules and Antigravity skills
  docs/
    project/             # Long-term project memory
    task/                # Canonical state per task
  AGENTS.md              # Antigravity entry point (merged)
  CLAUDE.md              # Claude entry point (merged)
```

## Branch Naming & Task Mapping
Task directories are derived from the branch name using the pattern: `[type]/[T-]<id>[-description]`.
- `feat/T-123-ui-refresh` -> `docs/task/T-123/`
- `fix/456-bug` -> `docs/task/456/`

## Upgrading
Just re-run the `install.sh` script. It will update the governance block in `AGENTS.md` / `CLAUDE.md` and sync the `.ai-governance/` folder while preserving your custom modifications in `docs/project/`.
