from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples" / "example_output.md"


REQUIRED_SNIPPETS = [
    "问题类型判断",
    "可能错因清单",
    "优先级排序",
    "定位依据",
    "最小修复建议",
    "安全风险检查",
    "验证步骤",
    "单元测试建议",
    "需要补充的信息",
]


def main() -> None:
    text = OUTPUT.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_SNIPPETS if snippet not in text]
    if missing:
        raise SystemExit(f"Missing required sections: {', '.join(missing)}")
    print("Example output validation passed.")


if __name__ == "__main__":
    main()