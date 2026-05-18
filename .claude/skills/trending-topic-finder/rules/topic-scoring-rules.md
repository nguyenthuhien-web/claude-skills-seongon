# Tiêu Chí Chấm Điểm & Phân Loại Trending Topics

Tài liệu này định nghĩa cách tính điểm trending, phân loại chủ đề, 
và lọc chất lượng để chọn những topic đáng viết bài.

---

## 1. THANG ĐIỂM TRENDING (0-100)

Mỗi trending topic sẽ được chấm điểm từ 0-100 dựa trên 3 yếu tố:

### 1.1. Điểm Tăng Trưởng (Growth Score) - 40%

Đo lường mức độ tăng tìm kiếm so với giai đoạn trước đó.

**Công thức tính:**
```
growth_percent = ((current_volume - previous_volume) / previous_volume) * 100

Nếu growth_percent >= 500%  → score = 100
Nếu growth_percent >= 300%  → score = 85
Nếu growth_percent >= 150%  → score = 70
Nếu growth_percent >= 50%   → score = 55
Nếu growth_percent >= 0%    → score = 40
Nếu growth_percent < 0%     → score = 20 (đang giảm)
```

**Ví dụ:**
- Topic "iPhone 16" từ 1000 → 5500 searches = +450% = Score 85
- Topic "Sale mùa hè" từ 500 → 750 searches = +50% = Score 55

### 1.2. Điểm Khối Lượng (Volume Score) - 35%

Đo lường tổng lượng tìm kiếm hiện tại. Topic có volume cao hơn 
có tiềm năng traffic lớn hơn.

**Công thức tính:**
```
Lấy đỉnh (peak) lượng tìm kiếm của topic trong khoảng thời gian phân tích

Nếu peak >= 100  → score = 100 (very high volume)
Nếu peak >= 80   → score = 85
Nếu peak >= 60   → score = 70
Nếu peak >= 40   → score = 55
Nếu peak >= 20   → score = 40
Nếu peak < 20    → score = 20 (niche topic)
```

**Ví dụ:**
- "Điện máy Xanh khuyến mãi" peak = 95 → Score 85
- "Bảo hành điện thoại Samsung" peak = 25 → Score 40

### 1.3. Điểm Bền Vững (Sustainability Score) - 25%

Đo lường liệu trend này sẽ tồn tại bao lâu (ngắn hạn vs dài hạn).

**Công thức tính:**
```
Phân tích trend line trong 7-30 ngày:

Nếu tăng liên tục, ổn định   → score = 90 (dài hạn)
Nếu peak rồi giảm từ từ       → score = 70 (mid-term, 2-3 tuần)
Nếu peak rồi giảm nhanh       → score = 50 (short-term, 3-5 ngày)
Nếu spike tức thời, rơi vê 0  → score = 30 (very short, <2 ngày)
```

**Ví dụ:**
- Trend "AI công cụ mới" tăng ổn định trong 3 tuần → Score 90
- Trend "Nổi tiếng vì 1 bài biffed viral" spike rồi rơi → Score 30

### 1.4. Công Thức Tính Điểm Tổng

```
TOTAL SCORE = (Growth Score × 0.40) + (Volume Score × 0.35) + (Sustainability Score × 0.25)

Làm tròn đến số nguyên gần nhất
```

**Ví dụ tính toán:**
- Topic "Điện máy Black Friday"
  - Growth Score = 85
  - Volume Score = 80
  - Sustainability Score = 60
  - **Total = (85 × 0.40) + (80 × 0.35) + (60 × 0.25) = 34 + 28 + 15 = 77**

---

## 2. PHÂN LOẠI 4 NHÓM

Dựa vào Total Score, phân loại topic vào 4 nhóm với hành động khác nhau:

### 2.1 🔥 HOT NGAY (Score ≥ 80)

**Đặc điểm:**
- Trending mạnh, tăng trưởng cao, volume lớn
- Xu hướng bền vững hoặc còn đang tăng
- Cơ hội traffic rất lớn

**Hành động:**
- ✅ **ƯU TIÊN HÀNG ĐẦU** — Viết bài **trong 24-48 giờ**
- Chuẩn bị outline + research từ khóa ngay lập tức
- Viết bài nhanh, đảm bảo chất lượng cơ bản
- Publish ngay khi ready (không chờ quá lâu)
- Tối ưu SEO để rank nhanh nhất

**Ghi chú:**
- Những topic này sẽ hết "hot" rất nhanh
- Nếu chờ >48h, có thể miss cơ hội

