---
name: swot-analyzer
description: "Phân tích SWOT cho dự án content SEO: nhận vào tên brand và tên đối thủ, trả về bảng SWOT đầy đủ, bảng so sánh cạnh tranh, positioning statement và gợi ý ưu tiên content"
user-invokable: true
argument-hint: "<brand_name> vs <competitor_1> [competitor_2]"
license: MIT
compatibility: "Free: no external API required"
metadata:
  author: SEONGON
  version: "1.0.0"
  category: seo-content
---

# swot-analyzer

Skill phân tích SWOT chuyên dụng cho dự án content SEO.
Nhận vào tên brand và 1-2 đối thủ cạnh tranh, trả về
phân tích SWOT đầy đủ kèm gợi ý chiến lược content.

## How to Use

Cú pháp: `/swot-analyzer <brand> vs <competitor1> [competitor2]`

**Ví dụ:**
```
/swot-analyzer "Điện Máy Chợ Lớn" vs "Điện Máy Xanh"
/swot-analyzer "Điện Máy Chợ Lớn" vs "Điện Máy Xanh" vs "MediaMart"
/swot-analyzer TechBlog vs DevForum vs CodeNews
```

**Input yêu cầu:**
- Brand chính (tên project/công ty muốn phân tích)
- 1 hoặc 2 đối thủ cạnh tranh
- Dấu ngăn cách: `vs` (có thể có hoặc không có khoảng trắng)

**Output trả về:**
- Tệp markdown chứa phân tích SWOT đầy đủ
- Lưu vào thư mục `outputs/`
- Tên file: `swot-[brand-name]-[YYYY-MM-DD].md`

---

## Step-by-step Process

### Bước 1: Parse input argument
- Tách tên brand chính (phần đầu tiên)
- Tách tên từng đối thủ (phần sau `vs`)
- Validate: brand không được trống, ít nhất 1 đối thủ

### Bước 2: Load rules/competitor-signals.md
- Đọc file quy tắc để biết các dấu hiệu cần phân tích
- Ghi nhớ 5 nhóm tín hiệu:
  1. Tín hiệu từ Website (tốc độ, UX, cấu trúc)
  2. Tín hiệu từ Nội dung (chất lượng, tần suất, EEAT)
  3. Tín hiệu từ SEO (DA, backlink, từ khóa rank)
  4. Tín hiệu từ Social (engagement, tần suất, sentiment)
  5. Tín hiệu từ Review (Google Maps, Facebook)

### Bước 3: Phân tích brand chính
- Tìm kiếm thông tin về brand
- Kiểm tra từng dấu hiệu trong 5 nhóm
- Xác định điểm mạnh của brand
- Ghi lại từng điểm, gán label [SEO]/[Nội dung]/[Brand]/[Giá]/[UX]

### Bước 4: Phân tích từng đối thủ
- Tìm kiếm thông tin về mỗi đối thủ
- Kiểm tra các dấu hiệu tương tự
- Xác định điểm mạnh của từng đối thủ
- Ghi lại đầy đủ để so sánh

### Bước 5: Xác định SWOT tổng hợp
**Strengths (Điểm mạnh):** 
- Những gì brand làm tốt hơn đối thủ
- Hoặc những điểm brand có mà đối thủ không

**Weaknesses (Điểm yếu):**
- Những gì brand làm tệ hơn đối thủ
- Hoặc những điểm brand thiếu mà đối thủ có

**Opportunities (Cơ hội):**
- Xu hướng, keyword, format nội dung mà chưa ai khai thác
- Gap trong content của đối thủ
- Nhu cầu thị trường chưa được đáp ứng

**Threats (Thách thức):**
- Nước đi của đối thủ có thể ảnh hưởng
- Xu hướng/thuật toán không thuận lợi
- Rủi ro về thị trường, quy định

