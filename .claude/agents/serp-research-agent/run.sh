#!/bin/bash
# Agent: serp-research-agent
KEYWORD=$1

echo "🔍 serp-research-agent starting for keyword: $KEYWORD"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo "▶ Triggering skill: competitor-content-analyzer"
bash .claude/agents/serp-research-agent/skills/competitor-content-analyzer/run.sh "$KEYWORD"

echo "▶ Triggering skill: content-gap-finder"
bash .claude/agents/serp-research-agent/skills/content-gap-finder/run.sh "$KEYWORD"

echo "✅ serp-research-agent completed"
