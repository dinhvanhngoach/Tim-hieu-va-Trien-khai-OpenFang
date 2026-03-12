# Cách chạy main.py

1. Mở Git Bash
cd Tim-hieu-va-Trien-khai-OpenFang/openfang/I3
2. Chạy chương trình
## Bước 1: Test Agent 1 (I1 + I2)
python agent_basic.py
tool upercase:
![alt text](image.png)

tool double:
![alt text](image-1.png)

## BƯỚC 2 — Test Agent 2 (Reviewer)
python agent_second.py
![alt text](image-2.png)
vậy:
✔ tool_summarize hoạt động đúng
✔ Reviewer.run() hoạt động đúng
✔ Test riêng Agent 2 (I4) → PASS

# Test agent_basic_I4.py
Cách chạy chương trình:
python I4/agent_basic_I4.py
Kết quả test tự động:
3. Kết quả test tự động
Test 1 – Tool uppercase
Input:
HELLO OPENFANG
Output:
[Agent TextProcessor dang chay...]
Tool su dung: uppercase
Ket qua: HELLO OPENFANG
Agent gọi đúng tool và xử lý chuỗi thành chữ in hoa.
Test 2 – Tool double
Input:
21
Output:
[Agent TextProcessor dang chay...]
Tool su dung: double
Ket qua: 42
Agent thực hiện phép nhân đôi số.
Test 3 – Tool không tồn tại
Input:
unknown_tool
Output:
Loi: khong tim thay cong cu 'unknown_tool' trong he thong!
Cac tool co san: ['uppercase', 'double']

Agent phát hiện tool không tồn tại và hiển thị danh sách tool hợp lệ.

4. Test nhập dữ liệu thủ công

Người dùng chọn tool và nhập dữ liệu trực tiếp.

Chon tool (uppercase / double): uppercase
Nhap du lieu: chao ban minh la tep

Output:

[Agent TextProcessor dang chay...]
Tool su dung: uppercase
Ket qua: CHAO BAN MINH LA TEP

Agent xử lý đúng dữ liệu người dùng nhập.
---
# Chạy file main.py:
python main.py

Tool uppercase:
![alt text](image-4.png)
tool double:
![alt text](image-5.png)

---
Chạy test Agent:
python test_agent.py
![alt text](image-6.png)
Chạy test Reviewer
python test_reviewer.py
![alt text](image-7.png)

---
Chạy test I5
cd F:\Tim-hieu-va-Trien-khai-OpenFang
phải chuột -> GIT BASH HERE
python -m unittest -v openfang.I5.test_main_pipeline
Kết quả:
![alt text](image-8.png)
pipeline hoạt động đúng
