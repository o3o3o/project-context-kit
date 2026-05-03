#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


MAP_REL = Path(".project-context/runtime/context-map.yaml")
ACTIVE = Path(".project-context/docs/task/active")
SOURCE_PATHS = [
    Path(".project-context/docs/project/metadata.yaml"),
    ACTIVE / "index.md",
    ACTIVE / "summary.md",
    ACTIVE / "task.md",
    ACTIVE / "verification.md",
    ACTIVE / "tasklist.md",
]

FORBIDDEN_DEFAULT_READ = {
    ".project-context/docs/task/archive/",
    ".project-context/docs/task/active/assets/",
    ".project-context/docs/task/active/commits/",
    ".project-context/docs/task/active/progress.md",
    ".project-context/docs/task/active/plan.md",
    ".project-context/docs/task/active/tasklist.md",
}

PLACEHOLDER_PATTERNS = [
    re.compile(r"^\s*TODO\b", re.IGNORECASE),
    re.compile(r"^\s*TBD\b", re.IGNORECASE),
    re.compile(r"^\s*placeholder\b", re.IGNORECASE),
    re.compile(r"^\s*fill in\b", re.IGNORECASE),
    re.compile(r"^\s*replace this\b", re.IGNORECASE),
    re.compile(r"\bplaceholder text\b", re.IGNORECASE),
    re.compile(r"^\s*lorem ipsum\b", re.IGNORECASE),
    re.compile(r"\{\{[^}]+\}\}"),
    re.compile(r"\[[^\]]*(state|describe|record|write|what|criterion|command|result|date|environment|notes)[^\]]*\]", re.IGNORECASE),
]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="ctx_map.py")
    parser.add_argument("command", choices=("build", "check", "print"))
    parser.add_argument("--root", default=".")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if args.command == "build":
        return build(root)
    if args.command == "check":
        return check(root)
    return print_map(root)


def build(root: Path) -> int:
    data = build_context_map(root)
    output = root / MAP_REL
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(dump_yaml(data), encoding="utf-8")
    print(f"wrote {output}")
    return 0


def check(root: Path) -> int:
    output = root / MAP_REL
    errors: list[str] = []
    warns: list[str] = []
    infos: list[str] = []

    if not output.exists():
        errors.append(f"missing {MAP_REL}")
    else:
        text = output.read_text(encoding="utf-8")
        if not has_flag(text, "generated", True) or not has_flag(text, "do_not_edit_manually", True):
            errors.append("context-map missing generated/manual flags")

        default_read = read_list_block(text, "default_read")
        if any(item in FORBIDDEN_DEFAULT_READ for item in default_read):
            errors.append("read_policy.default_read includes forbidden large/history paths")

        source_texts = load_source_texts(root)
        for rel, source_text in source_texts.items():
            if rel.name in {"index.md", "summary.md", "verification.md"} and is_placeholder_text(source_text):
                errors.append(f"placeholder text in {rel}")

        map_mtime = output.stat().st_mtime
        for rel in SOURCE_PATHS:
            source = root / rel
            if source.exists() and source.stat().st_mtime > map_mtime:
                warns.append(f"context-map older than {rel}")

        summary_text = source_texts.get(ACTIVE / "summary.md", "")
        verification_text = source_texts.get(ACTIVE / "verification.md", "")
        tasklist_text = source_texts.get(ACTIVE / "tasklist.md", "")

        if line_count(summary_text) > 20:
            warns.append("summary.md longer than 20 lines")
        if line_count(verification_text) > 80:
            warns.append("verification.md longer than 80 lines")

        tasklist_summary = summarize_tasklist(tasklist_text)
        if line_count(tasklist_text) > 500 and not tasklist_summary["current_focus"] and not any(
            tasklist_summary["summary"].values()
        ):
            warns.append("tasklist.md over 500 lines but modules summary/current_focus is empty")

        if looks_like_diary(summary_text):
            warns.append("summary.md looks like a session diary")
        if looks_like_large_logs(verification_text):
            warns.append("verification.md includes large logs")

        if has_private_evidence(tasklist_text):
            infos.append("tasklist.md references private/local evidence paths")

        if (root / ".project-context/docs/task/archive").exists():
            infos.append("archive exists and is not default-referenced")

        if (root / ".project-context/docs/task/active/plan.md").exists() or (
            root / ".project-context/docs/task/active/progress.md"
        ).exists():
            infos.append("optional deep files plan/progress exist but are excluded from default reads")

    for msg in errors:
        print(f"ERROR: {msg}")
    for msg in warns:
        print(f"WARN: {msg}")
    for msg in infos:
        print(f"INFO: {msg}")
    return 1 if errors else 0


