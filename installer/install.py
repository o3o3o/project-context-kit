#!/usr/bin/env python3
import os
import shutil
import datetime
import re
import argparse

# Configuration
VERSION = "1.0.0"
MARKER_START = "<!-- BEGIN AI-GOVERNANCE -->"
MARKER_END = "<!-- END AI-GOVERNANCE -->"

def log(msg):
    print(f"[*] {msg}")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        log(f"Created directory: {path}")

def merge_file(target_path, template_path):
    log(f"Merging governance block into {target_path}...")
    
    with open(template_path, 'r') as f:
        template_content = f.read().strip()
    
    new_block = f"{MARKER_START}\n{template_content}\n{MARKER_END}"
    
    if not os.path.exists(target_path):
        with open(target_path, 'w') as f:
            f.write(f"# AI Agent Instructions\n\n{new_block}\n")
        log(f"Created new file: {target_path}")
        return

    with open(target_path, 'r') as f:
        content = f.read()

    pattern = re.compile(f"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}", re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_block, content)
        log(f"Updated existing governance block in {target_path}")
    else:
        new_content = content.rstrip() + "\n\n" + new_block + "\n"
        log(f"Appended governance block to {target_path}")

    with open(target_path, 'w') as f:
        f.write(new_content)

def copy_template(src, dst, overwrite=False):
    if os.path.exists(dst) and not overwrite:
        log(f"Skipping existing file: {dst}")
        return
    
    if os.path.isdir(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        log(f"Copied directory: {src} -> {dst}")
    else:
        shutil.copy2(src, dst)
        log(f"Copied file: {src} -> {dst}")

def main():
    parser = argparse.ArgumentParser(description="Install Repo Governance Kit")
    parser.add_argument("--target", default=".", help="Target repository path")
    parser.add_argument("--source", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))), help="Source kit path")
    args = parser.parse_args()

    target_repo = os.path.abspath(args.target)
    source_kit = os.path.abspath(args.source)

    log(f"Installing Repo Governance Kit v{VERSION}")
    log(f"Target: {target_repo}")

    # 1. Create structure
    ensure_dir(os.path.join(target_repo, ".ai-governance/.agents/rules"))
    ensure_dir(os.path.join(target_repo, ".ai-governance/.agents/skills"))
    ensure_dir(os.path.join(target_repo, "docs/project"))
    ensure_dir(os.path.join(target_repo, "docs/task/_template"))

    # 2. Copy shared governance files
    gov_src = os.path.join(source_kit, "templates/governance")
    gov_dst = os.path.join(target_repo, ".ai-governance")
    for item in os.listdir(gov_src):
        if item == "install-manifest.yaml": continue
        copy_template(os.path.join(gov_src, item), os.path.join(gov_dst, item), overwrite=True)

    # 3. Copy Antigravity rules & skills
    copy_template(os.path.join(source_kit, "templates/.agents/rules"), os.path.join(target_repo, ".ai-governance/.agents/rules"), overwrite=True)
    copy_template(os.path.join(source_kit, "templates/.agents/skills"), os.path.join(target_repo, ".ai-governance/.agents/skills"), overwrite=True)

    # 4. Copy Documentation Templates (Non-destructive for root docs/project)
    docs_proj_src = os.path.join(source_kit, "templates/docs/project")
    docs_proj_dst = os.path.join(target_repo, "docs/project")
    for item in os.listdir(docs_proj_src):
        copy_template(os.path.join(docs_proj_src, item), os.path.join(docs_proj_dst, item), overwrite=False)

    # Copy task templates (Overwrite OK as they are templates)
    copy_template(os.path.join(source_kit, "templates/docs/task/_template"), os.path.join(target_repo, "docs/task/_template"), overwrite=True)

    # 5. Merge AGENTS.md and CLAUDE.md
    merge_file(os.path.join(target_repo, "AGENTS.md"), os.path.join(source_kit, "templates/root/AGENTS.append.md"))
    merge_file(os.path.join(target_repo, "CLAUDE.md"), os.path.join(source_kit, "templates/root/CLAUDE.append.md"))

    # 6. Generate Manifest
    manifest_src = os.path.join(source_kit, "templates/governance/install-manifest.yaml")
    manifest_dst = os.path.join(target_repo, ".ai-governance/install-manifest.yaml")
    
    with open(manifest_src, 'r') as f:
        manifest_content = f.read()
    
    manifest_content = manifest_content.replace("{{INSTALLED_AT}}", datetime.datetime.now().isoformat())
    
    with open(manifest_dst, 'w') as f:
        f.write(manifest_content)
    log(f"Generated manifest: {manifest_dst}")

    log("Installation successful!")

if __name__ == "__main__":
    main()
