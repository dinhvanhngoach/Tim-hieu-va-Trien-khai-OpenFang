# 15 — Trịnh Văn Vinh — Ghi chú về Tool trong OpenFang

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

### Ví dụ output khi chạy demo OpenFang
Khi chạy lệnh demo trong README:

```bash
openfang chat researcher
> "What are the emerging trends in AI agent frameworks?"
```

Agent `researcher` (được cấu hình với các tool như `web_search`, `web_fetch`, `memory_store`, `knowledge_*`, ...) sẽ tự gọi tool để tìm kiếm, tổng hợp và trả về kết quả dạng:

> **Question**: What are the emerging trends in AI agent frameworks?  
> **Key Findings:**  
> - The current trends in AI agent frameworks include the evolution of Large Language Models (LLMs), Generative AI, and the integration of AI prompt engineering.  
> - The leading frameworks of 2025 are expected to be tailored to enhance the development and deployment of intelligent agents.  
> - The landscape of AI agent technology has undergone significant transformation in recent years, driven by breakthroughs in large language models, reinforcement learning, multi-agent systems, and tool integration frameworks.  
> - The future of AI agent frameworks is expected to be shaped by the increasing use of LLMs and Generative AI in various applications.  
> **Sources Used:** DuckDuckGo, Medium, arXiv, LinkedIn, digitalissimple.com  

Ví dụ này thể hiện rõ: LLM không tự bịa mà **dùng các tool web search/fetch để đi thu thập dữ liệu, sau đó tổng hợp lại** thành câu trả lời có dẫn nguồn.

### Agent demo (I3/I4) đã có xử lý lỗi input tool
Khi áp dụng ý tưởng Tool vào các agent Python demo (I3/I4), phần `Agent.run()` đã được bổ sung:
- Nếu tool (đặc biệt là `tool_double`) nhận **input sai kiểu** (ví dụ `"abc"` thay vì số), agent:
  - In thông báo: dữ liệu đầu vào không hợp lệ + chi tiết `ValueError`
  - **Không crash chương trình**.
- Hành vi này đã được kiểm chứng bằng test tự động:
  - `python -m unittest -v openfang.I3.test_agent`
  - `python -m unittest -v openfang.I4.test_agent`
Chi tiết được ghi trong `I5/REPORT_ERROR_HANDLING_TOOL_INPUT.md`.

### Tóm tắt ngắn (3-5 dòng cho team)
> **Tool** trong OpenFang là các khả năng thực thi ở runtime (web/file/shell/browser/memory/knowledge/schedule…) giúp agent “làm việc thật”. Tool được **enable bằng cách khai báo danh sách `tools = [...]` trong manifest** (ví dụ `HAND.toml` của Hand), sau đó kernel/runtime chỉ inject đúng các tool được phép theo **capability gates + RBAC**. Khi chạy, LLM chọn gọi tool, runtime thực thi và trả kết quả về để agent tổng hợp.

---
*Ghi chú bởi: 15 — Trịnh Văn Vinh | Ngày 1 — Thứ Hai*