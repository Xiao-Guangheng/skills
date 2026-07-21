from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit("Missing YAML frontmatter.")

    lines = [line for line in match.group(1).splitlines() if line.strip()]
    if len(lines) != 2:
        raise SystemExit(f"Frontmatter must contain exactly 2 fields, found {len(lines)}.")
    if not lines[0].startswith("name: "):
        raise SystemExit("First frontmatter field must be name.")
    if not lines[1].startswith("description: "):
        raise SystemExit("Second frontmatter field must be description.")

    description = lines[1][len("description: "):].strip().strip('"')
    parts = [part.strip() for part in description.split("；") if part.strip()]
    if len(parts) < 3:
        raise SystemExit("Description must contain three semicolon-separated parts.")
    if "触发词：" not in parts[-1]:
        raise SystemExit("Description must include a trigger-word segment.")

    triggers = [item.strip() for item in parts[-1].split("触发词：", 1)[1].split("、") if item.strip()]
    if len(triggers) < 6:
        raise SystemExit(f"Expected at least 6 trigger words, found {len(triggers)}.")

    print("Frontmatter validation passed.")


if __name__ == "__main__":
    main()