### Bước 6: Load templates/swot-template.md
- Đọc file template để lấy cấu trúc output
- Chuẩn bị điền thông tin

### Bước 7: Điền thông tin vào template
- Thay tất cả placeholder [MẪU] bằng dữ liệu thực tế
- Bảng SWOT 4 ô với labels
- Bảng so sánh 6 tiêu chí
- Positioning statement đầy đủ

### Bước 8: Viết 6 gợi ý chủ đề content
**3 chủ đề khai thác điểm mạnh:**
- Chủ đề mà brand có lợi thế
- Giúp xây dựng leadership, authority
- Mục tiêu: rank top, tăng traffic, brand awareness

**3 chủ đề phản bác điểm yếu:**
- Chủ đề giải quyết vấn đề yếu của brand
- Giúp cải thiện vị trí trên thị trường
- Mục tiêu: catch-up, tăng conversion, community

Mỗi chủ đề gồm:
- Tên chủ đề
- Loại content (guide, case study, comparison, v.v.)
- Target keyword cụ thể
- Mục tiêu của bài viết

### Bước 9: Lưu output
- Tạo folder `outputs/` nếu chưa có
- Tên file: `swot-[brand-slug]-[YYYY-MM-DD].md`
- Ví dụ: `swot-dien-may-cho-lon-2026-05-18.md`
- In ra đường dẫn file để user dễ tìm

---

## Supporting Files

Hai file hỗ trợ nằm trong skill folder:

1. **rules/competitor-signals.md**
   - Load: Ở Bước 2
   - Dùng để: Biết cần kiểm tra dấu hiệu nào khi phân tích
   - Chứa: 5 nhóm tín hiệu, mỗi nhóm 5-7 dấu hiệu

2. **templates/swot-template.md**
   - Load: Ở Bước 6
   - Dùng để: Lấy cấu trúc template output
   - Chứa: Bảng SWOT, bảng so sánh, positioning statement, gợi ý content

---

## Quality Checklist

Trước khi trả kết quả, tự kiểm tra theo danh sách:

- [ ] **SWOT Strengths**: Có ít nhất 5 điểm mạnh cụ thể, mỗi điểm có label
- [ ] **SWOT Weaknesses**: Có ít nhất 5 điểm yếu cụ thể, mỗi điểm có label
- [ ] **SWOT Opportunities**: Có ít nhất 5 cơ hội rõ ràng
- [ ] **SWOT Threats**: Có ít nhất 5 thách thức rõ ràng
- [ ] **Bảng so sánh**: Đủ 6 tiêu chí (DA, chất lượng nội dung, tốc độ website, social presence, từ khóa rank, backlink)
- [ ] **Bảng so sánh**: Dữ liệu cụ thể, có con số hoặc đánh giá rõ ràng
- [ ] **Positioning Statement**: Có đủ 5 thành phần (target + nhu cầu + brand + lợi ích + điểm khác biệt)
- [ ] **Gợi ý content**: Đúng 6 chủ đề (3 khai thác mạnh + 3 phản bác yếu)
- [ ] **Gợi ý content**: Mỗi chủ đề có loại content, keyword, mục tiêu cụ thể
- [ ] **Output file**: Được lưu vào `outputs/` với tên đúng format
- [ ] **Tổng thể**: Không có placeholder [MẪU] còn lại chưa thay thế

---

## Common Errors

