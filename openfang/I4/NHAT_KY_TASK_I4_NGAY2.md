# NHẬT KÝ LÀM TASK I4 — NGÀY 2 (THỨ BA)
## Chủ đề: Build Agent Đầu Tiên Trong OpenFang

---

## 1. Task được giao

**I4 — Ngày 2:**
- Lấy code `agent_basic.py` của I1+I2 về, đọc hiểu trước khi làm tiếp
- Gắn `tool_double` (do I3 viết) vào agent
- Test agent với cả 2 tool: gọi `uppercase` rồi gọi `double`
- Đảm bảo agent biết dùng đúng tool khi được yêu cầu — không nhầm lẫn tool
- Push code lên repo, mô tả rõ đã thêm gì trong commit message

---

## 2. Chuẩn bị

### Lấy code từ I1+I2+I3

```bash
cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang
git pull origin main
```

### File cần đọc hiểu trước khi làm

**`agent_basic.py`** (I1+I2 viết):
```python
# Tool 1: chuyển chữ hoa
def tool_uppercase(text):
    return text.upper()

# Agent class
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list

    def run(self, tool_name, input_data):
        if tool_name in self.tools:
            result = self.tools[tool_name](input_data)
            print(f"Ket qua: {result}")
        else:
            print(f"Loi: khong tim thay tool '{tool_name}'")
```

**`tool_double.py`** (I3 viết):
```python
# Tool 2: nhân đôi số nguyên
def tool_double(number):
    return int(number) * 2
```

---

## 3. Viết file agent_basic_I4.py

I4 tạo file riêng `agent_basic_I4.py` — lấy code từ I1+I2+I3, gắn 2 tool vào agent, thêm test tự động và menu nhập tay.

### Nội dung file

```python
# agent_basic_I4.py
# I4 - Phạm Quốc Đạt
# Lấy code từ I1+I2+I3, gắn 2 tool, test và thêm nhập tay

# --- TOOL 1 (I2) ---
def tool_uppercase(text):
    return text.upper()

# --- TOOL 2 (I3) ---
def tool_double(number):
    return int(number) * 2

# --- AGENT (I1+I2) ---
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list

    def run(self, tool_name, input_data):
        print(f"\n[Agent {self.name} dang chay...]")
        if tool_name in self.tools:
            result = self.tools[tool_name](input_data)
            print(f"Tool su dung: {tool_name}")
            print(f"Ket qua: {result}")
        else:
            print(f"Loi: khong tim thay tool '{tool_name}'")
            print(f"Cac tool co san: {list(self.tools.keys())}")

if __name__ == "__main__":
    danh_sach_tools = {
        "uppercase": tool_uppercase,
        "double": tool_double
    }

    agent = Agent(
        name="TextProcessor",
        description="Agent xu ly van ban va so hoc.",
        tools_list=danh_sach_tools
    )

    # --- TEST TỰ ĐỘNG ---
    print("=== TEST TU DONG ===")

    # Test 1: Gọi tool_uppercase
    print("\n[TEST 1] Goi tool_uppercase:")
    agent.run("uppercase", "hello openfang")

    # Test 2: Gọi tool_double
    print("\n[TEST 2] Goi tool_double:")
    agent.run("double", 21)

    # Test 3: Tool không tồn tại (kiểm tra xử lý lỗi)
    print("\n[TEST 3] Tool khong ton tai:")
    agent.run("unknown_tool", "test")

    print("\n[KET QUA] Agent phan biet dung 2 tool!")

    # --- NHẬP TAY ---
    print("\n=== NHAP TAY ===")
    tool = input("Chon tool (uppercase / double): ")
    user_input = input("Nhap du lieu: ")
    agent.run(tool, user_input)
```

---

## 4. Kết quả chạy thử

```
=== TEST TU DONG ===

[TEST 1] Goi tool_uppercase:
[Agent TextProcessor dang chay...]
Tool su dung: uppercase
Ket qua: HELLO OPENFANG

[TEST 2] Goi tool_double:
[Agent TextProcessor dang chay...]
Tool su dung: double
Ket qua: 42

[TEST 3] Tool khong ton tai:
[Agent TextProcessor dang chay...]
Loi: khong tim thay tool 'unknown_tool'
Cac tool co san: ['uppercase', 'double']

[KET QUA] Agent phan biet dung 2 tool!
```

---

## 5. Lỗi gặp phải & cách fix

| Lỗi | Nguyên nhân | Cách fix |
|---|---|---|
| `git push rejected` | Remote có commit mới hơn local | Chạy `git pull origin main` trước rồi push lại |
| Vim editor mở khi merge | Git tự mở editor để nhập commit message | Nhấn `Esc` → gõ `:wq` → Enter |
| File I3 tạo nhầm là file thay vì folder | Tạo file tên `I3` thay vì folder | Xóa file, tạo lại đúng là folder |

---

## 6. Push code lên GitHub

```bash
cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang
git add openfang/I4/agent_basic_I4.py
git commit -m "I4: Ngay 2 - them agent_basic_I4.py, gan 2 tool, test tu dong + nhap tay"
git pull origin main
git push origin main
```

---

## 7. Cấu trúc folder I4 sau Ngày 2

```
openfang/I4/
    agent_basic_I4.py          ← File chính Ngày 2 ✅
    notes_I4_PhamQuocDat.md    ← Ghi chú từ Ngày 1
```

---

## 8. Output cuối ngày

- ✅ `agent_basic_I4.py` với 2 tool gắn vào agent
- ✅ 3 test tự động pass (uppercase, double, tool không tồn tại)
- ✅ Agent không nhầm tool
- ✅ Code đã push lên GitHub

---

*Ghi lại bởi: I4 — Phạm Quốc Đạt | Ngày 2 — Thứ Ba*
