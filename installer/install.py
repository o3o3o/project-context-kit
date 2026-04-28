#!/usr/bin/env python3
"""
project-context-kit installer.
Installs the multi-agent project-context layer into any target repository.
Supports non-destructive merge for AGENTS.md, CLAUDE.md, and GEMINI.md.
"""
import os
import shutil
import datetime
import re
import argparse

VERSION = "1.4.0"
MARKER_START = "<!-- BEGIN PROJECT-CONTEXT -->"
MARKER_END = "<!-- END PROJECT-CONTEXT -->"
LEGACY_MARKER_START = "<!-- BEGIN AI-GOVERNANCE -->"
LEGACY_MARKER_END = "<!-- END AI-GOVERNANCE -->"


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
    Non-destructively inject a project-context block into a target file.
    - If the file is missing: create it with the project-context block.
    - If the block already exists: replace only the block content.
    - If no block: append the block at the end.
    """
    log(f"Merging project-context block into: {target_path}")

    with open(template_path, 'r') as f:
        template_content = f.read().strip()

    # Prevent nesting: if template already contains markers, don't wrap it.
    if MARKER_START in template_content and MARKER_END in template_content:
        new_block = template_content
    else:
        new_block = f"{MARKER_START}\n{template_content}\n{MARKER_END}"

    if not os.path.exists(target_path):
        with open(target_path, 'w') as f:
            f.write(f"# AI Agent Instructions\n\n{new_block}\n")
        log(f"  Created new file with project-context block.")
        return

    with open(target_path, 'r') as f:
        content = f.read()

    # Check for marker and replace or append
    pattern = re.compile(
        "("
        + re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END)
        + "|"
        + re.escape(LEGACY_MARKER_START) + r".*?" + re.escape(LEGACY_MARKER_END)
        + ")",
        re.DOTALL
    )
    if pattern.search(content):
        # REPLACE existing block
        new_content = pattern.sub(new_block, content)
        log(f"  Updated existing project-context block.")
    else:
        # APPEND new block
        new_content = content.rstrip() + "\n\n" + new_block + "\n"
        log(f"  Appended project-context block.")

    with open(target_path, 'w') as f:
        f.write(new_content)


def copy_template(src, dst, overwrite=False):
    """
    Copy a file or directory.
    - If it's a file: copy if overwrite=True or dst doesn't exist.
    - If it's a directory: merge contents instead of deleting dst.
    """
    if os.path.isdir(src):
        ensure_dir(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            copy_template(s, d, overwrite=overwrite)
    else:
        if os.path.exists(dst) and not overwrite:
            # log(f"  Skipping file (already exists): {dst}")
            return
        shutil.copy2(src, dst)
        # log(f"  Copied: {os.path.basename(src)}")


def seed_active_task_files(source_kit, target_repo):
    """
    Seed starter files for the active task tree on first install.
    This keeps /ctx-load usable immediately while remaining non-destructive
    for repositories that already contain active task state.
    """
    template_dir = os.path.join(
        source_kit, "templates/project-context/docs/task/_template"
    )
    active_dir = os.path.join(target_repo, ".project-context/docs/task/active")

    for name in ["index.md", "task.md", "tasklist.md", "summary.md", "verification.md"]:
        copy_template(
            os.path.join(template_dir, name),
            os.path.join(active_dir, name),
            overwrite=False
        )


def main():
    parser = argparse.ArgumentParser(description="Install project-context-kit")
    parser.add_argument(
        "--target", default=".",
        help="Path to the target repository (default: current directory)"
    )
    parser.add_argument(
        "--source",
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="Path to the project-context-kit source"
    )
    args = parser.parse_args()

    target_repo = os.path.abspath(args.target)
    source_kit = os.path.abspath(args.source)

    log(f"project-context-kit v{VERSION}")
    log(f"Target: {target_repo}")
    log(f"Source: {source_kit}")
    print()

    # ── 1. Create project-context directory structure ─────────────────────
    log("Step 1: Creating directory structure...")
    ensure_dir(os.path.join(target_repo, ".agents/rules"))
    ensure_dir(os.path.join(target_repo, ".agents/skills"))
    ensure_dir(os.path.join(target_repo, ".agents/workflows"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/project"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/decisions"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/task/active/commits"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/task/active/assets"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/task/archive"))
    ensure_dir(os.path.join(target_repo, ".project-context/docs/task/_template/assets"))
    print()


    # ── 2. Copy Agent rules, skills & workflows (Root .agents/) ───────────
    log("Step 2: Installing agent logic to .agents/...")
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
    copy_template(
        os.path.join(source_kit, "templates/.agents/workflows"),
        os.path.join(target_repo, ".agents/workflows"),
        overwrite=True
    )
    print()

    # ── 3. Copy agent-specific command directories (CLI Entry Points) ─────
    log("Step 3: Installing agent-specific CLI commands...")
    agent_dirs = [".claude", ".codex", ".opencode", ".gemini"]
    for d in agent_dirs:
        src_d = os.path.join(source_kit, "templates", d)
        if os.path.exists(src_d):
            copy_template(src_d, os.path.join(target_repo, d), overwrite=True)
    print()

    # ── 4. Copy shared project-context files ──────────────────────────────
    log("Step 4: Copying shared project-context files...")
    gov_src = os.path.join(source_kit, "templates/project-context")
    gov_dst = os.path.join(target_repo, ".project-context")
    for item in os.listdir(gov_src):
        if item in ["install-manifest.yaml", "docs"]:
            continue  # handled separately
        copy_template(
            os.path.join(gov_src, item),
            os.path.join(gov_dst, item),
            overwrite=True
        )
    print()

    # ── 5. Copy project doc templates (non-destructive) ───────────────────
    log("Step 5: Installing .project-context/docs/project templates (non-destructive)...")
    docs_proj_src = os.path.join(source_kit, "templates/project-context/docs/project")
    docs_proj_dst = os.path.join(target_repo, ".project-context/docs/project")
    for item in os.listdir(docs_proj_src):
        copy_template(
            os.path.join(docs_proj_src, item),
            os.path.join(docs_proj_dst, item),
            overwrite=False  # Never overwrite project docs
        )
    print()

    # ── 5b. Copy decision doc templates (non-destructive) ─────────────────
    log("Step 5b: Installing .project-context/docs/decisions templates (non-destructive)...")
    docs_dec_src = os.path.join(source_kit, "templates/project-context/docs/decisions")
    docs_dec_dst = os.path.join(target_repo, ".project-context/docs/decisions")
    if os.path.exists(docs_dec_src):
        copy_template(
            docs_dec_src,
            docs_dec_dst,
            overwrite=False
        )
    print()

    # ── 6. Copy task templates (overwrite OK, these are just starters) ────
    log("Step 6: Installing .project-context/docs/task/_template files...")
    docs_task_src = os.path.join(source_kit, "templates/project-context/docs/task/_template")
    docs_task_dst = os.path.join(target_repo, ".project-context/docs/task/_template")
    copy_template(
        docs_task_src,
        docs_task_dst,
        overwrite=True
    )
    seed_active_task_files(source_kit, target_repo)
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
    manifest_src = os.path.join(source_kit, "templates/project-context/install-manifest.yaml")
    manifest_dst = os.path.join(target_repo, ".project-context/install-manifest.yaml")

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
    log("  1. Fill in .project-context/docs/project/context.md with your project details")
    log("  2. Update the seeded active task files before or during your first real session")
    log("  3. Use 'context-bootstrap' only if you want the agent to rewrite the active task from scratch")
    log("  4. Use tasklist.md for optional task splitting and handoff")


if __name__ == "__main__":
    main()