| Lỗi | Nguyên nhân | Cách khắc phục |
|-----|-----------|-----------------|
| Không tìm thấy thông tin brand/đối thủ | Tên viết sai, brand quá mới, không có online presence | Hỏi user tên chính xác hoặc website/social media của brand |
| SWOT quá chung chung | Thiếu thông tin cụ thể về ngành, thị trường | Yêu cầu user cung cấp thêm: ngành gì, sản phẩm gì, thị trường mục tiêu |
| Không load được file rules/template | Đường dẫn file sai, file chưa tồn tại | Kiểm tra path: `.claude/skills/swot-analyzer/rules/competitor-signals.md` |
| Positioning statement thiếu ý | Chưa có đủ thông tin về USP, value proposition | Yêu cầu user giải thích: lợi ích chính, điểm khác biệt so với đối thủ |
| Gợi ý content thiếu keyword | Chỉ viết chủ đề, chưa research keyword | Research thêm từ khóa có search volume, phù hợp với chủ đề |
| Output không lưu được | Folder `outputs/` chưa tồn tại | Tạo folder `outputs/` ở cùng cấp với `.claude` |
| Đối thủ không đủ thông tin | Brand nhỏ, ít có thông tin công khai | Phân tích với dữ liệu có sẵn, ghi chú: "dữ liệu hạn chế" |
| File output quá ngắn/dài | Phân tích thiếu hoặc thêm quá nhiều chi tiết | Duy trì 400-600 từ, tập trung vào điểm cốt lõi |

---

## Output Format

### Tên file
```
outputs/swot-[brand-slug]-[YYYY-MM-DD].md
```

Ví dụ:
```
outputs/swot-dien-may-cho-lon-2026-05-18.md
outputs/swot-techblog-2026-05-18.md
outputs/swot-brand-viet-2026-05-18.md
```

### Cấu trúc file output

1. **Header** (50-100 từ)
   - Tên brand chính, ngày phân tích
   - Danh sách đối thủ so sánh
   - Thị trường/lĩnh vực

2. **Bảng SWOT 4 ô** (200-250 từ)
   - Strengths: 5 điểm + label
   - Weaknesses: 5 điểm + label
   - Opportunities: 5 điểm
   - Threats: 5 điểm

3. **Bảng so sánh cạnh tranh** (100-150 từ)
   - 6 tiêu chí × (Brand + Đối thủ 1 + [Đối thủ 2])
   - Nhận xét ngắn về vùng dẫn đầu, lùi lạc, cơ hội

4. **Positioning Statement** (50-80 từ)
   - Đầy đủ 5 thành phần theo format chuẩn

5. **Gợi ý 6 chủ đề content** (250-300 từ)
   - 3 chủ đề khai thác điểm mạnh
   - 3 chủ đề phản bác điểm yếu
   - Mỗi chủ đề: loại content + keyword + mục tiêu

### Độ dài dự kiến
- **Tối thiểu**: 400 từ
- **Tối ưu**: 500-600 từ
- **Tối đa**: 700 từ (nếu nhiều chi tiết cần thiết)

### Định dạng markdown
- Tiêu đề H1: # [Tiêu đề chính]
- Tiêu đề H2: ## [Tiêu đề chính]
- Tiêu đề H3: ### [Tiêu đề phụ]
- Bảng: Markdown table format
- Danh sách: Bullet points (-)
- Nhấn mạnh: **bold** cho keyword quan trọng

---

## Tips & Best Practices

✅ **Làm tốt:**
- Tìm kiếm thông tin từ website, Google Search, SEO tools
- So sánh kỹ lưỡng từng dấu hiệu
- Ghi rõ label [SEO]/[Nội dung]/[Brand] cho từng điểm
- Gợi ý content phải hợp lý, có thể thực hiện được
- Lưu file output để user dễ tìm

❌ **Tránh:**
- Phân tích chung chung, không cụ thể
- Xây dựng SWOT mà không dùng dấu hiệu từ competitor-signals.md
- Gợi ý content quá rộng hoặc quá hẹp
- Quên kiểm tra quality checklist trước khi trả kết quả
- Để placeholder [MẪU] trong output cuối cùng

---

## Version History

| Phiên bản | Ngày | Thay đổi |
|-----------|------|---------|
| 1.0.0 | 2026-05-18 | Phiên bản đầu tiên |

---

**Tạo bởi:** SEONGON  
**License:** MIT  
**Thể loại:** SEO Content Strategy
