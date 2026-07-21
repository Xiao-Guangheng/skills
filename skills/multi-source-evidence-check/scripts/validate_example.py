from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples" / "example_output.md"


REQUIRED_SNIPPETS = [
    "查询意图改写",
    "相关证据列表",
    "证据矩阵",
    "冲突信息",
    "结论",
    "引用摘录",
    "待确认项",
]


def main() -> None:
    text = OUTPUT.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_SNIPPETS if snippet not in text]
    if missing:
        raise SystemExit(f"Missing required sections: {', '.join(missing)}")
    print("Example output validation passed.")


if __name__ == "__main__":
    main()