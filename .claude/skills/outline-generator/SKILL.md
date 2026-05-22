---
name: outline-generator
description: "Tạo dàn ý bài viết SEO hoàn chỉnh: nhận vào từ khóa và thông tin dự án, phân tích Search Intent, chọn concept phù hợp và tạo outline chuẩn SEO kèm checklist tự kiểm tra"
user-invokable: true
author: SEONGON
version: "1.0.0"
hooks:
  run: true
  trigger: "/outline-generator"
arguments:
  - name: keyword
    type: string
    required: true
    description: "Từ khóa hoặc cụm từ cần tạo outline"
  - name: intent
    type: string
    required: false
    description: "Search Intent (informational, transactional, commercial, navigational) - tự phân tích nếu không chỉ định"
  - name: concept
    type: string
    required: false
    description: "Concept type (listicle, howto, comparison, review, guide) - tự gợi ý nếu không chỉ định"
metadata:
  category: seo-content
  dependencies: []
  tags: [outline-generation, seo-content, search-intent, content-strategy]
---

# outline-generator

Skill tạo dàn ý bài viết SEO tự động.
Nhận vào từ khóa, tự phân tích Search Intent (SI), chọn concept phù hợp
và tạo outline hoàn chỉnh kèm checklist chất lượng.

**Tiết kiệm thời gian:** Từ khóa → Dàn ý chuẩn SEO trong 5 phút, không cần brainstorm.

---

## How to Use

**Cú pháp:** `/outline-generator <từ_khóa> [--intent <loại>] [--concept <dạng>]`

**Arguments:**
- `<từ_khóa>` (bắt buộc): Từ khóa hoặc cụm từ cần tạo outline
- `--intent` (tùy chọn): Chỉ định Search Intent (informational, transactional, commercial, navigational)
  - Nếu không chỉ định: Skill sẽ tự phân tích từ khóa
- `--concept` (tùy chọn): Chỉ định concept (listicle, howto, comparison, review, guide)
  - Nếu không chỉ định: Skill sẽ gợi ý concept phù hợp nhất

**Ví dụ sử dụng:**
```
/outline-generator "máy lọc không khí tốt nhất"
/outline-generator "mua điều hòa inverter" --intent transactional
/outline-generator "tủ lạnh sharp vs samsung" --concept comparison
/outline-generator "cách chọn máy giặt" --intent informational --concept howto
/outline-generator "Samsung tủ lạnh" --intent navigational
```

**Output trả về:**
- Tệp markdown chứa dàn ý hoàn chỉnh
- Lưu vào thư mục `outputs/`
- Tên file: `outline-[từ-khóa-slug]-[YYYY-MM-DD].md`
- Ví dụ: `outline-may-loc-khong-khi-2026-05-18.md`

---

## Step-by-step Process

### Bước 1: Parse Input Arguments
- Tách `<từ_khóa>` từ argument đầu tiên
- Tách `--intent` nếu có (mặc định: null, sẽ phân tích sau)
- Tách `--concept` nếu có (mặc định: null, sẽ gợi ý sau)
- Validate: từ khóa không được trống, intent/concept phải hợp lệ

**Ví dụ:**
```
Input: /outline-generator "máy lọc không khí tốt nhất" --intent commercial
→ keyword = "máy lọc không khí tốt nhất"
→ intent = "commercial"
→ concept = null (chưa chỉ định)
```

---

### Bước 2: Tải & Phân Tích Search Intent Rules
- Đọc file `rules/search-intent-rules.md`
- Ghi nhớ:
  - 4 loại SI: Informational, Transactional, Navigational, Commercial
  - Dấu hiệu nhận biết từng loại (từ khóa đặc trưng, cấu trúc câu, ví dụ)
  - Content type phù hợp cho mỗi SI
  - Quick reference: Từ khóa indicator (cách, là gì, mua, vs, so sánh, etc.)

---

### Bước 3: Xác Định Search Intent
- **Nếu `--intent` đã chỉ định:** Dùng intent đó, bỏ qua bước này
- **Nếu `--intent` chưa chỉ định:** Phân tích từ khóa dựa vào dấu hiệu:

| Dấu Hiệu | SI Kết Luận |
|----------|------------|
| Có "cách", "làm sao", "là gì" | 🔍 Informational |
| Có "mua", "giá", "khuyến mãi" | 🛒 Transactional |
| Chứa brand/website cụ thể | 🏢 Navigational |
| Có "vs", "so sánh", "review", "tốt nhất" | 💭 Commercial |

