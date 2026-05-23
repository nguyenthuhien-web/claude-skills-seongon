#!/bin/bash
KEYWORD=$1
MARKET=${2:-VN}
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="outputs/serp-analysis-${KEYWORD// /-}-${DATE}.md"

claude -p "
Đọc file .claude/agents/serp-research-agent/skills/competitor-content-analyzer/SKILL.md
Thực hiện đúng theo hướng dẫn cho keyword: $KEYWORD, market: $MARKET
Lưu kết quả vào file: $OUTPUT_FILE
" --allowedTools "Read,Write,Bash"
