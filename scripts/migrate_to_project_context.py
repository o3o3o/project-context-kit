#!/usr/bin/env python3
import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INSTALLER_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "installer")
if INSTALLER_DIR not in sys.path:
    sys.path.insert(0, INSTALLER_DIR)

from project_context_migration import (  # noqa: E402
    OLD_DIR,
    NEW_DIR,
    cleanup_legacy_after_migration,
    ensure_dir,
    has_migrated_project_context,
    migrate_legacy_active_task,
    migrate_legacy_root,
    rewrite_legacy_root_references,
)


def log(msg):
    print(f"[*] {msg}")


def warn(msg):
    print(f"[!] {msg}")


def main():
    parser = argparse.ArgumentParser(description="Migrate .ai-governance to .project-context")
    parser.add_argument("--target", default=".", help="Path to the target repository")
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Auto-confirm legacy cleanup after a successful migration"
    )
    args = parser.parse_args()

    target_repo = os.path.abspath(args.target)
    old_path = os.path.join(target_repo, OLD_DIR)
    new_path = os.path.join(target_repo, NEW_DIR)

    if not os.path.exists(old_path):
        warn(f"No {OLD_DIR} directory found in {target_repo}")
        return

    ensure_dir(new_path)
    migrate_legacy_root(target_repo, log=log)
    migrate_legacy_active_task(target_repo, log=log)
    rewrite_legacy_root_references(target_repo, log=log)

    if has_migrated_project_context(target_repo):
        should_cleanup = args.yes
        if not should_cleanup:
            reply = input(
                "[?] Migration data is present under .project-context/. "
                "Delete legacy .ai-governance and old gov-* command files now? [y/N]: "
            ).strip().lower()
            should_cleanup = reply in {"y", "yes"}
        if should_cleanup:
            cleanup_legacy_after_migration(target_repo, log=log)
        else:
            warn("Legacy .ai-governance and any old gov-* command files were left in place.")

    log("Migration complete.")
    if os.path.exists(old_path):
        log(f"Old directory preserved at {old_path}")
    log(f"New directory available at {new_path}")


if __name__ == "__main__":
    main()
