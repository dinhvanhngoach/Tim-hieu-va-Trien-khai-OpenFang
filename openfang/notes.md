# OpenFang – Notes Day 1

## 1. OpenFang là gì? Dùng để làm gì

OpenFang là một **AI Agent Operating System mã nguồn mở** được xây dựng bằng **Rust**.  
Hệ thống cho phép các nhà phát triển tạo ra **AI Agent tự động** có khả năng thực hiện các nhiệm vụ mà không cần con người giám sát liên tục.

OpenFang cung cấp các agent tích hợp sẵn gọi là **Hands** như:

- Researcher
- Browser

Các agent này có thể:

- Thu thập dữ liệu
- Phân tích thông tin
- Tự động hóa quy trình làm việc

OpenFang được sử dụng để:

- Xây dựng hệ thống **AI Automation**
- Tạo các **AI Agent tự động**
- Triển khai AI trong các ứng dụng thực tế

---

# 2. Vẽ sơ đồ kiến trúc OpenFang. Agent, Tool, Memory là gì

Các thành phần chính trong OpenFang:



## Agent (Hand)

Agent là **đơn vị thực thi tự động** trong hệ thống.

Agent hoạt động theo vòng lặp:

Agent được **Kernel của OpenFang tạo và quản lý**.

Lifecycle của Agent:

- Running
- Suspended
- Terminated


## Tool / Skills

Tool là các chức năng mà agent có thể gọi để thực hiện hành động.

Ví dụ:

- web_search
- web_fetch
- file_read
- shell_exec

OpenFang hiện có **53+ built-in tools**.

Các tool chạy trong **WASM sandbox** để đảm bảo:

- cách ly
- bảo mật
- an toàn hệ thống


## Memory

Memory là hệ thống lưu trữ thông tin của agent.

Bao gồm:

- SQLite (lưu dữ liệu)
- Vector Embeddings (tìm kiếm semantic)
- Knowledge Graph

Memory giúp agent:

- ghi nhớ thông tin
- duy trì ngữ cảnh
- sử dụng dữ liệu giữa các lần chạy

---

# 3. Tìm và đọc thêm 1 ví dụ dùng OpenFang trên GitHub hoặc docs — ghi tóm tắt lại

---
# 4. Ghi chú về Agent trong OpenFang

### Agent trong OpenFang là gì?

Agent trong OpenFang là một thực thể AI tự động, hoạt động như một "nhân viên số" có thể thực hiện nhiệm vụ thay người dùng mà không cần con người ngồi theo dõi liên tục. Khác với chatbot thông thường (chỉ phản hồi khi bạn hỏi), agent trong OpenFang có thể tự chủ động làm việc theo lịch, xử lý thông tin, gọi tool, và báo cáo kết quả về dashboard.

Ví dụ thực tế: Một agent có thể được giao nhiệm vụ "mỗi sáng tìm kiếm tin tức AI mới nhất và tóm tắt lại" — nó sẽ tự chạy lúc 8 giờ sáng mà không cần bạn ra lệnh.

### Cách tạo Agent trong OpenFang

Có 2 cách tạo agent:

**Cách 1 — Qua Dashboard (dễ nhất):**
1. Mở trình duyệt → vào http://127.0.0.1:4200
2. Nhấn "+ New Agent" ở góc trên bên phải
3. Chọn template có sẵn (General Assistant, Code Helper, Researcher, Writer...)
4. Đặt tên, mô tả nhiệm vụ, chọn model LLM
5. Nhấn Create → agent sẵn sàng hoạt động

**Cách 2 — Qua CLI:**
```bash
openfang chat   # Chat trực tiếp với agent mặc định
```

### Agent dùng để làm gì?

OpenFang cung cấp 30 pre-built agent chia thành 4 nhóm:

