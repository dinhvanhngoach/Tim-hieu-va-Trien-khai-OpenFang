# NHẬT KÝ LÀM TASK I4 — NGÀY 4 (THỨ NĂM)
## Chủ đề: Mở Rộng — Nhiều Agent Cùng Hoạt Động

---

## 1. Task được giao

**I4 — Ngày 4:**
- Viết test cho Reviewer agent: `tool_summarize` hoạt động đúng, agent trả lời được
- Cùng I5 chạy tất cả test — nếu fail thì debug cùng I1+I2+I3

---

## 2. Chuẩn bị file

### Kiểm tra file cần thiết

Trước khi làm task, cần có đủ các file sau trong folder I4:

| File | Từ đâu | Vai trò |
|---|---|---|
| `agent_basic.py` | I3 | Agent 1 + 2 tool |
| `agent_second.py` | I1 | Reviewer agent + tool_summarize |
| `agent_memory.py` | I1 | Memory cho agent |
| `main.py` | I3 (đã fix) | Pipeline 2 agent phối hợp |
| `test_agent.py` | I3+I4 | 4 test từ Ngày 3 |

### Vấn đề phát hiện với main.py của I3

File `main.py` gốc của I3 có 2 lỗi:
1. **Import sai**: `from agent_basic import Reviewer` → phải là `from agent_second import Reviewer`
2. **Bị lặp 2 lần**: toàn bộ nội dung bị viết 2 lần trong cùng 1 file

**Cách fix**: Tạo lại file `main.py` sạch, giữ lại phần đúng:
```python
from agent_second import Reviewer  # ← đúng
```

### Copy file vào folder I4

```bash
# Copy agent_second.py từ I1
cp ../I1/agent_second.py ./agent_second.py

# Copy main.py đã fix
cp "/c/Users/MY PC/Downloads/main.py" openfang/I4/main.py
```

---

## 3. Viết test_reviewer.py

### Nội dung file

```python
# test_reviewer.py
# I4 - Phạm Quốc Đạt
# Ngày 4: Viết test cho Reviewer agent và tool_summarize

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_second import tool_summarize, Reviewer


class TestReviewer(unittest.TestCase):

    # Test case 1: tool_summarize hoạt động đúng với text có dấu chấm
    def test_tool_summarize_basic(self):
        text = "Hello world. This is a test. Another sentence."
        result = tool_summarize(text)
        self.assertEqual(result, "Hello world")

    # Test case 2: tool_summarize với text 1 câu không có dấu chấm
    def test_tool_summarize_no_dot(self):
        text = "Hello world"
        result = tool_summarize(text)
        self.assertEqual(result, "Hello world")

    # Test case 3: Reviewer agent khởi tạo đúng
    def test_reviewer_init(self):
        reviewer = Reviewer()
        self.assertEqual(reviewer.name, "Reviewer")
        self.assertIsNotNone(reviewer.description)

    # Test case 4: Reviewer agent chạy được với input hợp lệ
    def test_reviewer_run(self):
        reviewer = Reviewer()
        try:
            reviewer.run("This is Agent 1 output. Some more text.")
            passed = True
        except Exception:
            passed = False
        self.assertTrue(passed)
```

### Giải thích từng test case

| Test case | Kiểm tra | Ý nghĩa |
|---|---|---|
| `test_tool_summarize_basic` | `tool_summarize("Hello world. ...")` == `"Hello world"` | Tool lấy đúng câu đầu tiên |
| `test_tool_summarize_no_dot` | `tool_summarize("Hello world")` == `"Hello world"` | Tool xử lý đúng khi không có dấu chấm |
| `test_reviewer_init` | `reviewer.name == "Reviewer"` | Agent khởi tạo đúng tên và mô tả |
| `test_reviewer_run` | Không raise exception | Agent chạy được với input hợp lệ |

---

## 4. Chạy test

### Chạy riêng test_reviewer.py

```bash
cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang/openfang/I4
pytest test_reviewer.py -v
```

**Kết quả:**
```
test_reviewer_init           PASSED ✅
test_reviewer_run            PASSED ✅
test_tool_summarize_basic    PASSED ✅
test_tool_summarize_no_dot   PASSED ✅
4 passed in 0.06s
```

### Chạy tất cả test (I4 + I5)

```bash
pytest test_agent.py test_reviewer.py -v
```

**Kết quả:**
```
test_agent.py::TestAgentTools::test_agent_memory     PASSED ✅
test_agent.py::TestAgentTools::test_agent_run        PASSED ✅
test_agent.py::TestAgentTools::test_tool_double      PASSED ✅
test_agent.py::TestAgentTools::test_tool_uppercase   PASSED ✅
test_reviewer.py::TestReviewer::test_reviewer_init   PASSED ✅
test_reviewer.py::TestReviewer::test_reviewer_run    PASSED ✅
test_reviewer.py::TestReviewer::test_tool_summarize_basic  PASSED ✅
test_reviewer.py::TestReviewer::test_tool_summarize_no_dot PASSED ✅
8 passed in 0.18s
```

---

## 5. Cấu trúc folder I4 sau Ngày 4

```
openfang/I4/
    agent_basic.py              ← Copy từ I3
    agent_basic_I4.py           ← File riêng của I4 (Ngày 2)
    agent_memory.py             ← Copy từ I1
    agent_second.py             ← Copy từ I1
    main.py                     ← Pipeline 2 agent (đã fix từ I3)
    test_agent.py               ← 4 test từ Ngày 3
    test_reviewer.py            ← 4 test mới Ngày 4 ✅
    notes_I4_PhamQuocDat.md     ← Ghi chú Ngày 1
    HUONG_DAN_TASK_I4_NGAY3.md  ← Hướng dẫn Ngày 3
```

---

## 6. Output cuối ngày

- ✅ `test_reviewer.py` với 4 test case
- ✅ 8/8 test PASS (`test_agent.py` + `test_reviewer.py`)
- ✅ Code đã push lên GitHub

---

*Ghi lại bởi: I4 — Phạm Quốc Đạt | Ngày 4 — Thứ Năm*
