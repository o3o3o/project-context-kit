#!/usr/bin/env python3
"""
Repo Governance Kit Installer (v1.1)
Installs the multi-agent governance layer into any target repository.
Supports non-destructive merge for AGENTS.md, CLAUDE.md, and GEMINI.md.
"""
import os
import shutil
import datetime
import re
import argparse

VERSION = "1.1.0"
MARKER_START = "<!-- BEGIN AI-GOVERNANCE -->"
MARKER_END = "<!-- END AI-GOVERNANCE -->"


def log(msg):
    print(f"[*] {msg}")


def warn(msg):
    print(f"[!] {msg}")


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created directory: {path}")


def merge_file(target_path, template_path):
    """
    Non-destructively inject a governance block into a target file.
    - If the file is missing: create it with the governance block.
    - If the block already exists: replace only the block content.
    - If no block: append the block at the end.
    """
    log(f"Merging governance block into: {target_path}")

    with open(template_path, 'r') as f:
        template_content = f.read().strip()

    new_block = f"{MARKER_START}\n{template_content}\n{MARKER_END}"

    if not os.path.exists(target_path):
        with open(target_path, 'w') as f:
            f.write(f"# AI Agent Instructions\n\n{new_block}\n")
        log(f"  Created new file with governance block.")
        return

    with open(target_path, 'r') as f:
        content = f.read()

    # Check for marker and replace or append
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL
    )
    if pattern.search(content):
        new_content = pattern.sub(new_block, content)
        log(f"  Updated existing governance block.")
    else:
        new_content = content.rstrip() + "\n\n" + new_block + "\n"
        log(f"  Appended governance block.")

    with open(target_path, 'w') as f:
        f.write(new_content)


def copy_template(src, dst, overwrite=False):
    """Copy a file or directory. Skips if dst exists and overwrite=False."""
    if os.path.exists(dst) and not overwrite:
        log(f"  Skipping (already exists): {dst}")
        return

    if os.path.isdir(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        log(f"  Copied directory: {os.path.basename(src)} -> {dst}")
    else:
        shutil.copy2(src, dst)
        log(f"  Copied: {os.path.basename(src)}")


def main():
    parser = argparse.ArgumentParser(description="Install Repo Governance Kit")
    parser.add_argument(
        "--target", default=".",
        help="Path to the target repository (default: current directory)"
    )
    parser.add_argument(
        "--source",
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="Path to the repo-governance-kit source"
    )
    args = parser.parse_args()

    target_repo = os.path.abspath(args.target)
    source_kit = os.path.abspath(args.source)

    log(f"Repo Governance Kit v{VERSION}")
    log(f"Target: {target_repo}")
    log(f"Source: {source_kit}")
    print()

    # ── 1. Create governance directory structure ───────────────────────────
    log("Step 1: Creating directory structure...")
    ensure_dir(os.path.join(target_repo, ".agents/rules"))
    ensure_dir(os.path.join(target_repo, ".agents/skills"))
    ensure_dir(os.path.join(target_repo, ".ai-governance/docs/project"))
    ensure_dir(os.path.join(target_repo, ".ai-governance/docs/task/active/branches/main/commits"))
    ensure_dir(os.path.join(target_repo, ".ai-governance/docs/task/archive"))
    ensure_dir(os.path.join(target_repo, ".ai-governance/docs/task/_template/branches/main/commits"))
    print()


    # ── 2. Copy shared governance files ───────────────────────────────────
    log("Step 2: Copying shared governance files...")
    gov_src = os.path.join(source_kit, "templates/governance")
    gov_dst = os.path.join(target_repo, ".ai-governance")
    for item in os.listdir(gov_src):
        if item in ["install-manifest.yaml", "docs"]:
            continue  # handled separately
        copy_template(
            os.path.join(gov_src, item),
            os.path.join(gov_dst, item),
            overwrite=True
        )
    print()

    # ── 3. Copy Agent rules & skills (Root .agents/) ──────────────────────
    log("Step 3: Installing agent rules and skills to .agents/...")
    copy_template(
        os.path.join(source_kit, "templates/.agents/rules"),
        os.path.join(target_repo, ".agents/rules"),
        overwrite=True
    )
    copy_template(
        os.path.join(source_kit, "templates/.agents/skills"),
        os.path.join(target_repo, ".agents/skills"),
        overwrite=True
    )
    print()

    # ── 4. Copy agent-specific command directories ────────────────────────
    log("Step 4: Installing agent-specific command directories...")
    agent_dirs = [".claude", ".codex", ".opencode", ".gemini"]
    for d in agent_dirs:
        src_d = os.path.join(source_kit, "templates", d)
        if os.path.exists(src_d):
            copy_template(src_d, os.path.join(target_repo, d), overwrite=True)
    print()

    # ── 5. Copy project doc templates (non-destructive) ───────────────────
    log("Step 5: Installing .ai-governance/docs/project templates (non-destructive)...")
    docs_proj_src = os.path.join(source_kit, "templates/governance/docs/project")
    docs_proj_dst = os.path.join(target_repo, ".ai-governance/docs/project")
    for item in os.listdir(docs_proj_src):
        copy_template(
            os.path.join(docs_proj_src, item),
            os.path.join(docs_proj_dst, item),
            overwrite=False  # Never overwrite project docs
        )
    print()

    # ── 6. Copy task templates (overwrite OK, these are just starters) ────
    log("Step 6: Installing .ai-governance/docs/task/_template files...")
    docs_task_src = os.path.join(source_kit, "templates/governance/docs/task/_template")
    docs_task_dst = os.path.join(target_repo, ".ai-governance/docs/task/_template")
    copy_template(
        docs_task_src,
        docs_task_dst,
        overwrite=True
    )
    print()

    # ── 7. Merge entry files (AGENTS.md, CLAUDE.md, GEMINI.md) ───────────
    log("Step 7: Merging agent entry files...")
    templates_root = os.path.join(source_kit, "templates/root")
    merge_file(
        os.path.join(target_repo, "AGENTS.md"),
        os.path.join(templates_root, "AGENTS.append.md")
    )
    merge_file(
        os.path.join(target_repo, "CLAUDE.md"),
        os.path.join(templates_root, "CLAUDE.append.md")
    )
    merge_file(
        os.path.join(target_repo, "GEMINI.md"),
        os.path.join(templates_root, "GEMINI.append.md")
    )
    print()

    # ── 8. Generate install manifest ──────────────────────────────────────
    log("Step 8: Generating install manifest...")
    manifest_src = os.path.join(source_kit, "templates/governance/install-manifest.yaml")
    manifest_dst = os.path.join(target_repo, ".ai-governance/install-manifest.yaml")

    with open(manifest_src, 'r') as f:
        manifest_content = f.read()

    manifest_content = manifest_content.replace("{{INSTALLED_AT}}", datetime.datetime.now().isoformat())
    manifest_content = manifest_content.replace("{{VERSION}}", VERSION)

    with open(manifest_dst, 'w') as f:
        f.write(manifest_content)
    log(f"  Generated: {manifest_dst}")
    print()

    log("✅ Installation complete!")
    log("Next steps:")
    log("  1. Fill in .ai-governance/docs/project/context.md with your project details")
    log("  2. Run 'task-bootstrap' skill in your AI agent to create the first active task")


if __name__ == "__main__":
    main()
