# Claude SEO Workspace

## Thứ tự chạy agents (quan trọng)
1. serp-research-agent   ← LUÔN chạy đầu tiên
2. content-seo-agent     ← Viết bài dựa trên SERP research
3. kyThuat-seo-agent     ← Tối ưu bài sau khi viết xong

## Agent Registry
| Agent | Vai trò | Chạy khi |
|-------|---------|----------|
| serp-research-agent | Phân tích top 10, tìm content gap | Trước khi viết bài |
| content-seo-agent | Keyword research + viết bài | Sau khi có SERP data |
| kyThuat-seo-agent | Audit + on-page optimize | Sau khi có bài draft |

## Skills Registry
| Skill | Agent |
|-------|-------|
| competitor-content-analyzer | serp-research-agent |
| content-gap-finder | serp-research-agent |
| keyword-research | content-seo-agent |
| content-writer | content-seo-agent |
| technical-audit | kyThuat-seo-agent |
| on-page-optimizer | kyThuat-seo-agent |

## Orchestration Rule
Khi nhận task lớn:
1. Đọc CLAUDE.md
2. Chạy theo thứ tự: serp → content → kỹ thuật
3. Mỗi agent PHẢI đọc AGENT.md và SKILL.md trước khi thực hiện
4. Lưu tất cả output vào outputs/
