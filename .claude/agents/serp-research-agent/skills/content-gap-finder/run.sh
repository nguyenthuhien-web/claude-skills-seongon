#!/bin/bash
KEYWORD=$1
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="outputs/content-gap-${KEYWORD// /-}-${DATE}.md"

claude -p "
Đọc file .claude/agents/serp-research-agent/skills/content-gap-finder/SKILL.md
Thực hiện đúng theo hướng dẫn cho keyword: $KEYWORD
Lưu kết quả vào file: $OUTPUT_FILE
" --allowedTools "Read,Write,Bash"
