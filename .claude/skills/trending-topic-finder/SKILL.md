---
name: trending-topic-finder
description: "Tìm kiếm và phân tích các chủ đề đang trending trên Google Trends theo ngành, trả về báo cáo phân loại và kế hoạch content ưu tiên"
user-invokable: true
argument-hint: "<ngành/từ_khóa> [--country VN] [--days 7]"
license: MIT
compatibility: "Free: requires pytrends library (pip install pytrends)"
metadata:
  author: SEONGON
  version: "1.0.0"
  category: seo-content
---

# trending-topic-finder

Skill tìm chủ đề trending cho content SEO.
Kết nối Google Trends qua CLI Python (pytrends).
Nhận vào ngành/từ khóa, trả về báo cáo trending
kèm kế hoạch content ưu tiên theo tuần.

---

## How to Use

**Cú pháp:** `/trending-topic-finder <ngành> [--country VN] [--days 7]`

**Ví dụ:**
```
/trending-topic-finder "điện máy"
/trending-topic-finder "điện máy" --days 30
/trending-topic-finder "điện máy" --country VN --days 7
/trending-topic-finder "công nghệ AI" --country US --days 14
```

**Input yêu cầu:**
- `<ngành>`: Ngành hoặc từ khóa cần tìm trending (bắt buộc)
- `--country`: Mã quốc gia (mặc định: VN). VD: VN, US, JP, etc.
- `--days`: Số ngày lấy dữ liệu (mặc định: 7). Tối đa: 90 ngày

**Output trả về:**
- Tệp markdown chứa báo cáo trending đầy đủ
- Lưu vào thư mục `outputs/`
- Tên file: `trending-[ngành-slug]-[YYYY-MM-DD].md`

---

## Step-by-step Process

### Bước 1: Parse input argument
- Tách tên ngành/từ khóa từ argument đầu tiên
- Tách country (mặc định: VN)
- Tách days (mặc định: 7)
- Validate: ngành không được trống, country có hiệu lực, days > 0

### Bước 2: Load rules/topic-scoring-rules.md
- Đọc file quy tắc chấm điểm
- Ghi nhớ 3 thành phần điểm:
  - **Growth Score (40%):** % tăng so với tuần trước
  - **Volume Score (35%):** Peak search volume hiện tại
  - **Sustainability Score (25%):** Trend dài hạn hay ngắn hạn
- Ghi nhớ 4 nhóm phân loại:
  - 🔥 **Hot ngay** (≥80): Viết trong 24-48h
  - 📈 **Đang lên** (60-79): Viết trong tuần
  - 👀 **Theo dõi** (40-59): Lên kế hoạch tuần sau
  - ❄️ **Bỏ qua** (<40): Không viết

### Bước 3: Cài đặt pytrends
- Kiểm tra xem thư viện `pytrends` đã cài chưa
- Nếu chưa, chạy: `pip install pytrends`
- Nếu cài không thành công → report lỗi

### Bước 4: Chạy script lấy dữ liệu
- Chạy lệnh CLI:
  ```bash
  python .claude/skills/trending-topic-finder/scripts/get-trends.py "<ngành>" --country <country> --days <days>
  ```
- Script sẽ:
  - Kết nối Google Trends qua pytrends
  - Lấy `interest_over_time`, `related_topics`, `related_queries`
  - Xử lý lỗi 429 bằng `time.sleep(2)`
  - In kết quả ra stdout
- Đợi script hoàn tất, collect dữ liệu output

### Bước 5: Đọc & phân tích kết quả
- Từ output của script, trích xuất:
  - Interest over time: first value, last value, peak, average
  - Related topics: rising topics + growth %
  - Related queries: rising queries + growth %
- Chuẩn bị dữ liệu để chấm điểm

### Bước 6: Chấm điểm từng topic
- Với mỗi topic:
  - Tính **Growth Score** dựa trên % tăng
  - Tính **Volume Score** dựa trên peak volume
  - Tính **Sustainability Score** dựa trên trend line
  - Tính **Total Score**: (Growth × 0.40) + (Volume × 0.35) + (Sustainability × 0.25)
- Sắp xếp topics theo Total Score giảm dần

