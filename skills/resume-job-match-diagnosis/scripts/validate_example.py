from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples" / "example_output.md"


REQUIRED_SNIPPETS = [
    "岗位画像判断",
    "候选人核心亮点",
    "匹配度结论",
    "硬条件匹配表",
    "能力匹配表",
    "主要缺口与风险",
    "简历改写建议",
    "是否建议推进",
]


def main() -> None:
    text = OUTPUT.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_SNIPPETS if snippet not in text]
    if missing:
        raise SystemExit(f"Missing required sections: {', '.join(missing)}")
    print("Example output validation passed.")


if __name__ == "__main__":
    main()