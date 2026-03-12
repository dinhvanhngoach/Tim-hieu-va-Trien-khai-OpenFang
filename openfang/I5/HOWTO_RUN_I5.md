# HOWTO_RUN_I5.md — Cách chạy các demo & test liên quan đến I5

## 1. Chạy các agent Python demo (I3, I4)
Đứng tại thư mục gốc repo:

```bash
cd C:\Users\OS\Tim-hieu-va-Trien-khai-OpenFang
```

### I3 — Agent cơ bản với 2 tool

- Chạy agent (nhập tay):

```bash
python openfang/I3/agent_basic.py
```

- Chạy test (kiểm tra tool + agent + xử lý lỗi input sai kiểu):

```bash
python -m unittest -v openfang.I3.test_agent
```

### I4 — Agent nâng cấp + memory

- Chạy agent cơ bản:

```bash
python openfang/I4/agent_basic.py
```

- Chạy agent bản I4 đầy đủ (tự test + nhập tay):

```bash
python openfang/I4/agent_basic_I4.py
```

- Chạy test (kiểm tra tool, agent, memory, xử lý lỗi input sai kiểu):

```bash
python -m unittest -v openfang.I4.test_agent
```

## 2. Kiểm tra xử lý lỗi input sai kiểu cho tool
Trong cả I3 và I4:
- `Agent.run("double", "abc")` **không làm crash chương trình**.
- Thay vào đó, màn hình in:
  - Tool đang dùng (`double`)
  - Thông báo lỗi input không hợp lệ
  - Chi tiết `ValueError` từ Python.

Các hành vi này đã được cover bởi test mới trong:
- `openfang/I3/test_agent.py`
- `openfang/I4/test_agent.py`

## 3. Docs & nhật ký liên quan cho I5
- Ghi chú khái niệm Tool: `openfang/I5/notes_I5_TrinhVanVinh.md`
- Lỗi thường gặp & cách fix: `openfang/I5/ERRORS_LOG.md`
- Báo cáo chi tiết xử lý lỗi input tool: `openfang/I5/REPORT_ERROR_HANDLING_TOOL_INPUT.md`

---
*Soạn bởi: I5 — Trịnh Văn Vinh*