def print_map(root: Path) -> int:
    output = root / MAP_REL
    if not output.exists():
        print(f"missing {MAP_REL}")
        return 1
    sys.stdout.write(output.read_text(encoding="utf-8"))
    return 0


def build_context_map(root: Path) -> dict[str, Any]:
    metadata = read_text(root / SOURCE_PATHS[0])
    index = read_text(root / SOURCE_PATHS[1])
    summary = read_text(root / SOURCE_PATHS[2])
    task = read_text(root / SOURCE_PATHS[3])
    verification = read_text(root / SOURCE_PATHS[4])
    tasklist = read_text(root / SOURCE_PATHS[5])
    tasklist_summary = summarize_tasklist(tasklist)

    current = build_current(index, summary, task, verification)
    project_context_key = parse_scalar_metadata(metadata, "project_context_key")

    project: dict[str, Any] = {
        "name": root.name,
        "purpose": "repo-local context layer for coding agents",
    }
    if project_context_key:
        project["context_key"] = project_context_key

    return {
        "schema": "project-context.context-map.v1",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "generated_by": "ctx_map.py",
        "generated": True,
        "do_not_edit_manually": True,
        "source_of_truth": [str(path) for path in SOURCE_PATHS],
        "project": project,
        "current": current,
        "modules": {
            "source": str(SOURCE_PATHS[5]),
            "default_read": False,
            "summary": tasklist_summary["summary"],
            "current_focus": tasklist_summary["current_focus"],
        },
        "routes": {
            "commands": ".project-context/docs/project/metadata.yaml",
            "project_context": ".project-context/docs/project/context.md",
            "task_scope": ".project-context/docs/task/active/task.md",
            "current_summary": ".project-context/docs/task/active/summary.md",
            "verification": ".project-context/docs/task/active/verification.md",
            "modules": ".project-context/docs/task/active/tasklist.md",
            "decisions": ".project-context/docs/decisions/",
            "archive": ".project-context/docs/task/archive/",
        },
        "read_policy": {
            "default_read": [str(MAP_REL)],
            "fallback_if_missing_runtime": [
                ".project-context/docs/task/active/index.md",
                ".project-context/docs/task/active/summary.md",
            ],
            "read_if_claiming_module": [".project-context/docs/task/active/tasklist.md"],
            "read_if_verifying": [
                ".project-context/docs/task/active/verification.md",
                ".project-context/docs/project/verify-runbook.md",
            ],
            "never_default_read": [
                ".project-context/docs/task/archive/",
                ".project-context/docs/task/active/assets/",
                ".project-context/docs/task/active/commits/",
                ".project-context/docs/task/active/progress.md",
                ".project-context/docs/task/active/plan.md",
            ],
        },
        "freshness": {
            "stale_check": "compare runtime mtime with active source files",
            "stale_if": [
                "runtime generated_at is older than active/index.md",
                "runtime generated_at is older than active/summary.md",
                "runtime generated_at is older than active/verification.md",
                "runtime generated_at is older than active/tasklist.md",
            ],
        },
    }


def build_current(index: str, summary: str, task: str, verification: str) -> dict[str, Any]:
    index_sections = parse_sections(index)
    task_sections = parse_sections(task)
    verification_sections = parse_sections(verification)

    goal = clean_value(first_paragraph(index_sections.get("Current Goal", "")))
    status = clean_value(first_paragraph(index_sections.get("Current Status", "")))
    next_action = clean_value(first_paragraph(index_sections.get("Next Step", "")))
    latest_verification = clean_value(first_paragraph(index_sections.get("Latest Verification", "")))
    blocked_by_text = clean_value(first_paragraph(index_sections.get("Known Risks / Blockers", "")))

    if not latest_verification:
        latest_verification = clean_value(first_paragraph(verification_sections.get("Latest Automated Results", "")))
    if not latest_verification:
        latest_verification = clean_value(first_paragraph(verification_sections.get("Latest Manual / Review Evidence", "")))
    if not latest_verification:
        latest_verification = clean_value(first_paragraph(verification_sections.get("Task Status", "")))

    if not goal:
        goal = clean_value(first_paragraph(task_sections.get("Description", "")))

    task_title = extract_task_title(task)
    task_id = extract_task_id(task_title)

    return {
        "task_id": task_id,
        "goal": goal or None,
        "status": status or None,
        "phase": infer_phase(status, summary, task_sections),
        "next_action": next_action or None,
        "blocked_by": blocked_by_text if blocked_by_text and re.search(r"\bblocked?\b|\bblocker\b|阻塞|卡住", blocked_by_text, re.IGNORECASE) else None,
        "latest_verification": latest_verification or None,
    }


