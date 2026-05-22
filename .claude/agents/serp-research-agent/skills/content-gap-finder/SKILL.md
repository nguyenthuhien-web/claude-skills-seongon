---
name: content-gap-finder
description: Tìm khoảng trống nội dung mà top 10 chưa khai thác
arguments:
  - name: keyword
    required: true
  - name: serp_analysis_file
    required: false
---
# Skill: Content Gap Finder
## Các bước
1. Đọc file serp-analysis nếu có
2. Liệt kê PAA questions chưa được trả lời đầy đủ
3. Tìm subtopic top 10 bỏ sót
4. Tìm góc độ local VN mà bài tiếng Anh không có
5. Đề xuất unique angle
## Output
Lưu file: content-gap-[keyword]-[date].md
- PAA chưa được trả lời
- Subtopics bị bỏ sót
- Góc độ local VN
- Unique angle đề xuất
