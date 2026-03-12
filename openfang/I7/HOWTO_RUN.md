# HOWTO_RUN.md

# I1 – Test Agent Cơ Bản

**File:** `agent_basic.py`

## Cách chạy

```bash
python I1/agent_basic.py
```

## Input

```
uppercase hello
```

## Output

```
[Agent TextProcessor dang hoat dong...]
Su dung cong cu: uppercase
Ket qua cuoi cung: UPPERCASE HELLO
```

## Kết luận

Agent chạy thành công và tool `uppercase` hoạt động đúng.

---

# I1 – Test Agent Memory

**File:** `agent_memory.py`

## Cách chạy

```bash
python I1/agent_memory.py
```

---

## Trường hợp 1 – Viết không dấu

### Input

```
You: luc nay may lam gi
```

### Output

```
Không hiểu yêu cầu.
```

### Kết luận

Agent không nhận diện được câu hỏi khi viết không dấu.

---

## Trường hợp 2 – Chưa có hành động trước

### Input

```
You: lúc nãy mày làm gì
```

### Output

```
Chưa có hành động nào trước đó.
```

### Kết luận

Agent kiểm tra memory và thông báo chưa có hành động trước đó.

---

## Trường hợp 3 – Có hành động trước đó

### Input

```
You: uppercase hello
```

### Output

```
Result: HELLO
```

Sau đó hỏi:

```
You: lúc nãy mày làm gì
```

### Output

```
Memory: Converted 'hello' to 'HELLO'
```

### Kết luận

Agent có thể lưu memory và nhớ được hành động trước đó.

---

# Test I3

## I3 – Test Agent với 2 Tool

**Thư mục:** `openfang/I3`

## Cách chạy

```bash
python I3/agent_basic.py
```

---

## Test 1 – Tool `uppercase`

### Input

```
Nhap ten tool (uppercase / double): uppercase
Nhap du lieu: chao ban nha
```

### Output

```
[Agent TextProcessor dang hoat dong...]
Su dung cong cu: uppercase
Ket qua cuoi cung: CHAO BAN NHA
```

### Kết luận

Tool `uppercase` hoạt động đúng, chuyển toàn bộ chuỗi sang chữ in hoa.

---

## Test 2 – Tool `double`

### Input

```
Nhap ten tool (uppercase / double): double
Nhap du lieu: 100
```

### Output

```
[Agent TextProcessor dang hoat dong...]
Su dung cong cu: double
Ket qua cuoi cung: 200
```

### Kết luận

Tool `double` hoạt động đúng, nhân đôi giá trị số được nhập.

---

# Test I3 – Test Agent

**File:** `test_agent.py`

## Cách chạy

```bash
python test_agent.py
```

## Input

Không cần nhập dữ liệu (file test chạy tự động).

## Kết quả

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### Kết luận

3 test chạy thành công, agent và tool hoạt động đúng.

---

# Test I4 – Agent Basic

**File:** `agent_basic.py`

## Cách chạy

```bash
python agent_basic.py
```

## Input

```
Nhap ten tool (uppercase / double): double
Nhap du lieu: 3
```

Sau đó chạy lại:

```
Nhap ten tool (uppercase / double): uppercase
Nhap du lieu: toi la sep cua ban
```

## Kết quả

### Lần 1

```
[Agent TextProcessor dang hoat dong...]
Su dung cong cu: double
Ket qua cuoi cung: 6
```

### Lần 2

```
[Agent TextProcessor dang hoat dong...]
Su dung cong cu: uppercase
Ket qua cuoi cung: TOI LA SEP CUA BAN
```

---

# Test I4 – Agent Basic I4

**File:** `agent_basic_I4.py`

## Cách chạy

```bash
python agent_basic_I4.py
```

## Input

```
Chon tool (uppercase / double): uppercase
Nhap du lieu: to la teo
```

## Kết quả

```
I4 - TEST TU DONG VOI 2 TOOL

[TEST 1] Goi tool_uppercase:

[Agent TextProcessor dang chay...]
Tool su dung: uppercase
Ket qua: HELLO OPENFANG

[TEST 2] Goi tool_double:

[Agent TextProcessor dang chay...]
Tool su dung: double
Ket qua: 42

[TEST 3] Tool khong ton tai (kiem tra xu ly loi):

[Agent TextProcessor dang chay...]
Loi: khong tim thay cong cu 'unknown_tool' trong he thong!
Cac tool co san: ['uppercase', 'double']

[KET QUA] Agent phan biet dung 2 tool!

NHAP DU LIEU BANG TAY

[Agent TextProcessor dang chay...]
Tool su dung: uppercase
Ket qua: TO LA TEO
```

---

# Test I4 – Agent Memory

**File:** `agent_memory.py`

## Cách chạy

```bash
python agent_memory.py
```

## Input

```
You: uppercase hello
You: lúc nãy mày làm gì
```

## Kết quả

```
You: uppercase hello
Result: HELLO

You: lúc nãy mày làm gì
Memory: Converted 'hello' to 'HELLO'
```

---

# Test I4 – Test Agent

**File:** `test_agent.py`

## Cách chạy

```bash
python test_agent.py
```

## Input

Không cần nhập dữ liệu (các test được chạy tự động).

## Kết quả

```
test_agent_memory (__main__.TestAgentTools) ... ok
test_agent_run (__main__.TestAgentTools) ... ok
test_tool_double (__main__.TestAgentTools) ... ok
test_tool_uppercase (__main__.TestAgentTools) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```