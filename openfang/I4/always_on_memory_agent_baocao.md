# Báo cáo tìm hiểu: Always-On Memory Agent

> **Nguồn:** https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/agents/always-on-memory-agent  
> **Ngày báo cáo:** 17/03/2026

---

## 1. Tổng quan

**Always-On Memory Agent** là một AI memory agent chạy nền 24/7, được xây dựng bằng **Google ADK** (Agent Development Kit) kết hợp **Gemini Flash-Lite**.

> **Ý tưởng cốt lõi:** Hầu hết AI agent bị "mất trí nhớ" — xử lý thông tin khi được hỏi rồi quên hết. Project này cho agent một bộ nhớ liên tục, tự tiến hóa, chạy liên tục để xử lý, hợp nhất và kết nối thông tin — giống như não người trong lúc ngủ.

**Triết lý kỹ thuật:** Không dùng vector database, không dùng embeddings. Chỉ dùng LLM để đọc, suy nghĩ và ghi structured memory.

---

## 2. Vấn đề cần giải quyết

Các phương pháp memory hiện tại đều có giới hạn:

| Phương pháp | Giới hạn |
|---|---|
| Vector DB + RAG | Thụ động — embed một lần, truy xuất sau, không xử lý chủ động |
| Conversation summary | Mất chi tiết theo thời gian, không cross-reference |
| Knowledge graph | Đắt để xây dựng và duy trì |

**Điểm thiếu:** Không có hệ thống nào chủ động hợp nhất thông tin như não người. Con người không chỉ lưu trữ ký ức — não phát lại, kết nối và nén thông tin trong lúc ngủ. Agent này làm đúng điều đó.

---

## 3. Kiến trúc — 3 Agent chuyên biệt

Một **Orchestrator** điều phối toàn bộ, định tuyến request đến đúng agent chuyên biệt. Mỗi agent có công cụ riêng để đọc/ghi memory store.

### 3.1 IngestAgent — Nhập dữ liệu

Nhận bất kỳ file nào và dùng Gemini multimodal để trích xuất thông tin có cấu trúc:

```
Input: "Anthropic reports 62% of Claude usage is code-related."
           │
           ▼
   ┌──────────────────────────────────┐
   │ Summary:  Anthropic reports...  │
   │ Entities: [Anthropic, Claude]   │
   │ Topics:   [AI, code generation] │
   │ Importance: 0.8                 │
   └──────────────────────────────────┘
```

**Hỗ trợ 27 loại file:**

| Loại | Định dạng |
|---|---|
| Text | `.txt`, `.md`, `.json`, `.csv`, `.log`, `.xml`, `.yaml`, `.yml` |
| Ảnh | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`, `.svg` |
| Audio | `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.aac` |
| Video | `.mp4`, `.webm`, `.mov`, `.avi`, `.mkv` |
| Document | `.pdf` |

**3 cách nạp dữ liệu:**
- **File watcher** — thả file vào thư mục `./inbox`, agent tự xử lý trong 5-10 giây
- **Dashboard upload** — dùng nút Upload trên giao diện Streamlit
- **HTTP API** — gửi `POST /ingest` với nội dung text

### 3.2 ConsolidateAgent — Hợp nhất ký ức

Chạy theo timer (mặc định: **mỗi 30 phút**). Giống não người trong lúc ngủ, nó:
- Xem lại các ký ức chưa được hợp nhất
- Tìm kết nối giữa các ký ức
- Tạo ra cross-cutting insights
- Nén các thông tin liên quan

```
Memory #1: "AI agents are growing fast but reliability is a challenge"
Memory #2: "Q1 priority: reduce inference costs by 40%"
Memory #3: "Current LLM memory approaches all have gaps"
                   │
                   ▼  ConsolidateAgent
   ┌───────────────────────────────────────────┐
   │ Insight: "The bottleneck for next-gen AI  │
   │  tools is the transition from static RAG  │
   │  to dynamic memory systems"               │
   └───────────────────────────────────────────┘
```

### 3.3 QueryAgent — Truy vấn

Nhận câu hỏi, đọc toàn bộ memories và consolidation insights, tổng hợp câu trả lời kèm **source citations**:

```
Q: "What should I focus on?"

A: "Based on your memories, prioritize:
   1. Ship the API by March 15 [Memory 2]
   2. The agent reliability gap [Memory 1] could be addressed
      by the reconstructive memory approach [Memory 3]"
```

---

## 4. Cấu trúc file trong repo

```
always-on-memory-agent/
├── agent.py          # Logic chính: IngestAgent, ConsolidateAgent, QueryAgent
├── dashboard.py      # Giao diện Streamlit (localhost:8501)
├── requirements.txt  # Dependencies Python
├── docs/             # Ảnh kiến trúc, banner
└── LICENSE
```

---

## 5. Hướng dẫn cài đặt nhanh

### Yêu cầu
- Python 3.x
- Google Gemini API key (lấy miễn phí tại [aistudio.google.com](https://aistudio.google.com))

### Các bước cài đặt

```bash
# Bước 1 — Clone repo
git clone https://github.com/GoogleCloudPlatform/generative-ai.git
cd generative-ai/gemini/agents/always-on-memory-agent

# Bước 2 — Cài dependencies
pip install -r requirements.txt

# Bước 3 — Set API key
export GOOGLE_API_KEY="your-gemini-api-key"
# Windows PowerShell:
# $env:GOOGLE_API_KEY = "your-gemini-api-key"

# Bước 4 — Chạy agent
python agent.py
```

Sau khi chạy, agent sẽ:
- Theo dõi thư mục `./inbox/` để nhận file mới
- Consolidate mỗi 30 phút
- Phục vụ queries tại `http://localhost:8888`

### Nạp dữ liệu

```bash
# Thả file vào inbox
echo "Thông tin quan trọng" > inbox/notes.txt
cp photo.jpg inbox/
cp report.pdf inbox/

# Hoặc qua API
curl -X POST http://localhost:8888/ingest \
  -H "Content-Type: application/json" \
  -d '{"text": "Nội dung cần nhớ", "source": "manual"}'
```

### Truy vấn

```bash
curl "http://localhost:8888/query?q=what+do+you+know"
```

### Mở Dashboard (tuỳ chọn)

```bash
streamlit run dashboard.py
# Truy cập: http://localhost:8501
```

---

## 6. Điểm mạnh nổi bật

- **Không cần vector DB** — đơn giản hơn nhiều so với RAG truyền thống
- **Multimodal** — hiểu được text, ảnh, audio, video, PDF trong cùng một pipeline
- **Chạy nền 24/7** — không cần người dùng kích hoạt, tự động consolidate
- **Source citations** — mọi câu trả lời đều có trích dẫn nguồn memory cụ thể
- **Lightweight** — dùng Gemini Flash-Lite, chi phí thấp

---

## 7. Tóm tắt nhanh

| Hạng mục | Thông tin |
|---|---|
| Nền tảng | Google ADK + Python |
| AI Model | Gemini Flash-Lite |
| Chạy nền | 24/7 |
| Số loại file hỗ trợ | 27 |
| Consolidate timer | Mỗi 30 phút |
| Dashboard | Streamlit (localhost:8501) |
| API | REST (localhost:8888) |
| API key cần | Google Gemini (miễn phí) |
| Cần vector DB không | ❌ Không |

---

*Báo cáo được tổng hợp ngày 17/03/2026*