**Ví dụ:**
```
Từ khóa: "máy lọc không khí tốt nhất"
→ Dấu hiệu: "tốt nhất" → Commercial SI
→ Content type: So sánh, Review, Best list
```

---

### Bước 4: Tải & Phân Tích Concept Types Rules
- Đọc file `rules/concept-types.md`
- Ghi nhớ:
  - 5 concept: Listicle, How-to, Comparison, Review, Ultimate Guide
  - Đặc điểm mỗi concept (độ dài, cấu trúc, khi nào dùng)
  - Bảng quyết định: SI + Concept Phù Hợp
  - Cấu trúc outline mẫu cho mỗi concept

---

### Bước 5: Chọn Concept Phù Hợp
- **Nếu `--concept` đã chỉ định:** Dùng concept đó
- **Nếu `--concept` chưa chỉ định:** Gợi ý dựa vào SI + từ khóa:

| SI | Từ Khóa | Concept Gợi Ý |
|----|---------|----|
| Informational | "cách...", "là gì" | How-to, Ultimate Guide |
| Transactional | "mua", "giá", "khuyến mãi" | Listicle, Review |
| Commercial | "so sánh", "tốt nhất", "review" | Comparison, Listicle, Review |
| Navigational | "brand", "website" | (Không phù hợp cho bài editorial) |

**Ví dụ:**
```
SI: Commercial
Từ khóa: "máy lọc không khí tốt nhất"
→ Concept: Listicle (Top 10) hoặc Comparison
→ Gợi ý: "Nên dùng Listicle vì có từ 'tốt nhất' và high-intent"
```

---

### Bước 6: Tải File Ví Dụ Mẫu
- Dựa vào SI chọn file ví dụ:
  - **SI = Informational:** Load `examples/informational-outline.md`
  - **SI = Transactional:** Load `examples/transactional-outline.md`
  - **SI = Commercial:** Load `examples/transactional-outline.md` (tương tự Transactional)
  - **SI = Navigational:** Gợi ý đặc biệt (thường không lên outline bài editorial)

- Ghi nhớ cấu trúc template mẫu:
  - H1 + Intro
  - H2s (4-8 tùy concept) + H3s
  - Bảng so sánh (nếu cần)
  - FAQ (nếu Informational)
  - Conclusion + CTA

---

### Bước 7: Tạo Dàn Ý Hoàn Chỉnh
- Tạo H1 với từ khóa chính (ví dụ: "Top 10 Máy Lọc Không Khí Tốt Nhất 2026")
- Tạo phần Intro (100-200 từ): Hook + Vấn đề + Lợi ích
- Tạo H2s (4-8 mục tùy concept):
  - Listicle: #1, #2, ..., #5-10
  - How-to: Bước 1, 2, 3...
  - Comparison: Sản phẩm A, Sản phẩm B, So sánh
  - Review: Specs, Ưu điểm, Nhược điểm, Rating
  - Ultimate Guide: Topic 1, 2, 3, ... FAQ, Conclusion
- Tạo H3 bên dưới mỗi H2 (ít nhất 1 H3/H2)
- Thêm bảng so sánh (nếu cần)
- Thêm FAQ (nếu SI = Informational)
- Tạo phần Conclusion + CTA (100-150 từ)
- Ghi chú về từ khóa phụ, schema, internal links

---

### Bước 8: Tải & Tự Chấm Điểm Outline
- Đọc file `rules/outline-checklist.md`
- Chạy checklist trên outline vừa tạo:
  - ✅ Cơ bản: H1, H2, H3, Intro, Conclusion, CTA, Độ dài
  - ✅ SEO: Từ khóa chính/phụ, FAQ (nếu Informational), Schema
  - ✅ EEAT: Dẫn chứng, Source, Kinh nghiệm
  - ✅ Brand Voice: Tone, Không từ cấm, CTA align
- Tính điểm: (✅) / (Total) × 100
  - 90-100%: ✅ Duyệt ngay
  - 80-89%: ⚠️ Chỉnh sửa nhỏ
  - Dưới 80%: ❌ Cần sửa lại

**Nếu điểm < 80%:**
- Chỉ rõ điểm yếu
- Gợi ý cách sửa
- **Không lưu file, hỏi lại user muốn sửa điểm nào**

---

