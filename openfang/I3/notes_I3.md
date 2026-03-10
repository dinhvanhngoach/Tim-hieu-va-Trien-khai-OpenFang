# Notes I3 — Ví dụ dùng OpenFang chạy Agent "Researcher"

---

## 1. Mục tiêu

Tạo một agent nghiên cứu tự động để:
- Tìm thông tin trên internet
- Kiểm tra nguồn
- Viết báo cáo có trích dẫn
- Gửi kết quả về dashboard hoặc channel

> Trong OpenFang, agent dạng này thường dùng **Researcher Hand**.

---

## 2. Các bước thực hiện

**Bước 1 — Cài OpenFang:**
```bash
curl -fsSL https://openfang.sh/install | sh
```
Hệ thống agent được cài thành 1 binary chạy độc lập (~32MB).

**Bước 2 — Khởi động hệ thống:**
```bash
openfang start
```
Lệnh này chạy: kernel agent, memory database, API server, dashboard quản lý.

**Bước 3 — Kích hoạt Researcher Hand:**
```bash
openfang hand activate researcher
```
Sau khi kích hoạt: hệ thống tạo autonomous agent, agent chạy theo lịch, agent có thể gọi tool (search, summarize...).

---

## 3. Workflow của Agent Researcher

```
Search information
      ↓
Collect sources
      ↓
Fact-check sources
      ↓
Summarize results
      ↓
Generate report
```

Agent sẽ:
1. Tìm dữ liệu từ web
2. Thu thập nguồn
3. Kiểm tra độ tin cậy (CRAAP evaluation)
4. Viết báo cáo có citation

---

## 4. Cấu trúc Agent

Một agent trong OpenFang thường gồm: `HAND.toml`, system prompt, skills, tools, metrics.

Ví dụ cấu hình:
```toml
name = "research-agent"
schedule = "0 */4 * * *"
tools = [
  "web_search",
  "summarize",
  "citation"
]
```

> Agent chạy mỗi 4 giờ, dùng tool search và summarize, tạo report tự động.

---

## 5. Kết quả sau khi chạy

- Thông tin được lưu vào memory (SQLite + vector)
- Báo cáo hiển thị trên dashboard
- Có thể gửi sang Telegram / Slack / Discord
- OpenFang hỗ trợ 40+ channel integration

---

## 6. Ý tưởng sử dụng thực tế

Researcher agent có thể dùng cho:
- Nghiên cứu thị trường
- Theo dõi đối thủ
- Viết báo cáo ngành
- Thu thập tin tức

**Ví dụ thực tế:**
> Theo dõi tin AI mỗi ngày → agent search → tóm tắt → gửi báo cáo Telegram

---
*Ghi chú bởi: I3 | Ngày 1 — Thứ Hai*
