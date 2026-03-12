# I5 — ERRORS_LOG — Các lỗi phổ biến gặp khi chạy demo (I1–I4)

### 1. Lỗi import sai module demo trong repo OpenFang
- **Mô tả**: Trong code mẫu ban đầu có dòng:
  - `from src.spikes.deps import Deps, User, agent, chat, create_deps`
  - Khi chạy trong repo `Tim-hieu-va-Trien-khai-OpenFang` sẽ báo:  
    `ModuleNotFoundError: No module named 'src.spikes'`
- **Nguyên nhân**: Repo này không có thư mục `src/spikes` như ví dụ gốc.
- **Cách fix (I1 đã làm)**:
  - Xóa dòng import đó.
  - Viết lại agent + tool trực tiếp trong file (ví dụ `agent_basic.py`).
  - Chạy đúng thư mục:  
    `cd Tim-hieu-va-Trien-khai-OpenFang\openfang\I1` rồi `python agent_basic.py`.

### 2. Lỗi gọi sai tên tool trong agent tự viết (I4)
- **Mô tả**: Trong `agent_basic_I4.py`, danh sách tool:
  - `"uppercase"` → `tool_uppercase`  
  - `"double"` → `tool_double`
- Nếu gọi `agent.run("unknown_tool", "test")` thì agent in:
  - Không tìm thấy công cụ `"unknown_tool"` và liệt kê lại các tool có sẵn.
- **Bài học**:
  - Khi build agent với dict `tools`, luôn kiểm tra key name khớp với tên bạn dự định dùng.
  - Với OpenFang thật, tên tool trong `HAND.toml`/manifest cũng phải khớp với tool runtime.

### 3. Lỗi nhập sai kiểu dữ liệu cho tool xử lý số (I3/I4)
- **Ngữ cảnh**:
  - `tool_double.py` và `agent_basic_I4.py` đều dùng `int(number) * 2`.
- **Lỗi tiềm ẩn**:
  - Nếu user nhập `"abc"` hoặc chuỗi không phải số cho tool `"double"` thì Python sẽ ném `ValueError` khi `int(number)`.
- **Cách tránh**:
  - Khi test tay, chú ý nhập số hợp lệ (ví dụ `21`, `5`, `100`).
  - Nếu mang ý tưởng này sang OpenFang thật, nên validate input trước khi cast sang `int`.

### 4. Lỗi “không hiểu yêu cầu” do nhập tiếng Việt không dấu (I1 — agent_memory)
- **Triệu chứng**:
  - Input: `luc nay may lam gi`
  - Output: `Không hiểu yêu cầu.`
- **Nguyên nhân**:
  - Logic xử lý câu hỏi trong `agent_memory.py` (demo) phụ thuộc vào pattern tiếng Việt có dấu/đúng cụm từ, nên viết không dấu sẽ không match.
- **Cách tránh**:
  - Khi test demo memory, nhập có dấu (ví dụ: `lúc nãy mày làm gì`) hoặc chỉnh lại code để normalize dấu/khớp nhiều biến thể.

### 5. Lỗi “Chưa có hành động nào trước đó” khi hỏi memory quá sớm (I1 — agent_memory)
- **Triệu chứng**:
  - Hỏi: `lúc nãy mày làm gì` ngay từ đầu
  - Agent trả: `Chưa có hành động nào trước đó.`
- **Nguyên nhân**:
  - Demo memory chỉ “nhớ” khi trước đó đã có hành động (ví dụ chạy `uppercase hello`) để lưu lại.
- **Cách tránh**:
  - Thực hiện 1 hành động trước (ví dụ `uppercase hello`), rồi mới hỏi memory.

### 6. Lỗi chạy sai đường dẫn tương đối khi gọi `python I*/...` (HOWTO_RUN)
- **Triệu chứng**:
  - Chạy `python I3/agent_basic.py` nhưng đang đứng sai thư mục → Python báo không tìm thấy file.
- **Cách tránh**:
  - Đứng tại thư mục `openfang/` rồi chạy theo đường dẫn tương đối (ví dụ `python I3/agent_basic.py`), hoặc `cd openfang\I3` rồi `python agent_basic.py`.

---
*Tổng hợp bởi: I5 — Trịnh Văn Vinh*