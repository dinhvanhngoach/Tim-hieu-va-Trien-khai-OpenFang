# HƯỚNG DẪN TASK I4 — NGÀY 3 (THỨ TƯ)
## Chủ đề: Thêm Memory & Viết Test Tự Động

---

## 1. Tổng quan nhiệm vụ

| Người | Task |
|---|---|
| I1 | Thêm memory vào agent, test memory hoạt động |
| I2 | Test memory: gọi agent 2 lần, kiểm tra agent nhớ |
| **I3** | **Viết file test_agent.py với 3 test case** |
| **I4** | **Chạy pytest, debug, thêm test case thứ 4 về memory** |

---

## 2. Cấu trúc file cần có trong folder I4

```
openfang/I4/
    agent_basic.py      ← Copy từ I3 (có tool_uppercase + tool_double + Agent)
    agent_memory.py     ← Copy từ I1 (có memory + uppercase_tool)
    agent_basic_I4.py   ← File riêng của I4 (đã làm từ Ngày 2)
    test_agent.py       ← File test (I3 viết gốc, I4 thêm test case 4)
```

> ⚠️ Lưu ý: `agent_basic.py` phải lấy từ **I3** (có cả 2 tool), KHÔNG lấy từ I1 (chỉ có 1 tool).

---

## 3. Các bước thực hiện

### Bước 1 — Copy file cần thiết vào folder I4

```bash
cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang

# Copy agent_basic.py từ I3 (có đủ 2 tool)
cp openfang/I3/agent_basic.py openfang/I4/agent_basic.py

# Copy agent_memory.py từ I1
cp openfang/I1/agent_memory.py openfang/I4/agent_memory.py
```

**Tại sao cần 2 file này?**
- `test_agent.py` import `tool_uppercase`, `tool_double`, `Agent` từ `agent_basic`
- `test_agent.py` import `uppercase_tool`, `memory` từ `agent_memory`

---

### Bước 2 — Hiểu cấu trúc file test_agent.py

File `test_agent.py` gồm 4 test case:

```python
# Test case 1 (I3): Kiểm tra tool_uppercase chạy đúng
def test_tool_uppercase(self):
    result = tool_uppercase("hello")
    self.assertEqual(result, "HELLO")   # "hello" → "HELLO" ✅

# Test case 2 (I3): Kiểm tra tool_double chạy đúng
def test_tool_double(self):
    result = tool_double(5)
    self.assertEqual(result, 10)        # 5 × 2 = 10 ✅

# Test case 3 (I3): Kiểm tra agent có đủ 2 tool
def test_agent_run(self):
    agent = Agent(name="TestAgent", description="...", tools_list=tools)
    self.assertIn("uppercase", agent.tools)   # agent có tool uppercase ✅
    self.assertIn("double", agent.tools)      # agent có tool double ✅

# Test case 4 (I4): Kiểm tra agent nhớ được context (MEMORY)
def test_agent_memory(self):
    memory.clear()                        # Xóa memory trước khi test
    result1 = uppercase_tool("hello")     # Gọi lần 1
    self.assertEqual(len(memory), 1)      # Memory phải có 1 entry
    self.assertIn("HELLO", memory[0])     # Entry phải chứa kết quả
    result2 = uppercase_tool("openfang") # Gọi lần 2
    self.assertEqual(len(memory), 2)      # Memory phải có 2 entry
    self.assertIn("OPENFANG", memory[1]) # Entry thứ 2 đúng không
```

---

### Bước 3 — Cài pytest

```bash
pip install pytest
```

Kiểm tra đã cài chưa:
```bash
pytest --version
```

---

### Bước 4 — Chạy pytest

```bash
cd openfang/I4
pytest test_agent.py -v
```

**Kết quả mong đợi:**
```
test_agent_memory     PASSED ✅
test_agent_run        PASSED ✅
test_tool_double      PASSED ✅
test_tool_uppercase   PASSED ✅
4 passed in 0.05s
```

---

### Bước 5 — Kiểm tra riêng test case 4 (memory)

```bash
pytest test_agent.py::TestAgentTools::test_agent_memory -v
```

Test này kiểm tra 4 điều:

| Kiểm tra | Ý nghĩa |
|---|---|
| `result1 == "HELLO"` | Tool chạy đúng lần 1 |
| `len(memory) == 1` | Memory đã lưu sau lần 1 |
| `result2 == "OPENFANG"` | Tool chạy đúng lần 2 |
| `len(memory) == 2` | Memory nhớ cả 2 lần |

---

### Bước 6 — Push code lên GitHub

```bash
cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang
git add openfang/I4/
git commit -m "I4: Ngay 3 - test_agent.py 4 test pass, agent_basic.py, agent_memory.py"
git push origin main
```

---

## 4. Lỗi thường gặp & cách fix

| Lỗi | Nguyên nhân | Cách fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'agent_basic'` | Chưa có file hoặc chạy sai folder | Chạy pytest từ trong folder I4 |
| `cannot import name 'tool_double'` | Copy nhầm `agent_basic.py` từ I1 thay vì I3 | Copy lại từ I3 |
| `agent_basic.p` thiếu chữ `y` | Lỗi khi copy file | `mv agent_basic.p agent_basic.py` |

---

## 5. Output cuối ngày cần có

- ✅ File `test_agent.py` với 4 test case
- ✅ Tất cả 4 test PASS khi chạy `pytest test_agent.py -v`
- ✅ Code đã push lên GitHub

---

*Hướng dẫn bởi: I4 — Phạm Quốc Đạt | Ngày 3 — Thứ Tư*
