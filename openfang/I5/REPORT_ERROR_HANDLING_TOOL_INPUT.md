# I5 — Báo cáo: Thêm xử lý lỗi input sai kiểu cho tool

## Mục tiêu
Khi tool nhận **input sai kiểu** (ví dụ `tool_double` nhận text `"abc"` thay vì số), agent phải:
- **In thông báo lỗi rõ ràng**
- **Không crash**

## Thay đổi đã thực hiện
- **Bọc try/except trong `Agent.run()`** để bắt lỗi khi tool chạy:
  - Bắt `ValueError`, `TypeError` → in thông báo “Dữ liệu đầu vào không hợp lệ…”
  - Bắt `Exception` chung → in thông báo “Tool gặp sự cố không mong đợi…”
  - **Không raise** ra ngoài (agent không bị crash)

## File đã chỉnh sửa
- `openfang/I3/agent_basic.py`
- `openfang/I4/agent_basic.py`
- `openfang/I4/agent_basic_I4.py`
- `openfang/I3/test_agent.py`
- `openfang/I4/test_agent.py`

## Test case bổ sung
Đã thêm test để đảm bảo **agent không crash** khi gọi:

- `agent.run("double", "abc")`

Áp dụng ở:
- `openfang/I3/test_agent.py` (test case 4)
- `openfang/I4/test_agent.py` (test case 5)

## Kết quả chạy test (unittest)
- **I3**: `python -m unittest -v openfang/I3/test_agent.py` → **OK (4 tests)**
- **I4**: `python -m unittest -v openfang/I4/test_agent.py` → **OK (5 tests)**

Ví dụ log khi input sai kiểu:
`ValueError: invalid literal for int() with base 10: 'abc'`  
→ Agent in lỗi và tiếp tục chạy, không crash.

---
*Ghi bởi: I5 — Trịnh Văn Vinh*
