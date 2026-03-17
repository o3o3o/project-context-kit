# Merge Rules for AI Governance Kit

## Principle 1: Non-Destructive
- Never delete existing content in `AGENTS.md` or `CLAUDE.md`.
- Use boundary markers `<!-- BEGIN AI-GOVERNANCE -->` and `<!-- END AI-GOVERNANCE -->`.

## Principle 2: Idempotency
- If markers exist, replace everything between them with the latest template.
- If markers don't exist, append to the end of the file.
- If the file doesn't exist, create it with a minimal header + the governance block.

## Principle 3: Protection of Custom Docs
- Do not overwrite `docs/project/*.md` if they already exist and have content other than the default template header.
- The installer should detect if a file is substantially different from the template before offering to update it.

## Principle 4: Manifest Tracking
- Every installation or upgrade must update `.ai-governance/install-manifest.yaml`.
- Record the timestamp and the version installed.