### 2.2 📈 ĐANG LÊN (Score 60-79)

**Đặc điểm:**
- Trending vừa phải, tăng trưởng ổn định
- Volume khá, còn có thời gian để trend tăng thêm
- Cơ hội traffic tốt, nhưng không jeopardy

**Hành động:**
- ✅ **CÓ PRIORITY** — Viết bài **trong tuần này (3-5 ngày)**
- Lên outline chi tiết và research keyword hôm nay
- Viết bài trong vòng 2-3 ngày
- Publish cuối tuần hoặc đầu tuần sau
- Có thể tối ưu hơn vì còn thời gian

**Ghi chú:**
- Trend này còn sức sống 1-2 tuần nữa
- Nên publish trong tuần để còn bắt kịp peak

### 2.3 👀 THEO DÕI (Score 40-59)

**Đặc điểm:**
- Trending yếu hoặc ngành niche
- Volume tạm được, nhưng tăng trưởng không mạnh
- Cơ hội traffic vừa phải

**Hành động:**
- 📋 **LÊN KẾ HOẠCH TUẦN SAU**
- Thêm vào wishlist content để track tiếp
- Viết bài **tuần sau nếu trend tiếp tục tăng**
- Nếu trend giảm, bỏ qua

**Ghi chú:**
- Trend này có thể tăng tốc nên cần theo dõi
- Nếu xuống dưới 40 tuần tới → bỏ qua
- Nếu tăng lên trên 80 tuần tới → chuyển sang "Hot ngay"

### 2.4 ❄️ BỎ QUA (Score < 40)

**Đặc điểm:**
- Trending yếu hoặc niche quá nhỏ
- Tăng trưởng thấp, volume ít
- ROI viết bài sẽ thấp

**Hành động:**
- ❌ **BỎ QUA** — Không viết bài
- Không xếp vào roadmap
- Có thể giữ lại ý tưởng cho future evergreen content

**Ghi chú:**
- Những topic này không đáng đầu tư thời gian
- Chỉ xem xét nếu topic liên quan trực tiếp đến sản phẩm lõi

---

## 3. TIÊU CHÍ LỌC CHẤT LƯỢNG

Ngoài điểm số, cần áp dụng các tiêu chí lọc để loại bỏ topic không tốt:

### 3.1 Loại Bỏ: Trend Không Liên Quan Ngành

**Rule:**
- ❌ Nếu topic hoàn toàn ngoài ngành kinh doanh của brand
- ❌ Nếu không thể liên hệ hoặc tie-in được với sản phẩm

**Ví dụ loại bỏ (với brand "Điện máy Chợ Lớn"):**
- "Sao nhập học" → Không liên quan
- "Bóng đá World Cup 2026" → Không liên quan (trừ khi viết về promotional "xem World Cup trên TV mình bán")

**Ví dụ giữ lại:**
- "iPhone 16 giá rẻ" → Có thể liên hệ (brand bán điện thoại)
- "Smart home technology" → Liên quan trực tiếp (brand bán smart devices)

### 3.2 Loại Bỏ: Trend Mùa Vụ Lặp Lại Hàng Năm

**Rule:**
- ❌ Nếu trend này lặp lại vào cùng thời gian hàng năm (VD: Black Friday, 8/3, Tết)
- ⚠️ **NHƯNG:** Nếu trend này lần đầu xuất hiện → có thể xem xét
- ⚠️ **NHƯNG:** Nếu bạn chưa viết bài cho trend này năm trước → có thể viết

**Ví dụ loại bỏ (nếu đã từng viết):**
- "Black Friday Sale" lần thứ 3 → bỏ
- "Valentine gift ideas" lần thứ 2 → bỏ

**Ví dụ giữ lại:**
- "Black Friday Sale 2026" lần đầu tiên → viết (update SEO từ năm trước)
- Trend "Cyber Monday" nếu lần đầu xuất hiện ở VN → viết

**Ghi chú:**
- Những trend tái diễn này tốt cho evergreen content, không cần phải nhanh
- Nên chuẩn bị từ trước (tháng 8 cho Black Friday tháng 11)

### 3.3 Ưu Tiên: Trend Có Commercial Intent

**Rule:**
- ✅ Ưu tiên những trend có khả năng chuyển đổi sale cao
- ✅ Trend liên quan đến mua hàng, so sánh sản phẩm, review

