# Skills

Skills are folders of instructions, scripts, and resources that AI agents load dynamically to improve performance on specialized tasks. Each skill teaches an AI how to complete a specific task in a repeatable way — whether that's diagnosing code errors, analyzing business metrics, parsing financial reports, or tracking meeting action items.

For more information about the Agent Skills system, check out:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

## About This Repository

This repository contains 10 production-ready skills built for the **iFlytek AI Developer Competition** (讯飞 AI 开发者大赛 Skill 赛道). Each skill targets a real-world pain point with a systematic, verifiable workflow.

### The Creation Philosophy

Building these 10 skills taught us a few things that go beyond the competition:

**1. A skill is not a prompt.** A good prompt tells an AI what to do once. A good skill teaches an AI *how to think about a class of problems*. The difference is structural — skills define diagnostic frameworks, output templates, fallback behaviors, and interactive triage rules. They don't just say "analyze this data"; they say "first classify the error type, then enumerate possible causes with evidence, then rank by likelihood, then suggest the minimal fix, then generate tests, then check security."

**2. The description is everything.** The YAML frontmatter `description` field is the only triggering mechanism. If it's too short or too vague, the skill simply won't fire when users need it. We learned to make descriptions "pushy" — explicitly stating "you MUST use this skill when..." and listing concrete trigger phrases users actually say. A description like "helps with code errors" is useless; "当你贴出代码并附上报错、异常、单测失败、堆栈日志时，必须使用此 Skill" is what actually works.

**3. Style matters more than you think.** After studying Anthropic's official skill repository, we realized that the *presentation style* of a skill shapes how seriously the AI takes its own instructions. A skill written as a technical reference manual (with task-method tables, mandatory output templates, and dependency declarations) produces more structured, reliable output than one written as a conversational guide. We deliberately gave different skills different styles to match their domains — code skills read like API documentation, analysis skills read like analyst playbooks, office skills read like SOP documents.

**4. Safety is not an afterthought.** Every skill includes field sanitization rules (formula prefix escaping, HTML escaping, pipe escaping in Markdown tables, PII redaction) and explicit "should not do" sections. In a competition setting, judges will look for these details. In production, users depend on them.

### The Creation Process

Each skill followed a disciplined workflow:

1. **Pain point mining** — What repetitive, error-prone, or time-consuming task do people actually do?
2. **Input/output definition** — What exactly goes in? What exactly comes out? If you can't draw the I/O boundary, the skill will be too vague.
3. **Workflow design** — What are the decision points? Where does the AI need to ask follow-up questions? Where should it refuse to guess?
4. **Template authoring** — Write the mandatory output format. Force the AI into a structure that's verifiable.
5. **Safety rule definition** — What can never be fabricated? What fields need sanitization? What's the processing order?
6. **Example creation** — Build a minimal but realistic test case that exercises every output field.
7. **Validation scripting** — Write `validate_example.py` and `validate_frontmatter.py` so the skill is self-testing.
8. **Iterative refinement** — Run the validation, compare output to expectations, tighten the rules.

---

## Skills Overview

