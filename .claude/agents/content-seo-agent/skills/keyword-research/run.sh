#!/bin/bash
TOPIC=$1
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="outputs/keyword-research-${TOPIC// /-}-${DATE}.md"

claude -p "
Đọc file .claude/agents/content-seo-agent/skills/keyword-research/SKILL.md
Thực hiện cho topic: $TOPIC
Lưu kết quả vào: $OUTPUT_FILE
"
