---
name: context-doctor
description: Diagnose and optionally repair the repo-local Project Context harness, including agent instructions, code rules, verification rules, and active task state.
---

# Context Doctor Skill

## Purpose
Audit and maintain the repository's Project Context harness so coding agents can reliably understand the project, follow code rules, control scope, verify work, and leave resumable state.

This skill is for harness documents, not product implementation.

## Modes

### diagnose
Use this mode by default.

Read the repo and produce a diagnosis. Do not edit files.

### apply
Use this mode only when the user explicitly asks to apply, fix, update, or implement the doctor recommendations.

Edit only allowed harness markdown and Project Context files. Do not edit product code.

## Read Set
Read only what is needed, but prefer this order:

1. Root entry files: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` if present.
2. Shared harness files:
   - `.project-context/AGENTS.shared.md`
   - `.project-context/repo-contract.md`
3. Project docs:
   - `.project-context/docs/project/metadata.yaml`
   - `.project-context/docs/project/context.md`
   - `.project-context/docs/project/architecture.md`
   - `.project-context/docs/project/coding-standards.md`
   - `.project-context/docs/project/verify-runbook.md`
4. Active task docs:
   - `.project-context/docs/task/active/index.md`
   - `.project-context/docs/task/active/task.md`
   - `.project-context/docs/task/active/tasklist.md`
   - `.project-context/docs/task/active/summary.md`
   - `.project-context/docs/task/active/verification.md`
5. Existing decisions and proposals when relevant.
6. A small repo structure sample and current git status.

## Diagnosis Questions
Answer these questions from repo evidence:

- Can a fresh agent understand the project purpose, structure, commands, current task, and verification path within 60 seconds?
- Which stable coding rules are visible in code, tests, or docs but missing from `coding-standards.md`?
- Which recurring agent workflows are missing from `AGENTS.shared.md` or `ctx-*` commands?
- Are verification commands, order, skipped checks, and evidence standards clear?
- Are active task scope, `Do Not Touch`, acceptance, owner, and WIP state clear enough for another agent?
- Are any rules only present in chat-like task notes and worth promoting to project docs or decisions?
- Are there stale paths, old naming, duplicate rules, or contradictory lifecycle instructions?
- Which details should not be promoted because they are temporary, uncertain, or task-local?

## Diagnosis Output
Return exactly these sections:

```text
## Context Doctor Report

### Instructions
[Agent entry and workflow findings.]

### Code Rules
[Stable coding rules missing, stale, or contradictory.]

### Project Context
[Context, architecture, metadata, and decision-memory findings.]

### Scope Control
[Task/tasklist/WIP/ownership/Do Not Touch findings.]

### Verification
[Runbook, verification.md, and proof-of-work findings.]

### Lifecycle
[ctx-load, ctx-save, bootstrap, checkpoint, and archive findings.]

### Recommended Updates
[Prioritized file-by-file recommendations.]

### Should Not Add
[Temporary or uncertain items that should not become rules.]
```

Keep findings concise and evidence-based. If a file is missing, say whether it is required, optional, or only useful for this repo.

## Apply Rules
When applying recommendations:

- Edit only allowed harness and Project Context files unless the user explicitly asks otherwise.
- Do not edit product code.
- Do not invent project facts. Mark uncertain items as proposals or questions.
- Respect file ownership boundaries:
  - Project Context marker blocks in root entry files are kit-owned install blocks and may be overwritten during install or upgrade.
  - Content outside Project Context marker blocks in root entry files is user-owned project guidance.
  - `.project-context/AGENTS.shared.md` is kit-owned shared protocol, not a place for project-specific rules.
  - `.project-context/docs/project/*` and `.project-context/docs/task/active/*` are project-owned harness state and are the default apply targets.
- Do not write project-specific code rules, workflows, or task guidance into `<!-- BEGIN PROJECT-CONTEXT --> ... <!-- END PROJECT-CONTEXT -->` blocks.
- Do not edit outside root entry marker blocks unless the user explicitly asks for apply mode and the recommendation belongs in project-specific entry guidance.
- Prefer `AGENTS.md` outside the Project Context marker for short project-specific agent entry notes.
- Modify `CLAUDE.md` or `GEMINI.md` outside markers only when the user explicitly asks, or when those files already contain project-specific user-owned guidance that must stay consistent.
- When modifying multiple root entry files, write short references only. Do not copy long rules across files.
- Keep root entry files short; route detail into `.project-context/docs/project/`.
- Keep `AGENTS.shared.md` as a generic harness map and shared protocol, not a long project manual.
- Write generic project-context-kit workflow improvements to `.project-context/AGENTS.shared.md` or `ctx-*` commands.
- Write project-specific agent workflow details to root entry files outside the marker, or to project docs referenced from there.
- Write stable code rules to `.project-context/docs/project/coding-standards.md`.
- Write project purpose, domain facts, and durable repo knowledge to `.project-context/docs/project/context.md`.
- Write commands, runtime, repo layout, and branch conventions to `.project-context/docs/project/metadata.yaml`.
- Write verification order and proof standards to `.project-context/docs/project/verify-runbook.md`.
- Write current task scope to `.project-context/docs/task/active/task.md`.
- Write module ownership, WIP, acceptance, and per-module verification to `.project-context/docs/task/active/tasklist.md`.
- Write latest validation evidence and gaps to `.project-context/docs/task/active/verification.md`.
- Promote long-lived design conclusions to `.project-context/docs/decisions/`.
- Put unsettled ideas in `.project-context/docs/proposals/`.

## Apply Priority
Apply fixes in this order:

1. Stale paths, old names, and contradictory instructions.
2. Missing verification commands or proof standards.
3. Missing stable coding rules.
4. Missing agent workflows or lifecycle guidance, using the ownership boundaries above.
5. Current task scope and tasklist gaps.

## Apply Output
After edits, return:

```text
## Applied Updates
[File-by-file changes.]

## Skipped Recommendations
[What was not changed and why.]

## Verification
[Static checks, smoke checks, or "Not run" with reason.]
```