| Skill | Competition Track | One-Line Description |
| --- | --- | --- |
| [code-error-triage-fix](./skills/code-error-triage-fix) | 代码智能辅助与质量保障 | Systematic code error diagnosis with multi-cause enumeration, interactive triage, unit test generation, five-dimension code review checklists, and comprehensive security scanning |
| [business-metric-anomaly-attribution](./skills/business-metric-anomaly-attribution) | 数据智能分析与应用 | KPI anomaly detection with seven-layer attribution, drill-down path suggestions, and decision tradeoff frameworks with cost/benefit/risk/cycle comparisons |
| [meeting-action-tracker](./skills/meeting-action-tracker) | 智能办公协同助理 | Scene-routed meeting-to-action pipeline producing structured minutes, accountable TODO ledgers with overdue alerts, and weekly report drafts from raw transcripts and chat logs |
| [fin-report-risk-insight](./skills/fin-report-risk-insight) | 金融材料智能解析与风险洞察 | Financial report and announcement parser that extracts key indicators, detects anomalous movements, identifies risk signals, and outputs citable conclusions with evidence excerpts |
| [multi-source-evidence-check](./skills/multi-source-evidence-check) | 多源信息检索与分析 | Multi-source evidence aggregation with query intent rewriting, cross-document contradiction resolution, evidence matrices, and citation-backed answers |
| [physical-checkup-alert-map](./skills/physical-checkup-alert-map) | 医疗健康智能理解与辅助决策 | Physical exam report interpreter with three-tier severity classification (observe/recheck/urgent), follow-up recommendations, lifestyle suggestions, and explicit red-flag alerts |
| [resume-job-match-diagnosis](./skills/resume-job-match-diagnosis) | 人才匹配与发展智能辅助 | Resume-to-JD matching engine with four-layer compatibility analysis (hard requirements, skills, business domain, expression quality), gap identification, and rewriting suggestions |
| [biz-story-pack](./skills/biz-story-pack) | 全场景内容智能创作 | Business storytelling pack generator that evaluates topic value, structures audience-aware narratives, and produces ready-to-speak scripts with hooks, evidence lists, and post-mortem cards |
| [shop-signal](./skills/shop-signal) | 电商内容智能生成与用户洞察 | E-commerce content engine that extracts purchase motivations and churn risks from reviews, generates optimized product detail pages, and produces customer service FAQ scripts |
| [govflow](./skills/govflow) | 政务公文智能处理 | Government document triage system for citizen messages — classifies inquiry types, assesses urgency levels, drafts standard replies, and generates supervision recommendations |

---

## How to Use These Skills

### Quick Start

Each skill is self-contained. To use any skill:

