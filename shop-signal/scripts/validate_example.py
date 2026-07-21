from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "examples" / "example_input.md",
    ROOT / "examples" / "example_output.md",
    ROOT / "references" / "scope.md",
    ROOT / "references" / "safety.md",
    ROOT / "templates" / "product_pack_template.md",
]


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in FILES if not path.exists()]
    if missing:
        raise SystemExit(f"Missing files: {', '.join(missing)}")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    lines = skill_text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit("SKILL.md frontmatter is missing")
    if "name:" not in skill_text or "description:" not in skill_text:
        raise SystemExit("SKILL.md frontmatter must contain name and description")

    input_text = (ROOT / "examples" / "example_input.md").read_text(encoding="utf-8")
    output_text = (ROOT / "examples" / "example_output.md").read_text(encoding="utf-8")
    if "保温杯" not in input_text:
        raise SystemExit("Example input is incomplete")
    if "商品定位判断" not in output_text or "客服回复建议" not in output_text:
        raise SystemExit("Example output is incomplete")

    print("Example validation passed.")


if __name__ == "__main__":
    main()