def summarize_tasklist(text: str) -> dict[str, Any]:
    modules = parse_module_blocks(text)
    counts = {"todo": 0, "in_progress": 0, "blocked": 0, "done": 0}
    current_focus: list[dict[str, str | None]] = []

    for module in modules:
        status = normalize_status(module.get("status", ""))
        if status in counts:
            counts[status] += 1
        if status != "done":
            focus = module_focus(module)
            if focus:
                current_focus.append(focus)

    total = sum(counts.values())
    if len(current_focus) > 5:
        current_focus = current_focus[:5]
    return {
        "summary": {"total": total, **counts},
        "current_focus": current_focus,
    }


def parse_module_blocks(text: str) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_key: str | None = None

    for line in text.splitlines():
        if re.match(r"^##\s+Example\b", line):
            if current:
                blocks.append(current)
            break
        match = re.match(r"^##\s+((?:M|T)\d+\b.*)$", line)
        if match:
            if current:
                blocks.append(current)
            current = {"title": match.group(1).strip()}
            current_key = None
            continue

        if current is None:
            continue

        field = re.match(r"^-\s+([^:：]+)[:：]\s*(.*)$", line)
        if field:
            key = normalize_field_name(field.group(1).strip())
            current[key] = field.group(2).strip()
            current_key = key
            continue

        item = re.match(r"^-\s+(.*)$", line)
        if item and current_key:
            current[current_key] = (current.get(current_key, "") + " " + item.group(1).strip()).strip()
            continue

    if current:
        blocks.append(current)
    return blocks


def module_focus(module: dict[str, str]) -> dict[str, str | None] | None:
    title = module.get("title", "").strip()
    goal = module.get("goal", "").strip()
    if not goal:
        goal = module.get("target", "").strip()
    acceptance = module.get("acceptance", "").strip()
    status = normalize_status(module.get("status", ""))
    owner = module.get("owner") or module.get("assignee")
    blocked_by = module.get("blocked_by") or module.get("blocker")
    if not title:
        return None
    item = {
        "id": title.split(" ", 1)[0],
        "title": truncate_one_line(title, 80),
        "status": status or None,
        "owner": owner or None,
    }
    if goal:
        item["summary"] = truncate_one_line(goal, 96)
    elif acceptance:
        item["summary"] = truncate_one_line(acceptance, 96)
    if blocked_by:
        item["blocked_by"] = truncate_one_line(blocked_by, 96)
    return item


def normalize_field_name(name: str) -> str:
    mapping = {
        "状态": "status",
        "负责人": "owner",
        "目标": "goal",
        "验收标准": "acceptance",
        "阻塞原因": "blocked_by",
        "最近更新": "last_update",
        "备注": "notes",
        "工作流": "workflow",
        "允许修改": "allowed_paths",
        "不要修改": "do_not_touch",
        "优先级": "priority",
    }
    if name in mapping:
        return mapping[name]
    return name.lower().replace(" ", "_")


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current_title = ""
    current_lines: list[str] = []

    for line in text.splitlines():
        heading = re.match(r"^##+\s+(.+)$", line)
        if heading:
            if current_title:
                sections[current_title] = current_lines[:]
            current_title = heading.group(1).strip()
            current_lines = []
            continue
        if current_title:
            current_lines.append(line)

    if current_title:
        sections[current_title] = current_lines

    return {title: "\n".join(lines).strip() for title, lines in sections.items()}