### Bước 7: Phân loại topics vào 4 nhóm
- Dựa vào Total Score:
  - Score ≥80 → 🔥 **Hot ngay**
  - Score 60-79 → 📈 **Đang lên**
  - Score 40-59 → 👀 **Theo dõi**
  - Score <40 → ❄️ **Bỏ qua**
- Áp dụng 4 tiêu chí lọc chất lượng:
  1. Loại bỏ topic không liên quan ngành
  2. Loại bỏ topic mùa vụ lặp lại (nếu đã viết)
  3. Ưu tiên topic có commercial intent
  4. Ưu tiên topic phù hợp brand voice

### Bước 8: Load template & điền dữ liệu
- Đọc file `templates/trending-report-template.md`
- Điền thông tin vào template:
  1. **Header:** Ngành, thời gian, quốc gia, tổng topics
  2. **Bảng tổng hợp:** Tất cả topics sắp xếp theo điểm
  3. **Chi tiết Top 5:** Mỗi topic gồm 3 góc viết, từ khóa, deadline
  4. **Kế hoạch content:** Tuần này, tuần sau, theo dõi
- Thay tất cả placeholder [MẪU] bằng dữ liệu thực tế

### Bước 9: Lưu output & hoàn tất
- Tạo folder `outputs/` nếu chưa có
- Tên file: `trending-[ngành-slug]-[YYYY-MM-DD].md`
- Ví dụ: `trending-dien-may-2026-05-18.md`
- Lưu file, report đường dẫn cho user

---

## Supporting Files

Ba file hỗ trợ nằm trong skill folder:

1. **rules/topic-scoring-rules.md**
   - Load: Ở Bước 2
   - Dùng để: Biết cách chấm điểm (công thức, thang điểm, tiêu chí lọc)
   - Chứa: 3 phần (thang điểm, phân loại 4 nhóm, tiêu chí lọc)

2. **scripts/get-trends.py**
   - Chạy: Ở Bước 4
   - Dùng để: Lấy dữ liệu từ Google Trends via pytrends
   - Chứa: Hàm parse args, fetch data, xử lý lỗi 429, print results

3. **templates/trending-report-template.md**
   - Load: Ở Bước 8
   - Dùng để: Lấy cấu trúc template output
   - Chứa: 4 phần (header, bảng tổng hợp, chi tiết top 5, kế hoạch content)

---

## Quality Checklist

Trước khi trả kết quả, tự kiểm tra theo danh sách:

- [ ] **Script chạy thành công**: get-trends.py không có lỗi, lấy được dữ liệu
- [ ] **Có ít nhất 5 topics**: Báo cáo chứa tối thiểu 5 topics trending
- [ ] **Mỗi topic có điểm**: Tất cả topics có Total Score (0-100)
- [ ] **Phân loại đúng nhóm**: Topics được phân vào đúng 4 nhóm theo thang điểm
- [ ] **Top 5 đầy đủ**: Mỗi topic top 5 có đủ 3 góc viết, từ khóa, deadline
- [ ] **Góc viết cụ thể**: 3 góc viết mỗi topic có tên bài cụ thể, không generic
- [ ] **Từ khóa target**: Mỗi topic có 5+ từ khóa với search volume
- [ ] **Kế hoạch rõ ràng**: Báo cáo phân tuần (tuần này vs tuần sau) rõ ràng
- [ ] **Không placeholder**: Không còn [MẪU], [NGÀNH], [ĐIỂM] chưa thay
- [ ] **File lưu đúng**: Output file nằm trong `outputs/` với tên đúng format
- [ ] **Độ dài hợp lý**: Báo cáo từ 500-800 từ (không quá dài/ngắn)
- [ ] **Không lỗi format**: Markdown format đúng, bảng hiển thị bình thường

---

## Common Errors

| Lỗi | Nguyên nhân | Cách khắc phục |
|-----|-----------|-----------------|
| ModuleNotFoundError: No module named 'pytrends' | Chưa cài thư viện pytrends | Chạy: `pip install pytrends` |
| 429 Too Many Requests | Gọi API Google Trends quá nhiều lần | Script tự xử lý bằng `time.sleep(2)`, nếu vẫn lỗi → thử lại sau 1 phút |
| HTTPError: 429 | Rate limit từ Google | Giảm số lần gọi API hoặc chờ trước khi retry |
| Không có dữ liệu trending | Từ khóa quá hẹp hoặc không phổ biến | Thử từ khóa rộng hơn hoặc tăng `--days` lên 30 |
| Kết quả output trống | Từ khóa không có trending data ở VN | Thử không ghi `--country` để lấy global data, hoặc thử ngành khác |
| Script không chạy được | Đường dẫn tuyệt đối sai | Kiểm tra path: `./.claude/skills/trending-topic-finder/scripts/get-trends.py` |
| File output quá dài | Quá nhiều topics hoặc chi tiết | Cắt giảm chi tiết, focus top 5-10 topics |
| Điểm số không hợp lý | Tính toán Growth/Volume/Sustainability sai | Kiểm tra lại công thức trong topic-scoring-rules.md |

