# Skills

Skills are folders of instructions, scripts, and resources that AI agents load dynamically to improve performance on specialized tasks. Each skill teaches an AI how to complete a specific task in a repeatable way — whether that's diagnosing code errors, analyzing business metrics, parsing financial reports, or tracking meeting action items.

## About This Repository

This repository contains production-ready skills built for the iFlytek AI Developer Competition (讯飞 AI 开发者大赛). Each skill targets a real-world pain point with a systematic, verifiable workflow.

| Skill | Track | Description |
| --- | --- | --- |
| [code-error-triage-fix](./code-error-triage-fix) | 代码智能辅助与质量保障 | Systematic code error diagnosis with interactive triage, unit test generation, code review checklists, and security scanning |
| [business-metric-anomaly-attribution](./business-metric-anomaly-attribution) | 数据智能分析与应用 | KPI anomaly detection with layered attribution, drill-down path suggestions, and decision tradeoff frameworks |
| [meeting-action-tracker](./meeting-action-tracker) | 智能办公协同助理 | Scene-routed meeting-to-action tracker that produces structured minutes, accountable TODO ledgers, and weekly report drafts |
| [fin-report-risk-insight](./fin-report-risk-insight) | 金融材料智能解析与风险洞察 | Financial report parsing with key metric extraction, anomaly detection, risk signal identification, and citable conclusions |
| [multi-source-evidence-check](./multi-source-evidence-check) | 多源信息检索与分析 | Multi-source evidence search, aggregation, conflict resolution, and citation-backed answers |
| [physical-checkup-alert-map](./physical-checkup-alert-map) | 医疗健康智能理解与辅助决策 | Physical exam report interpretation with tiered severity classification and follow-up recommendations |
| [resume-job-match-diagnosis](./resume-job-match-diagnosis) | 人才匹配与发展智能辅助 | Resume-to-JD matching with gap analysis, rewriting suggestions, and interview preparation |
| [biz-story-pack](./biz-story-pack) | 智能生成与创作 | Content pack generator for business storytelling, speeches, and presentation scripts |
| [shop-signal](./shop-signal) | 电商内容智能生成与用户洞察 | E-commerce product detail page generation, review insight extraction, and customer service FAQ |
| [govflow](./govflow) | 政务公文智能处理 | Government document processing with message triage, urgency assessment, and standard reply drafting |

## Creating a Skill

Skills are simple to create — just a folder with a `SKILL.md` file containing YAML frontmatter and Markdown instructions:

```markdown
---
name: my-skill-name
description: "What this skill does; when to use it; trigger words: keyword1, keyword2, keyword3, keyword4, keyword5, keyword6"
---

# My Skill Name

[Instructions that the AI will follow when this skill is active]
```

### Standard Directory Structure

```
my-skill/
├── SKILL.md           # Skill definition (required)
├── README.md          # Documentation
├── examples/          # Example inputs and outputs
│   ├── example_input.md
│   └── example_output.md
├── references/        # Scope, safety, and domain rules
│   ├── scope.md
│   └── safety.md
├── templates/         # Output templates
│   └── output_template.md
└── scripts/           # Validation and packaging
    ├── package_skill.ps1
    ├── validate_example.py
    └── validate_frontmatter.py
```