### Bước 9: Lưu Output & Hoàn Tất
- Tạo folder `outputs/` nếu chưa có
- Tên file: `outline-[từ-khóa-slug]-[YYYY-MM-DD].md`
  - Ví dụ: `outline-may-loc-khong-khi-2026-05-18.md`
  - Slug: Chuyển từ khóa thành lowercase, thay space bằng dấu gạch ngang, bỏ ký tự đặc biệt
- Lưu file với nội dung:
  1. Header: Từ khóa, SI, Concept, Độ dài dự kiến, Điểm checklist
  2. Dàn ý H1/H2/H3 đầy đủ
  3. Ghi chú cho writer (từ khóa phụ, schema, internal link)
  4. Kết quả checklist (%) + Ghi chú sửa chữa (nếu có)
- Report đường dẫn file cho user

---

## Supporting Files

Ba file hỗ trợ nằm trong skill folder. **Chỉ load khi đến bước cần, không load tất cả cùng lúc:**

1. **rules/search-intent-rules.md**
   - Load: Ở Bước 2
   - Dùng để: Phân tích Search Intent (4 loại, dấu hiệu, ví dụ)
   - Chứa: Định nghĩa 4 loại SI, dấu hiệu, content type, bảng quyết định

2. **rules/concept-types.md**
   - Load: Ở Bước 4
   - Dùng để: Chọn concept + cấu trúc outline mẫu
   - Chứa: 5 concept, khi nào dùng, cấu trúc H1/H2/H3, bảng quyết định

3. **rules/outline-checklist.md**
   - Load: Ở Bước 8
   - Dùng để: Tự kiểm tra outline, chấm điểm (checklist 30+ items)
   - Chứa: Checklist cơ bản, SEO, EEAT, Brand voice, thang điểm

4. **examples/informational-outline.md**
   - Load: Ở Bước 6 nếu SI = Informational
   - Dùng để: Template mẫu cho bài Informational/Comparison
   - Chứa: Metadata, dàn ý mẫu, ghi chú cho writer

5. **examples/transactional-outline.md**
   - Load: Ở Bước 6 nếu SI = Transactional hoặc Commercial
   - Dùng để: Template mẫu cho bài Transactional/Listicle
   - Chứa: Metadata, dàn ý mẫu, ghi chú cho writer (focus CTA, giá)

---

## Quality Checklist

Trước khi trả kết quả, tự kiểm tra theo danh sách:

- [ ] **SI được xác định đúng** - Đã phân tích từ khóa hoặc sử dụng intent chỉ định?
- [ ] **Concept phù hợp với SI** - Dựa vào bảng quyết định, concept có match SI không?
- [ ] **H1 chứa từ khóa chính** - H1 có từ khóa chính không, ở vị trí tốt không?
- [ ] **Có ít nhất 4 H2** - Đủ số lượng H2 cho outline hoàn chỉnh?
- [ ] **Mỗi H2 có ít nhất 1 H3** - Tất cả H2 đều có sub-section H3?
- [ ] **Có phần mở bài & kết bài** - Intro (100-200 từ) và Conclusion (100-150 từ) có rõ ràng?
- [ ] **Có ít nhất 1 CTA** - Bài viết có hành động gợi ý cuối cùng không?
- [ ] **Điểm checklist ≥ 80%** - Outline đạt ít nhất 80% trên 30+ tiêu chí?
- [ ] **File output lưu thành công** - File có nằm trong `outputs/` không?

**Nếu fail bất cứ checkpoint nào:**
- ❌ Không lưu file
- ❌ Report điểm yếu cho user
- ❌ Gợi ý cách sửa (ví dụ: "Thêm H3 vào H2 #2", "Viết lại intro cho rõ ràng")
- ❌ Hỏi user muốn sửa hay tạo lại

---

## Common Errors

| Lỗi | Nguyên Nhân | Cách Khắc Phục |
|-----|-----------|-----------------|
| Từ khóa quá ngắn (1-2 từ) | Thiếu context để phân tích SI chính xác | Hỏi: "Ngành gì? Mục tiêu bài là gì? (bán, giáo dục, so sánh)" |
| SI không rõ ràng | Từ khóa có thể thuộc nhiều loại | Ưu tiên Commercial nếu có "tốt nhất", "nên mua", "giá rẻ" |
| Concept không phù hợp | Chọn sai dựa vào SI | Kiểm tra lại bảng quyết định ở rules/concept-types.md |
| Outline quá ngắn (< 4 H2) | Từ khóa quá hẹp hoặc concept sai | Mở rộng thêm angle, hoặc chuyển concept (ví dụ: How-to → Ultimate Guide) |
| Outline quá dài (> 8 H2) | Scope quá lớn, khó viết | Cắt giảm xuống 4-6 H2 chính, cái còn lại lên bài khác |
| Không có H3 bên dưới H2 | Quên check cấu trúc | Thêm H3 cho mỗi H2 (ít nhất 1 cái) |
| Checklist < 80% | Outline chưa hoàn thiện | Đưa danh sách điểm yếu, hỏi user sửa hay tạo lại |
| File example không load | Sai đường dẫn hoặc file bị xóa | Kiểm tra `/examples/` có đủ 2 files (informational + transactional) không |
| Từ khóa phụ không được nhắc | Quên phân tích từ khóa phụ | Thêm mục "Từ Khóa Phụ" vào ghi chú cho writer |