---

## Output Format

### Tên file
```
outputs/trending-[ngành-slug]-[YYYY-MM-DD].md
```

Ví dụ:
```
outputs/trending-dien-may-2026-05-18.md
outputs/trending-ai-tools-2026-05-18.md
outputs/trending-ecommerce-2026-05-18.md
```

### Cấu trúc file output

1. **Header** (50-100 từ)
   - Ngành/từ khóa phân tích
   - Khoảng thời gian (ngày bắt đầu - kết thúc)
   - Quốc gia
   - Tổng số topics tìm được
   - Ngày report

2. **Bảng Tổng Hợp Topics** (7 cột)
   - STT, Chủ đề, Điểm, Nhóm, Mức Tăng, Gợi Ý Hành Động
   - Sắp xếp theo Điểm giảm dần
   - Highlight 🔥 **Hot ngay**
   - Tóm tắt số lượng theo 4 nhóm

3. **Chi Tiết Top 5 Topics** (300-400 từ)
   - Tên chủ đề + Điểm + Nhóm
   - Deadline nên đăng bài
   - Lý do trending (2-3 điểm)
   - Search volume & trend line
   - 3 góc viết bài cụ thể (How-to, So sánh, News)
   - 5+ từ khóa liên quan (kèm search volume)
   - Gợi ý thêm (2-3 points)

4. **Kế Hoạch Content** (150-200 từ)
   - **Tuần này**: Topics viết ngay (🔥 Hot ngay)
   - **Tuần sau**: Topics chuẩn bị (📈 Đang lên)
   - **Theo dõi**: Topics cần check lại (👀 Theo dõi)
   - Mỗi item có: tên topic, angle, deadline, priority, owner

### Độ dài dự kiến
- **Tối thiểu:** 500 từ
- **Tối ưu:** 600-800 từ
- **Tối đa:** 1000 từ

### Định dạng markdown
- Tiêu đề H1: `# [Tiêu đề chính]`
- Tiêu đề H2: `## [Tiêu đề phụ]`
- Bảng: Markdown table format
- Danh sách: Bullet points (-)
- Nhấn mạnh: **bold** cho keywords quan trọng
- Emoji: 📊, 🔥, 📈, 👀, ❄️, ✍️, 🔑, etc.

---

## Tips & Best Practices

✅ **Làm tốt:**
- Chạy script get-trends.py đầu tiên để có dữ liệu chính xác
- Áp dụng đúng công thức chấm điểm từ topic-scoring-rules.md
- Phân loại topics cẩn thận, không bỏ sót tiêu chí lọc
- Viết 3 góc viết bài rõ ràng, có tên bài cụ thể
- Lên kế hoạch content phân tuần rõ ràng
- Lưu file output ngay lập tức

❌ **Tránh:**
- Chấm điểm chủ quan, không dùng công thức
- Bỏ qua 4 tiêu chí lọc chất lượng
- Liệt kê nhiều topics nhưng chi tiết không đủ (chỉ có top 5 thôi)
- Góc viết generic ("So sánh", "Hướng dẫn") mà không có tên bài cụ thể
- Quên check Quality Checklist trước khi trả kết quả
- Để placeholder [MẪU] trong output cuối cùng
- Viết báo cáo chỉ dựa vào output của script mà không phân tích thêm

---

## Version History

| Phiên bản | Ngày | Thay đổi |
|-----------|------|---------|
| 1.0.0 | 2026-05-18 | Phiên bản đầu tiên |

---

**Tạo bởi:** SEONGON  
**License:** MIT  
**Thể loại:** SEO Content Strategy  
**Dependencies:** pytrends, pandas, argparse, time, datetime
