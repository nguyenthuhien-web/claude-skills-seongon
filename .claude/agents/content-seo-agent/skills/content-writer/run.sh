#!/bin/bash
KEYWORD=$1
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="outputs/content-${KEYWORD// /-}-${DATE}.md"

claude -p "
Đọc file .claude/agents/content-seo-agent/skills/content-writer/SKILL.md
Viết bài SEO cho keyword: $KEYWORD
Lưu kết quả vào: $OUTPUT_FILE
"
