---
name: competitor-content-analyzer
description: Phân tích nội dung top 10 kết quả Google cho 1 keyword
arguments:
  - name: keyword
    required: true
  - name: market
    default: VN
---
# Skill: Competitor Content Analyzer
## Các bước
1. Liệt kê top 10 URL đang rank
2. Phân tích từng URL: title, H1, cấu trúc heading, word count, format, CTA
3. Tổng hợp pattern chung
4. Xác định winning format
## Output
Lưu file: serp-analysis-[keyword]-[date].md
- Bảng top 10: URL / Title / Format / Word count
- Pattern chung
- Winning format đề xuất
