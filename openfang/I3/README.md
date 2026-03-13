# Tìm Hiểu và Triển Khai OpenFang

## 1. Giới thiệu dự án

Dự án **Tìm Hiểu và Triển Khai OpenFang** nhằm mục tiêu nghiên cứu cách xây dựng và vận hành các AI Agent bằng framework **OpenFang**.

Trong dự án này, nhóm thực hiện:

* Cài đặt và cấu hình môi trường OpenFang
* Xây dựng các **Agent** có thể sử dụng nhiều **Tool**
* Thêm **Memory** để agent ghi nhớ thông tin
* Viết **Test tự động** để đảm bảo hệ thống hoạt động ổn định
* Triển khai **nhiều agent phối hợp với nhau**

Mục tiêu cuối cùng là xây dựng một hệ thống **2 AI Agent có thể phối hợp xử lý nhiệm vụ**.

---

# 2. Mục tiêu theo tuần

## Ngày 1 – Thứ Hai

**Làm Quen & Cài Đặt Môi Trường OpenFang**

* Tất cả thành viên cài đặt thành công OpenFang
* Chạy được demo đầu tiên

---

## Ngày 2 – Thứ Ba

**Build Agent Đầu Tiên Trong OpenFang**

* Xây dựng 1 Agent cơ bản
* Agent có **2 Tool hoạt động**
* Có tài liệu mô tả chi tiết

---

## Ngày 3 – Thứ Tư

**Thêm Memory & Viết Test Tự Động**

* Agent có khả năng **ghi nhớ dữ liệu**
* Có **xử lý lỗi**
* Viết **4 test case**
* Tất cả test đều **pass**

---

## Ngày 4 – Thứ Năm

**Mở Rộng — Nhiều Agent Hoạt Động**

* Xây dựng **2 Agent**
* Hai agent có thể **phối hợp thực hiện nhiệm vụ**
* Có **test tự động**
* Có **tài liệu hướng dẫn**

---

## Ngày 5 – Thứ Sáu

**Hoàn Thiện & Demo Cuối Tuần**

* Demo hệ thống hoàn chỉnh
* 2 Agent phối hợp xử lý task
* Có tài liệu đầy đủ
* Có test đảm bảo hệ thống ổn định

---

# 3. Cài đặt dự án

### 1. Clone repository

```bash
git clone https://github.com/dinhvanhngoach/Tim-hieu-va-Trien-khai-OpenFang.git
```

### 2. Di chuyển vào thư mục dự án

```bash
cd Tim-hieu-va-Trien-khai-OpenFang
```

### 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

# 4. Chạy dự án

Chạy agent chính:

```bash
python main.py
```

Hoặc chạy tool riêng:

```bash
python openfang/I3/tool_double.py
```

---

# 7. Ví dụ Output

### Input

```
Input number: 5
```

### Output

```
Running tool_double...

Result: 10
```

---

# 8. Chạy Test

Để kiểm tra hệ thống:

```bash
pytest
```

Ví dụ kết quả:

```
====================
4 passed in 0.10s
====================
```

---

# 9. Demo Multi-Agent

Ví dụ hệ thống có 2 agent:

Agent 1: xử lý phép toán
Agent 2: phân tích kết quả

Output:

```
Agent1: Calculating result...
Agent2: Analyzing output...

Final Result: 20
```

---