---

## Output Format

### Tên File
```
outputs/outline-[từ-khóa-slug]-[YYYY-MM-DD].md
```

**Ví dụ:**
```
outputs/outline-may-loc-khong-khi-tham-khao-2026-05-18.md
outputs/outline-mua-tu-lanh-side-by-side-gia-tot-2026-05-18.md
outputs/outline-iphone-16-review-2026-05-18.md
```

---

### Cấu Trúc File Output

**1. HEADER (50-100 từ)**
```markdown
# [Tiêu Đề H1]

**Thông Tin Bài Viết:**
- Từ khóa chính: [Từ khóa]
- Search Intent: [SI icon + tên]
- Concept: [Concept]
- Độ dài dự kiến: [X]-[Y] từ
- Mục tiêu: [Mục tiêu bài]
- Điểm Checklist: [%]

---
```

**2. DÀN Ý H1/H2/H3 (250-400 từ)**
```markdown
# [H1 Tiêu Đề Chính]

[Intro - 100-200 từ]

## H2 #1: [Tên]
### H3 #1.1: [Tên]
### H3 #1.2: [Tên]

## H2 #2: [Tên]
...

[Bảng so sánh nếu cần]

[FAQ nếu SI = Informational]

## Kết Luận
[Conclusion - 100-150 từ]

---
```

**3. GHI CHÚ CHO WRITER (50-150 từ)**
```markdown
## Ghi Chú Cho Writer

### Từ Khóa Phụ Cần Nhắc
- [Keyword 1]
- [Keyword 2]
...

### Schema Markup
- Type: [Schema type]

### Internal Linking
- Link to: [Related post]

### Tips Thêm
- [Tip 1]
- [Tip 2]
```

**4. KẾT QUẢ CHECKLIST (30-50 từ)**
```markdown
## Kết Quả Checklist

**Điểm tổng hợp:** [%]
**Status:** ✅ Duyệt / ⚠️ Chỉnh sửa / ❌ Cần sửa

Điểm yếu (nếu có):
- [Điểm yếu 1] → Cách sửa: [...]
- [Điểm yếu 2] → Cách sửa: [...]
```

---

### Độ Dài Dự Kiến

- **Header:** 50-100 từ
- **Dàn ý:** 250-400 từ
- **Ghi chú:** 50-150 từ
- **Checklist:** 30-50 từ
- **TOTAL:** 380-700 từ (phù hợp để review nhanh)

---

## Tips & Best Practices

✅ **Làm tốt:**
- Load file cần khi nào dùng, không load tất cả cùng lúc (tiết kiệm context)
- Phân tích SI cẩn thận dựa vào dấu hiệu từ khóa cụ thể
- Chọn concept phù hợp nhất (dùng bảng quyết định)
- Chấm điểm outline trước khi lưu (phải ≥ 80%)
- Ghi chú rõ ràng cho writer (từ khóa phụ, schema, internal link)
- Luôn tạo slug sạch (lowercase, dấu gạch ngang, không ký tự đặc biệt)

❌ **Tránh:**
- Load tất cả files cùng lúc (lãng phí context window)
- Phân tích SI chủ quan, không dùng dấu hiệu từ khóa
- Chọn concept random, không dùng bảng quyết định
- Lưu file mà không chấm điểm (outline có thể chưa hoàn thiện)
- Tạo outline 3-4 H2 (quá ít), hoặc 10+ H2 (quá nhiều)
- Quên ghi chú để writer biết cần phải làm gì

---

## Version History

| Phiên Bản | Ngày | Thay Đổi |
|-----------|------|---------|
| 1.0.0 | 2026-05-18 | Phiên bản đầu tiên |

---

**Tạo bởi:** SEONGON  
**Thể loại:** SEO Content Strategy