| Nhóm | Ví dụ Agent | Tác dụng |
|------|------------|----------|
| TỔNG QUAN | General Assistant | Trợ lý đa năng hàng ngày |
| PHÁT TRIỂN | Code Helper, DevOps Engineer | Viết code, debug, CI/CD |
| NGHIÊN CỨU | Researcher | Tìm kiếm, tổng hợp thông tin |
| VIẾT | Writer, Meeting Notes | Soạn thảo nội dung |

### Các thành phần cốt lõi của Agent

```
Agent = LLM (não) + Tools (tay) + Memory (trí nhớ) + Skills (kỹ năng)
```

- **LLM**: "Não" của agent — xử lý ngôn ngữ, ra quyết định (Groq/Llama, Gemini, v.v.)
- **Tools**: Công cụ agent dùng để thực thi (web search, đọc file, chạy code, v.v.) — OpenFang có 53 tools sẵn có
- **Memory**: Bộ nhớ lưu context giữa các cuộc hội thoại — dùng SQLite + vector embeddings
- **Skills**: Kỹ năng chuyên biệt — OpenFang có 60 bundled skills

### Điểm đặc biệt: "Hands" (Tay)

OpenFang có khái niệm đặc biệt là **Hands** — khác với agent thông thường chờ bạn hỏi, Hands tự chạy theo lịch và báo cáo kết quả. OpenFang có 7 Hands:

- **Clip**: Chuyển video dài thành clip ngắn
- **Lead**: Tự động tìm kiếm khách hàng tiềm năng
- **Collector**: Thu thập thông tin OSINT
- **Predictor**: Dự đoán và theo dõi độ chính xác
- **Researcher**: Nghiên cứu và kiểm chứng thông tin
- **Twitter**: Quản lý mạng xã hội
- **Browser**: Tự động hóa trình duyệt

### Bảo mật của Agent

OpenFang có 16 lớp bảo mật, đáng chú ý:
- Tool code chạy trong **WebAssembly sandbox** — bị cô lập, không thể làm hỏng hệ thống
- **Taint tracking**: Theo dõi luồng dữ liệu nhạy cảm từ nguồn đến đích
- **RBAC**: Agent chỉ được dùng tool đã được cấp phép
- **Merkle audit trail**: Mọi hành động được ghi lại và không thể giả mạo

### Ví dụ tìm thấy trên GitHub/Docs

Trên GitHub của OpenFang (github.com/RightNow-AI/openfang/tree/main/agents), có nhiều ví dụ agent sẵn có:
- `assistant/` — Agent trợ lý cơ bản
- `coder/` — Agent viết code
- `analyst/` — Agent phân tích dữ liệu
- `orchestrator/` — Agent điều phối nhiều agent khác
- `hello-world/` — Agent đơn giản nhất để học

### Tóm tắt:

> **Agent** trong OpenFang là đơn vị AI tự động có thể làm việc độc lập theo lịch hoặc theo yêu cầu. Mỗi agent có LLM làm não, Tools để thực thi, và Memory để ghi nhớ. Tạo agent dễ nhất qua Dashboard → New Agent → chọn template. OpenFang có 30 agent template sẵn có, 53 tools, và 60 skills để dùng ngay. Điểm mạnh nhất là "Hands" — agent tự chạy theo lịch mà không cần con người can thiệp.
---
# 15 Ghi chú về Tool trong OpenFang

### Tool trong OpenFang là gì?
Trong OpenFang, **Tool** là các **khả năng thực thi ở runtime** (capability) mà Agent/Hand có thể gọi để “làm việc thật” thay vì chỉ tạo văn bản. Tool có thể là web search/fetch, đọc/ghi file, chạy lệnh, thao tác browser, truy xuất memory/knowledge graph, tạo lịch (schedule), phát sự kiện (event), v.v. (xem khái niệm Tools/Skills trong “Core Concepts”: `https://openfang.info/docs/concepts`).

Điểm quan trọng: **Agent chỉ thấy và chỉ gọi được các tool đã được cấp quyền** (capability-based security + RBAC). Kernel sẽ chặn mọi lời gọi tool nằm ngoài danh sách đã khai báo/được cho phép (tham chiếu tổng quan bảo mật: `https://openfang.info/docs/security`).

