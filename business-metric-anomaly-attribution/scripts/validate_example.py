from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples" / "example_output.md"


REQUIRED_SNIPPETS = [
    "数据范围与口径判断",
    "核心指标概览",
    "异常波动清单",
    "异常分层判断",
    "可能原因拆解",
    "待验证线索",
    "钻取路径建议",
    "决策权衡框架",
    "结论摘要",
    "行动项清单",
]


def main() -> None:
    text = OUTPUT.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_SNIPPETS if snippet not in text]
    if missing:
        raise SystemExit(f"Missing required sections: {', '.join(missing)}")
    print("Example output validation passed.")


if __name__ == "__main__":
    main()