#!/usr/bin/env python3
import os
from pathlib import Path
import re
from datetime import date


# ---------- Utilities ----------
def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s).strip("-")
    return s or "untitled"


def read_multiline(prompt: str) -> str:
    print(f"\n{prompt}\nEnter text. Finish with a single '.' on a line:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == ".":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(content)


# ---------- Anchors & inputs ----------
# Anchor everything to the directory containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

category = input("\nEnter your project category: ").strip()
project = input("Enter your project name: ").strip()

category_slug = slugify(category)
project_slug = slugify(project)

# Working dir to keep raw section txts (optional, nice for later edits)
work_dir = SCRIPT_DIR / category_slug / project_slug
# Wiki output directory
wiki_dir = SCRIPT_DIR / "wikifiles" / category_slug
# Final markdown path
md_path = wiki_dir / f"{project_slug}.md"

# ---------- Collect content ----------
# If you prefer to paste from an editor later, you can just hit '.' to skip.
abstract = read_multiline("Abstract")
objectives = read_multiline("Objectives")
methodology = read_multiline("Methodology")
est_timeline = read_multiline("Estimated Timelines")
deliverables = read_multiline("Possible Deliverables")

# Save the raw section files for future editing (no brittle size checks)
write_text(work_dir / "abstract.txt", abstract)
write_text(work_dir / "objectives.txt", objectives)
write_text(work_dir / "methodology.txt", methodology)
write_text(work_dir / "est_timeline.txt", est_timeline)
write_text(work_dir / "deliverables.txt", deliverables)


# ---------- Render Markdown ----------
def sec(title: str, body: str) -> str:
    body = body.strip()
    return f"## {title}\n\n{body}\n" if body else ""


markdown = (
    f"# {project}\n\n"
    f"*Category:* {category}\n\n"
    f"*Created:* {date.today().isoformat()}\n\n"
    + sec("Abstract", abstract)
    + sec("Objectives", objectives)
    + sec("Methodology", methodology)
    + sec("Estimated Timelines", est_timeline)
    + sec("Possible Deliverables", deliverables)
).strip() + "\n"

# ---------- Write output (atomically via tmp) ----------
wiki_dir.mkdir(parents=True, exist_ok=True)
tmp_path = md_path.with_suffix(".md.tmp")
write_text(tmp_path, markdown)
tmp_path.replace(md_path)

print(f"\n✅ Saved:\n  {md_path}")
print(f"🗂️  Source notes:\n  {work_dir}")
