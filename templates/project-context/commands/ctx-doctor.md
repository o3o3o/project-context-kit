---
name: ctx-doctor
description: Diagnose or repair the repo-local Project Context harness.
---

# /ctx-doctor

Purpose:
Diagnose whether this repository's Project Context harness gives coding agents clear instructions, code rules, scope control, verification rules, and resumable state.

## Default Mode: diagnose

Use diagnose mode unless the user explicitly asks to apply, fix, update, or implement recommendations.
Reply in the user's language unless the user explicitly requests another language.

Steps:
1. Read root entry files if present: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`.
2. Read `.project-context/AGENTS.shared.md` and `.project-context/repo-contract.md`.
3. Read project docs: `metadata.yaml`, `context.md`, `architecture.md`, `coding-standards.md`, and `verify-runbook.md`.
4. Read active task docs: `index.md`, `task.md`, `tasklist.md`, `summary.md`, and `verification.md`.
5. Inspect a small repo structure sample and current git status.
6. Activate `context-doctor` and return the diagnosis report.

## Apply Mode

Use apply mode only when the user explicitly asks for it.

Rules:
- Edit only allowed harness markdown and Project Context files.
- Do not edit product code.
- Treat `<!-- BEGIN PROJECT-CONTEXT --> ... <!-- END PROJECT-CONTEXT -->` blocks in root entry files as kit-owned install blocks that may be overwritten by install or upgrade.
- Do not write project-specific rules into Project Context marker blocks.
- Treat content outside root entry marker blocks as user-owned project guidance.
- Apply project-specific recommendations to the current project's `.project-context/**` docs and user-owned root entry content outside marker blocks.
- Do not edit kit-owned install templates or generated install blocks during normal doctor apply.
- Treat `templates/**`, `installer/**`, `manifests/**`, and Project Context marker blocks as product-owned install surfaces. They may be overwritten by install or upgrade.
- If a recommendation requires changing an install surface, report it under `Skipped Recommendations` and recommend changing the project-context-kit source separately, then reinstalling.
- Prefer project docs for durable project-specific rules.
- If a root entry note is needed, prefer `AGENTS.md` outside the marker and keep it short.
- Modify `CLAUDE.md` or `GEMINI.md` outside markers only when the user explicitly asks or those files already contain matching project-specific guidance.
- Keep `.project-context/AGENTS.shared.md` generic; do not put project-specific code rules there.
- Do not modify `templates/root/*.append.md` during normal doctor apply for one target repo's project-specific workflow.
- Write stable code rules to `docs/project/coding-standards.md`.
- Write durable project facts to `docs/project/context.md`.
- Write verification order and proof standards to `docs/project/verify-runbook.md`.
- Write generic project-context-kit workflows to `.project-context/AGENTS.shared.md` or `ctx-*` commands.
- Write task-local scope and state to `docs/task/active/`.
- Put uncertain ideas in `docs/proposals/`, not in rules.

## Output

In diagnose mode, return:

```text
## Context Doctor Report
### Instructions
### Code Rules
### Project Context
### Scope Control
### Verification
### Lifecycle
### Recommended Updates
### Should Not Add
```

In apply mode, return:

```text
## Applied Updates
## Skipped Recommendations
## Verification
```
