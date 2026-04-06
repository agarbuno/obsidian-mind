#!/usr/bin/env python3
"""Classify freeform vault input and print routing hints."""

from __future__ import annotations

import argparse
import json
import re
import sys


SIGNALS = [
    {
        "name": "DECISION",
        "message": "Consider creating a decision record in work/active/ and logging it in work/Index.md.",
        "patterns": [
            "decided",
            "deciding",
            "decision",
            "we chose",
            "agreed to",
            "let's go with",
            "the call is",
            "we're going with",
            "決定した",
            "決めた",
            "合意した",
            "결정했어",
            "결정했습니다",
            "합의했어",
            "决定了",
            "我们决定",
            "确定了",
            "同意",
        ],
    },
    {
        "name": "INCIDENT",
        "message": "Consider using `.codex/commands/incident-capture.md` or writing to work/incidents/.",
        "patterns": [
            "incident",
            "outage",
            "pagerduty",
            "severity",
            "p0",
            "p1",
            "p2",
            "sev1",
            "sev2",
            "postmortem",
            "rca",
            "インシデント",
            "障害",
            "인시던트",
            "장애",
            "事件",
            "故障",
            "事后分析",
        ],
    },
    {
        "name": "1:1 CONTENT",
        "message": "Consider creating a work/1-1/ note and updating the related person note in org/people/.",
        "patterns": [
            "1:1",
            "1-1",
            "1-on-1",
            "one on one",
            "1on1",
            "catch up with",
            "sync with",
            "ワンオンワン",
            "원온원",
            "一对一",
            "单独面谈",
        ],
    },
    {
        "name": "WIN",
        "message": "Consider adding the result to perf/Brag Doc.md with links to evidence notes.",
        "patterns": [
            "shipped",
            "shipping",
            "ships",
            "launched",
            "launching",
            "launches",
            "completed",
            "completing",
            "completes",
            "released",
            "releasing",
            "releases",
            "deployed",
            "deploying",
            "deploys",
            "achieved",
            "achieving",
            "won",
            "promoted",
            "praised",
            "win",
            "kudos",
            "shoutout",
            "great feedback",
            "recognized",
            "出荷した",
            "リリースした",
            "達成した",
            "褒められた",
            "배포했어",
            "출시했어",
            "달성했어",
            "칭찬받았어",
            "发布了",
            "上线了",
            "完成了",
            "表扬",
            "认可",
        ],
    },
    {
        "name": "ARCHITECTURE",
        "message": "Consider creating a reference note or a decision record for the architecture discussion.",
        "patterns": [
            "architecture",
            "system design",
            "rfc",
            "tech spec",
            "trade-off",
            "design doc",
            "adr",
            "アーキテクチャ",
            "システム設計",
            "아키텍처",
            "시스템 설계",
            "架构",
            "系统设计",
            "技术规范",
        ],
    },
    {
        "name": "PERSON CONTEXT",
        "message": "Consider updating the relevant person note in org/people/ and linking it from the work note.",
        "patterns": [
            "told me",
            "said that",
            "feedback from",
            "met with",
            "talked to",
            "spoke with",
            "mentioned that",
            "mentioned the",
            "mentioned a",
            "言ってた",
            "フィードバック",
            "話した",
            "말했어",
            "피드백",
            "얘기했어",
            "언급했어",
            "说了",
            "提到",
            "反馈",
            "提及",
        ],
    },
    {
        "name": "PROJECT UPDATE",
        "message": "Consider updating the active work note and checking whether the result belongs in the brag doc.",
        "patterns": [
            "project update",
            "sprint",
            "milestone",
            "shipped",
            "shipping",
            "ships",
            "shipped feature",
            "launched",
            "launching",
            "launches",
            "completed",
            "completing",
            "completes",
            "released",
            "releasing",
            "releases",
            "deployed",
            "deploying",
            "deploys",
            "went live",
            "rolled out",
            "rolling out",
            "merged",
            "merging",
            "merges",
            "cut the release",
            "release cut",
            "スプリント",
            "マイルストーン",
            "マージした",
            "リリースしました",
            "스프린트",
            "마일스톤",
            "배포",
            "릴리스",
            "병합",
            "迭代",
            "里程碑",
            "上线",
            "合并了",
        ],
    },
]


def any_word_match(pattern_words: list[str], text: str) -> bool:
    for phrase in pattern_words:
        if re.search(r"(?<![a-zA-Z])" + re.escape(phrase) + r"(?![a-zA-Z])", text):
            return True
    return False


def classify(prompt: str) -> list[dict[str, str]]:
    lowered = prompt.lower()
    matches = []
    for signal in SIGNALS:
        if any_word_match(signal["patterns"], lowered):
            matches.append({"name": signal["name"], "message": signal["message"]})
    return matches


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Classify freeform work input and print Obsidian Mind routing hints."
    )
    parser.add_argument("text", nargs="*", help="Text to classify. If omitted, stdin is used.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = " ".join(args.text).strip()
    if not text:
        text = sys.stdin.read().strip()

    if not text:
        print("No input provided.", file=sys.stderr)
        return 1

    matches = classify(text)

    if args.json:
        print(json.dumps({"matches": matches}, ensure_ascii=False, indent=2))
        return 0

    if not matches:
        print("No strong routing signals detected.")
        return 0

    print("Routing hints:")
    for match in matches:
        print(f"- {match['name']}: {match['message']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