def first_paragraph(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    parts: list[str] = []
    for line in lines:
        if not line:
            if parts:
                break
            continue
        if line.startswith("- "):
            parts.append(line[2:].strip())
        else:
            parts.append(line)
    return truncate_one_line(" ".join(parts).strip())


def extract_task_title(task_text: str) -> str:
    first = next((line.strip() for line in task_text.splitlines() if line.strip().startswith("#")), "")
    if first.startswith("# Task:"):
        return first[len("# Task:") :].strip()
    if first.startswith("# "):
        return first[2:].strip()
    return ""


def extract_task_id(task_title: str) -> str | None:
    if not task_title:
        return None
    if "[" in task_title or "]" in task_title:
        return None
    if " - " in task_title:
        return task_title.split(" - ", 1)[0].strip() or None
    return task_title.strip() or None


def infer_phase(status: str, summary: str, task_sections: dict[str, str]) -> str | None:
    text = status.lower()
    if not text:
        return None
    if "review" in text:
        return "review"
    if "blocked" in text:
        return "blocked"
    if "in progress" in text or "progress" in text:
        return "in_progress"
    if "done" in text or "complete" in text:
        return "done"
    return None


def parse_scalar_metadata(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*\"?(.*?)\"?\s*$", text, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip() or None


def load_source_texts(root: Path) -> dict[Path, str]:
    data: dict[Path, str] = {}
    for rel in SOURCE_PATHS:
        data[rel] = read_text(root / rel)
    return data


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_flag(text: str, key: str, expected: bool) -> bool:
    pattern = rf"^{re.escape(key)}:\s*{'true' if expected else 'false'}\s*$"
    return re.search(pattern, text, re.MULTILINE) is not None


def read_list_block(text: str, key: str) -> list[str]:
    lines = text.splitlines()
    result: list[str] = []
    capture = False
    base_indent: int | None = None

    for line in lines:
        if not capture:
            if re.match(rf"^\s*{re.escape(key)}:\s*$", line):
                capture = True
            continue
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if base_indent is None:
            base_indent = indent
        if indent < base_indent:
            break
        item = re.match(r"^\s*-\s+(.+)$", line)
        if item:
            result.append(unquote_yaml_scalar(item.group(1).strip()))
    return result


def unquote_yaml_scalar(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return bytes(value[1:-1], "utf-8").decode("unicode_escape")
    return value


def is_placeholder_text(text: str) -> bool:
    if not text.strip():
        return True
    if any(pattern.search(line) for line in text.splitlines() for pattern in PLACEHOLDER_PATTERNS):
        return True
    blank_fields = sum(1 for line in text.splitlines() if is_blank_template_field(line))
    return blank_fields >= 2


def is_blank_template_field(line: str) -> bool:
    return re.match(
        r"^\s*-\s*(Goal|Status|Lead chain|Do not split|Module IDs|Module status|Action|Command|Result|Date|Checkpoint|State|Item|Check|Environment|Notes|Gap)\s*:\s*$",
        line,
        re.IGNORECASE,
    ) is not None


def looks_like_diary(text: str) -> bool:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 6:
        return False
    diary_markers = sum(
        1
        for line in lines
        if re.search(r"\b(today|yesterday|worked on|finished|started|morning|afternoon|evening)\b", line, re.I)
        or re.match(r"^\d{4}-\d{2}-\d{2}", line)
    )
    return diary_markers >= 3


def looks_like_large_logs(text: str) -> bool:
    if text.count("```") >= 2:
        return True
    lines = [line for line in text.splitlines() if line.strip()]
    long_lines = sum(1 for line in lines if len(line) > 140)
    return long_lines >= 10 or any(token in text.lower() for token in ("traceback", "stderr", "stdout", "stack trace"))


def has_private_evidence(text: str) -> bool:
    return any(token in text for token in ("/private/", "/tmp/", "~/", "file://", "localhost"))


def normalize_status(value: str) -> str:
    lowered = value.strip().lower()
    if lowered in {"todo", "待办"}:
        return "todo"
    if lowered in {"in progress", "in_progress", "进行中"}:
        return "in_progress"
    if lowered in {"blocked", "阻塞"}:
        return "blocked"
    if lowered in {"done", "完成", "已完成"}:
        return "done"
    return ""


def clean_value(value: str) -> str:
    if not value:
        return ""
    if "{{" in value or re.search(r"\[[^\]]+\]", value):
        return ""
    if is_placeholder_text(value):
        return ""
    labels = r"(Goal|Status|Lead chain|Do not split|Module IDs|Module status|Action|Command|Result|Date|Checkpoint|State|Item|Check|Environment|Notes|Gap)"
    normalized = value.replace("**", "")
    if re.fullmatch(rf"(?:{labels}:\s*)+", normalized.strip(), re.IGNORECASE):
        return ""
    return value


def line_count(text: str) -> int:
    return 0 if not text else len(text.splitlines())


def truncate_one_line(text: str, limit: int = 160) -> str:
    collapsed = " ".join(text.split())
    if len(collapsed) <= limit:
        return collapsed
    return collapsed[: limit - 1].rstrip() + "…"


def dump_yaml(value: Any, indent: int = 0) -> str:
    pad = " " * indent
    if isinstance(value, dict):
        if not value:
            return f"{pad}{{}}"
        lines: list[str] = []
        for key, item in value.items():
            if isinstance(item, dict) and not item:
                lines.append(f"{pad}{key}: {{}}")
            elif isinstance(item, list) and not item:
                lines.append(f"{pad}{key}: []")
            elif isinstance(item, (dict, list)):
                lines.append(f"{pad}{key}:")
                lines.append(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}{key}: {yaml_scalar(item)}")
        return "\n".join(lines)
    if isinstance(value, list):
        if not value:
            return f"{pad}[]"
        lines = []
        for item in value:
            if isinstance(item, (dict, list)):
                lines.append(f"{pad}-")
                lines.append(dump_yaml(item, indent + 2))
            else:
                lines.append(f"{pad}- {yaml_scalar(item)}")
        return "\n".join(lines)
    return f"{pad}{yaml_scalar(value)}"


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