1. Browse the [Skills Overview](#skills-overview) table above to find the one matching your task
2. Open that skill's folder and read its `SKILL.md` — this is the complete instruction set
3. Provide the inputs described in the skill's "Input" section
4. The AI will follow the workflow defined in the skill and produce structured output

### Standard Directory Structure

Every skill follows this structure:

```
skill-name/
├── SKILL.md              # Skill definition with YAML frontmatter (name + description) and full workflow
├── README.md             # Human-readable documentation with capability overview and scoring coverage
├── examples/
│   ├── example_input.md  # Realistic test input that exercises all output fields
│   └── example_output.md # Expected output showing the complete format
├── references/
│   ├── scope.md          # What this skill covers and explicitly does NOT cover
│   └── safety.md         # Safety rules, sanitization procedures, and field processing order
├── templates/
│   └── output_template.md # The mandatory output format the AI must follow
└── scripts/
    ├── package_skill.ps1     # PowerShell packaging script to create deployable ZIP
    ├── validate_example.py   # Validates that example output contains all required sections
    └── validate_frontmatter.py # Validates YAML frontmatter format and description structure
```

### Running Validation

Each skill includes self-testing scripts. To validate any skill:

```bash
# Validate example output completeness
python skills/<skill-name>/scripts/validate_example.py

# Validate frontmatter format and description structure
python skills/<skill-name>/scripts/validate_frontmatter.py

# Package into deployable ZIP
powershell -Command "& 'skills/<skill-name>/scripts/package_skill.ps1'"
```

---

## Creating Your Own Skill

Skills are simple to create — just a folder with a `SKILL.md` file containing YAML frontmatter and Markdown instructions:

```markdown
---
name: my-skill-name
description: "What this skill does — be pushy and explicit; when to use it — include trigger conditions and anti-triggers; trigger words: phase1, phase2, phase3, phase4, phase5, phase6"
---

# My Skill Name

[Instructions that the AI will follow when this skill is active]
```

### The frontmatter requires two fields:

- **`name`** — A concise Chinese name (8-15 characters) that precisely reflects the skill's core capability. Avoid generic names like "文档助手"; prefer specific ones like "财报指标风险洞察助手".
- **`description`** — Three semicolon-separated parts: (1) what the skill does with specific input/output types, (2) when to trigger and when NOT to trigger, (3) trigger words — at least 6 concrete phrases users actually say.

### Key lessons from building these 10 skills:

- Keep `SKILL.md` under 500 lines. If you're approaching that limit, split reference material into `references/`.
- Make descriptions "pushy" — AI agents tend to undertrigger skills, so descriptions need to be aggressive about when to activate.
- Every output field should be verifiable. Write `validate_example.py` early, not as an afterthought.
- Safety rules belong in the skill body, not just in a separate file. The AI needs them in context when generating output.
- Match the writing style to the domain. A financial skill should read differently from a creative content skill.

---

## Repository Structure

```
skills/
├── README.md                                          # This file
├── .gitignore                                         # Excludes ZIPs, Python cache, OS files
│
├── skills/
│   ├── code-error-triage-fix/                         # 代码智能辅助与质量保障
│   │   ├── SKILL.md                                   # Six-stage diagnosis workflow
│   │   ├── README.md                                  # Capability overview + scoring coverage
│   │   ├── examples/                                  # IndentationError test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Debug report template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── business-metric-anomaly-attribution/           # 数据智能分析与应用
│   │   ├── SKILL.md                                   # Five-stage decision chain workflow
│   │   ├── README.md                                  # Capability overview + scoring coverage
│   │   ├── examples/                                  # GMV anomaly test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Anomaly report template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── meeting-action-tracker/                        # 智能办公协同助理
│   │   ├── SKILL.md                                   # Scene-routed workflow with output templates
│   │   ├── README.md                                  # Capability overview + scoring coverage
│   │   ├── examples/                                  # Meeting transcript test case
│   │   ├── references/                                # Scope + safety rules (with field sanitization)
│   │   ├── templates/                                 # Action tracker template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── fin-report-risk-insight/                       # 金融材料智能解析与风险洞察
│   │   ├── SKILL.md                                   # Financial indicator extraction + risk signals
│   │   ├── README.md
│   │   ├── examples/                                  # Semi-annual report test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Financial risk pack template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── multi-source-evidence-check/                   # 多源信息检索与分析
│   │   ├── SKILL.md                                   # Evidence matrix + conflict resolution
│   │   ├── README.md
│   │   ├── examples/                                  # Deadline conflict test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Evidence matrix template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── physical-checkup-alert-map/                    # 医疗健康智能理解与辅助决策
│   │   ├── SKILL.md                                   # Three-tier severity interpretation
│   │   ├── README.md
│   │   ├── examples/                                  # Annual checkup test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Checkup summary card template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── resume-job-match-diagnosis/                    # 人才匹配与发展智能辅助
│   │   ├── SKILL.md                                   # Four-layer matching analysis
│   │   ├── README.md
│   │   ├── examples/                                  # Data analyst matching test case
│   │   ├── references/                                # Scope + safety rules (with field sanitization)
│   │   ├── templates/                                 # Match card template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── biz-story-pack/                                # 全场景内容智能创作
│   │   ├── SKILL.md                                   # Story value assessment + script generation
│   │   ├── README.md
│   │   ├── examples/                                  # Business insight test case
│   │   ├── references/                                # Scope + security notes
│   │   ├── templates/                                 # Content pack template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   ├── shop-signal/                                   # 电商内容智能生成与用户洞察
│   │   ├── SKILL.md                                   # Product detail + review insight engine
│   │   ├── README.md
│   │   ├── examples/                                  # Thermos product test case
│   │   ├── references/                                # Scope + safety rules
│   │   ├── templates/                                 # Product pack template
│   │   └── scripts/                                   # Validation + packaging
│   │
│   └── govflow/                                       # 政务公文智能处理
│       ├── SKILL.md                                   # Message triage + reply drafting
│       ├── README.md
│       ├── examples/                                  # Citizen complaint test case
│       ├── references/                                # Scope + safety + public service rules
│       ├── templates/                                 # Government doc + public reply templates
│       └── scripts/                                   # Validation + packaging
```

---

## License

These skills are created for the iFlytek AI Developer Competition. Each skill is self-contained and follows the competition's submission requirements for originality, safety compliance, and documentation completeness.
