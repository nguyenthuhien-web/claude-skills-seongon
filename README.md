# Claude Code Skills - SEONGON

Workspace Claude Code cho Content SEO, gồm 3 skills + 2 sub-agents.

## Cấu trúc

### Skills (`.claude/skills/`)
1. **swot-analyzer** — Phân tích SWOT đối thủ
2. **outline-generator** — Tạo outline bài SEO
3. **trending-topic-finder** — Tìm trending topics

### Sub-Agents (`.claude/agents/`)
1. **serp-research-agent** — Nghiên cứu SERP, phân tích đối thủ
   - Skills: competitor-content-analyzer, content-gap-finder
2. **content-seo-agent** — Viết bài SEO chuẩn E-E-A-T
   - Skills: keyword-research, content-writer

## Cách chạy

```bash
# Chạy serp-research-agent
bash .claude/agents/serp-research-agent/run.sh "keyword"

# Chạy content-seo-agent  
bash .claude/agents/content-seo-agent/skills/keyword-research/run.sh "keyword"
```

## Outputs
Tất cả output được lưu vào folder `outputs/`
