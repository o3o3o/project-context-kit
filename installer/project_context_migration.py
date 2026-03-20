#!/usr/bin/env python3
import os
import re
import shutil


OLD_DIR = ".ai-governance"
NEW_DIR = ".project-context"
LEGACY_COMMAND_PATHS = [
    ".claude/commands/gov-context.md",
    ".claude/commands/gov-writeback.md",
    ".codex/prompts/gov-context.md",
    ".codex/prompts/gov-writeback.md",
    ".opencode/commands/gov-context.md",
    ".opencode/commands/gov-writeback.md",
    ".gemini/commands/gov-context.toml",
    ".gemini/commands/gov-writeback.toml",
    ".agents/workflows/gov-context.md",
    ".agents/workflows/gov-writeback.md",
    ".project-context/commands/gov-context.md",
    ".project-context/commands/gov-writeback.md",
]


def ensure_dir(path, log=None):
    if not os.path.exists(path):
        os.makedirs(path)
        if log:
            log(f"Created directory: {path}")


def copy_tree_no_overwrite(src, dst, log=None):
    if not os.path.exists(src):
        return
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        dst_root = dst if rel == "." else os.path.join(dst, rel)
        ensure_dir(dst_root, log=log)
        for d in dirs:
            ensure_dir(os.path.join(dst_root, d), log=log)
        for name in files:
            src_file = os.path.join(root, name)
            dst_file = os.path.join(dst_root, name)
            if os.path.exists(dst_file):
                continue
            shutil.copy2(src_file, dst_file)
            if log:
                log(f"Migrated legacy file: {dst_file}")


def replace_in_file(path, replacements, log=None):
    if not os.path.exists(path):
        return
    with open(path, "r") as f:
        content = f.read()
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        if log:
            log(f"Updated references in: {path}")


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file(path, content, log=None):
    parent = os.path.dirname(path)
    if parent:
        ensure_dir(parent, log=log)
    with open(path, "w") as f:
        f.write(content)


def extract_section(markdown, heading):
    pattern = re.compile(
        rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL
    )
    match = pattern.search(markdown)
    if not match:
        return None
    return match.group(1).strip()


def first_nonempty_line(text):
    if not text:
        return None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def migrate_legacy_active_task(target_repo, log=None):
    task_root = os.path.join(target_repo, NEW_DIR, "docs/task/active")
    legacy_paths = [
        os.path.join(task_root, "branches/main/summary.md"),
        os.path.join(task_root, "branches", "main", "summary.md"),
    ]
    legacy_summary_path = next((path for path in legacy_paths if os.path.exists(path)), None)
    if not legacy_summary_path:
        return

    summary_path = os.path.join(task_root, "summary.md")
    index_path = os.path.join(task_root, "index.md")
    if os.path.exists(summary_path) and os.path.exists(index_path):
        if log:
            log("Legacy task layout detected, but active-task files already exist. Skipping summary/index migration.")
        return

    if log:
        log(f"Migrating legacy task state from {legacy_summary_path}")
    legacy_summary = read_file(legacy_summary_path)
    current_state = extract_section(legacy_summary, "Current State") or "Migrated from legacy branch summary."
    risks = extract_section(legacy_summary, "Known Risks / Blockers") or "- None recorded"
    next_action = extract_section(legacy_summary, "Next Action") or "Review migrated task state and continue."
    intent = extract_section(legacy_summary, "Branch Intent") or "Continue the current active task."
    latest_commits = extract_section(legacy_summary, "Latest Commits") or "- None recorded"

    if not os.path.exists(summary_path):
        migrated_summary = "\n".join([
            "# Active Task Summary",
            "",
            "## Current State",
            current_state,
            "",
            "## What Changed Recently",
            latest_commits,
            "",
            "## Known Risks / Blockers",
            risks,
            "",
            "## Next Action",
            next_action,
            "",
        ])
        write_file(summary_path, migrated_summary, log=log)
        if log:
            log(f"Wrote migrated summary: {summary_path}")

    if not os.path.exists(index_path):
        current_status = first_nonempty_line(current_state) or "Migrated from legacy layout"
        latest_milestone = first_nonempty_line(latest_commits) or "Migrated from legacy branch summary"
        migrated_index = "\n".join([
            "# Active Task Index",
            "",
            "## Current Goal",
            first_nonempty_line(intent) or "Continue the current active task.",
            "",
            "## Current Status",
            current_status,
            "",
            "## Next Step",
            first_nonempty_line(next_action) or "Review migrated task state and continue.",
            "",
            "## Latest Verification",
            "Not migrated automatically. Review verification.md if present.",
            "",
            "## Latest Milestone",
            latest_milestone,
            "",
        ])
        write_file(index_path, migrated_index, log=log)
        if log:
            log(f"Wrote migrated index: {index_path}")


def migrate_legacy_root(target_repo, log=None):
    legacy_root = os.path.join(target_repo, OLD_DIR)
    new_root = os.path.join(target_repo, NEW_DIR)
    if not os.path.exists(legacy_root):
        return
    if log:
        log("Migrating legacy .ai-governance tree into .project-context...")
    copy_tree_no_overwrite(legacy_root, new_root, log=log)


def rewrite_legacy_root_references(target_repo, log=None):
    replacements = [
        (".ai-governance/", ".project-context/"),
        ("/gov-context", "/ctx-load"),
        ("/gov-writeback", "/ctx-save"),
    ]
    for path in [
        os.path.join(target_repo, "AGENTS.md"),
        os.path.join(target_repo, "CLAUDE.md"),
        os.path.join(target_repo, "GEMINI.md"),
    ]:
        replace_in_file(path, replacements, log=log)


def has_migrated_project_context(target_repo):
    new_root = os.path.join(target_repo, NEW_DIR)
    if not os.path.exists(new_root):
        return False

    key_paths = [
        os.path.join(new_root, "docs/project"),
        os.path.join(new_root, "docs/task/active"),
    ]
    return all(os.path.exists(path) for path in key_paths)


def remove_path(path, log=None):
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    if log:
        log(f"Removed legacy path: {path}")


def prune_legacy_command_files(target_repo, log=None):
    for rel_path in LEGACY_COMMAND_PATHS:
        remove_path(os.path.join(target_repo, rel_path), log=log)


def cleanup_legacy_after_migration(target_repo, log=None):
    prune_legacy_command_files(target_repo, log=log)
    remove_path(os.path.join(target_repo, OLD_DIR), log=log)