### “Tools” khác “Skills” thế nào?
- **Tools**: “tay” của agent — các API/hành động hệ thống cung cấp lúc chạy (web/file/shell/browser/memory…).
- **Skills**: gói tri thức + quy trình + (có thể kèm code) để agent làm tốt một domain; OpenFang hỗ trợ SKILL.md và nhiều loại skill (Python/Node/WASM/PromptOnly) (tham chiếu: `https://openfang.info/docs/concepts`).

### Cách đăng ký (enable) tool vào Agent/Hand như thế nào?
Trong OpenFang, tool thường được **khai báo trong manifest `HAND.toml`** của Hand. Trường `tools = [...]` là danh sách tool mà agent runtime sẽ đưa vào “available tools” để LLM có thể gọi.

Ví dụ thật từ `Researcher Hand` trên repo OpenFang (trích từ `crates/openfang-hands/bundled/researcher/HAND.toml`):
```toml
tools = ["shell_exec", "file_read", "file_write", "file_list",
         "web_fetch", "web_search", "memory_store", "memory_recall",
         "schedule_create", "schedule_list", "schedule_delete",
         "knowledge_add_entity", "knowledge_add_relation", "knowledge_query",
         "event_publish"]
```
Nguồn: `https://raw.githubusercontent.com/RightNow-AI/openfang/main/crates/openfang-hands/bundled/researcher/HAND.toml`

### Quy trình gọi tool (mô hình hóa đơn giản)
1. **Khai báo quyền**: Hand/Agent khai báo danh sách tool trong manifest (ví dụ `HAND.toml`).
2. **Kernel kiểm soát**: khi agent chạy, kernel/runtime chỉ “phơi bày” (inject) những tool được phép; mọi lời gọi khác bị chặn theo capability gates/RBAC.
3. **LLM quyết định gọi**: trong vòng lặp agent, LLM chọn tool phù hợp, tạo tham số (theo schema), rồi runtime thực thi.
4. **Trả kết quả & ghi dấu vết**: kết quả tool trả về cho LLM để tổng hợp câu trả lời; các lớp an toàn (audit trail, taint tracking, loop guard…) giảm rủi ro “agent chạy quá đà”.

### Bảng phân loại tool hay gặp (theo nhóm chức năng)
| Nhóm | Ví dụ tool | Dùng để làm gì |
| :--- | :--- | :--- |
| Web | `web_search`, `web_fetch` | Tìm và lấy nội dung từ Internet (có lớp chống SSRF theo docs bảo mật). |
| File | `file_read`, `file_write`, `file_list` | Đọc/ghi/liệt kê file phục vụ workflow. |
| Shell/Exec | `shell_exec` | Chạy lệnh hệ thống (bị kiểm soát quyền và sandbox). |
| Memory | `memory_store`, `memory_recall` | Lưu/nhớ trạng thái dài hạn giữa các lần chạy. |
| Knowledge Graph | `knowledge_add_entity`, `knowledge_add_relation`, `knowledge_query` | Biểu diễn tri thức dạng thực thể–quan hệ để truy vấn lại. |
| Schedule | `schedule_create`, `schedule_list`, `schedule_delete` | Lập lịch chạy định kỳ cho Hand. |
| Events | `event_publish` | Phát sự kiện để tích hợp workflow/trigger/observability. |

### Tóm tắt:
> **Tool** trong OpenFang là các khả năng thực thi ở runtime (web/file/shell/browser/memory/knowledge/schedule…) giúp agent “làm việc thật”. Tool được **enable bằng cách khai báo danh sách `tools = [...]` trong manifest** (ví dụ `HAND.toml` của Hand), sau đó kernel/runtime chỉ inject đúng các tool được phép theo **capability gates + RBAC**. Khi chạy, LLM chọn gọi tool, runtime thực thi và trả kết quả về để agent tổng hợp.