**Ví dụ ưu tiên (với brand Điện máy):**
- "Mua tủ lạnh Samsung giá rẻ" → **PRIORITY** (intention rõ ràng → mua)
- "Cách chọn máy giặt tốt" → **PRIORITY** (intention sắp mua)
- "Tủ lạnh nào tốt nhất" → **PRIORITY** (so sánh → sắp mua)

**Ví dụ ít priority:**
- "Lịch sử phát triển tủ lạnh" → Informational, không bán hàng
- "Vật lý đằng sau tủ lạnh" → Educational, không bán hàng

### 3.4 Ưu Tiên: Trend Phù Hợp Với Brand Voice

**Rule:**
- ✅ Ưu tiên trend phù hợp tone, style, positioning của brand
- ❌ Bỏ qua trend nếu tone/style không match

**Ví dụ (brand Điện máy Chợ Lớn):**
- "Điện máy giá sốc" → Phù hợp (brand nổi tiếng giá rẻ)
- "Điện máy hàng hiếm luxury" → Không phù hợp (brand không fancy)

**Ví dụ (brand Flagship Store cao cấp):**
- "Điện máy hàng hiếm luxury" → Phù hợp
- "Điện máy giá rẻ" → Không phù hợp (conflict với positioning)

---

## 📋 CHECKLIST CHỌN TOPIC

Trước khi xác định topic trending có đáng viết hay không, 
hãy check lại theo thứ tự này:

1. **Tính điểm:** Topic có score bao nhiêu? (reference phần 1)
2. **Phân loại:** Rơi vào nhóm nào? (reference phần 2)
3. **Liên quan ngành:** Có liên hệ được với brand không?
4. **Mùa vụ:** Có phải trend mùa vụ lặp lại không? (nếu có, check xem đã viết rồi chưa)
5. **Commercial intent:** Có khả năng chuyển đổi sale không?
6. **Brand voice:** Phù hợp với tone/style của brand không?

**Quyết định:**
- Nếu pass hết 6 tiêu chí → **✅ VIẾT BÀI**
- Nếu fail ≥2 tiêu chí → **❌ BỎ QUA**
- Nếu uncertain → Trao đổi với team

---

## 🎯 Ví Dụ Case Study

### Case 1: iPhone 16 Pre-order

| Tiêu chí | Đánh giá |
|----------|---------|
| Growth Score | 95 (tăng 600%) |
| Volume Score | 92 (peak = 98) |
| Sustainability Score | 70 (tăng ổn định 3 tuần) |
| **Total Score** | **86 (Hot ngay)** |
| Liên quan ngành | ✅ (bán điện thoại) |
| Mùa vụ | ✅ (product launch mới, không lặp) |
| Commercial intent | ✅ (people want to buy) |
| Brand voice | ✅ (match) |
| **Quyết định** | **🔥 VIẾT NGAY trong 24-48h** |

### Case 2: Tết mua sắm (lần thứ 3)

| Tiêu chí | Đánh giá |
|----------|---------|
| Growth Score | 85 (trend mùa vụ) |
| Volume Score | 88 (peak = 95) |
| Sustainability Score | 40 (peak rồi giảm) |
| **Total Score** | **72 (Đang lên)** |
| Liên quan ngành | ✅ |
| Mùa vụ | ⚠️ (lặp lại, đã viết năm trước) |
| Commercial intent | ✅ |
| Brand voice | ✅ |
| **Quyết định** | **📋 KHỈ TRACK, có thể update bài cũ thay vì viết mới** |

### Case 3: "Cách tiết kiệm điện năng"

| Tiêu chí | Đánh giá |
|----------|---------|
| Growth Score | 55 (tăng 40%) |
| Volume Score | 48 (peak = 42) |
| Sustainability Score | 75 (evergreen, search hàng ngày) |
| **Total Score** | **59 (Theo dõi)** |
| Liên quan ngành | ✅ |
| Mùa vụ | ✅ (evergreen) |
| Commercial intent | ⚠️ (educational, không trực tiếp sale) |
| Brand voice | ✅ |
| **Quyết định** | **👀 THEO DÕI, lên roadmap evergreen content** |

---

## 📌 Ghi Chú Chung

- Điểm số **không phải tiêu chí duy nhất** — cần xem cả 6 tiêu chí lọc
- Một topic score 95 nhưng không liên quan ngành → vẫn bỏ
- Một topic score 50 nhưng có commercial intent cao + brand match → vẫn viết
- Revisit trending list **hàng tuần** để update tiến độ và status

---

**Phiên bản:** 1.0  
**Ngày cập nhật:** 2026-05-18
