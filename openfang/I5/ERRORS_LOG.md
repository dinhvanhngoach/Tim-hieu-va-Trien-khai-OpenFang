# I5 — ERROR_LOG — Các lỗi phổ biến OpenFang (I1–I4)

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

---
*Tổng hợp bởi: I5 — Trịnh Văn Vinh*