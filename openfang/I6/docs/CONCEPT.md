
---

# [DOCS] TỔNG QUAN VỀ HỆ SINH THÁI OPENFANG

Tài liệu này tổng hợp các kiến thức nền tảng mà nhóm đã tìm hiểu và phân tích trong tuần qua.

## 1. OpenFang là gì? (Khái niệm chung)

OpenFang là một **hệ điều hành tác nhân AI (Agent OS)** mã nguồn mở được phát triển bằng ngôn ngữ **Rust**. Khác với các thư viện AI thông thường, OpenFang cung cấp một môi trường chạy (runtime) hoàn chỉnh để quản lý vòng đời của các AI Agent.

* **Tính an toàn:** Các thành phần của OpenFang chạy trong sandbox **WASM**, giúp cách ly Agent với hệ thống máy chủ vật lý.
* **Tính tự hành:** Cho phép Agent hoạt động liên tục (24/7) theo lịch trình (Scheduled Tasks) mà không cần sự can thiệp trực tiếp của con người.

---

## 2. Các thành phần cốt lõi (Core Components)

### 2.1 Agent (Hand) — Đơn vị thực thi

* **Khái niệm:** Là "bộ não" điều phối. Trong OpenFang, mỗi tác nhân được gọi là một **Hand**.
* **Cơ chế vận hành:** Agent nhận yêu cầu -> Sử dụng LLM để lập kế hoạch -> Quyết định sử dụng công cụ nào -> Lưu kết quả vào bộ nhớ.
* **Phân loại:** OpenFang cung cấp khoảng 30 mẫu Agent có sẵn (pre-built) và 7 loại Hands chuyên dụng cho từng tác vụ.

### 2.2 Tool — Cánh tay thực thi

* **Khái niệm:** Là các khả năng (Capabilities) cho phép Agent tương tác với môi trường bên ngoài.
* **Đặc điểm:** OpenFang hỗ trợ hơn 53 công cụ tích hợp sẵn như: Tìm kiếm web (Web Search), thao tác tệp (File Operations), chạy lệnh hệ thống (Shell), và quản lý bộ nhớ.
* **Cơ chế bảo mật:** Mỗi Tool khi được gọi đều phải thông qua Kernel để kiểm tra quyền truy cập (RBAC) và các cổng bảo mật (Capability Gates).

### 2.3 Memory — Hệ thống tri thức

* **Khái niệm:** Là hệ thống lưu trữ context bên ngoài để khắc phục tính "nhanh quên" (stateless) của LLM.
* **Cấu trúc 4 giai đoạn:** 
1.  **Persistence:** Lưu trữ hội thoại vào SQLite theo từng phiên (Session).
2.  **Semantic Encoding:** Chuyển đổi ý nghĩa văn bản thành Vector Embeddings.
3.  **Retrieval:** Tìm kiếm "ký ức" liên quan dựa trên sự tương đồng ngữ nghĩa.
4.  **Context Injection:** Đưa các mẩu ký ức tìm được vào prompt gửi cho LLM để đảm bảo câu trả lời chính xác nhất.

---

## 3. Mô hình phối hợp (Multi-Agent Architecture)

OpenFang cho phép nhiều Agent phối hợp theo mô hình **Sequential Pipeline** (Chuỗi tuần tự):

* **Processor Hand:** Tập trung vào việc xử lý logic, tính toán và biến đổi dữ liệu thô.
* **Reviewer Hand:** Tập trung vào việc đánh giá kết quả, tóm tắt và kiểm tra tính hợp lệ của dữ liệu từ Processor chuyển sang.

---

## 4. Ý nghĩa của các ví dụ thực tế (Researcher Hand)

Nhóm đã tìm hiểu về **Researcher Hand** — một ví dụ điển hình của OpenFang. Nó minh chứng cho việc Agent có thể tự động đi tìm kiếm thông tin trên internet, tổng hợp lại và viết thành báo cáo mà không cần con người điều khiển từng bước.

---

**Tổng hợp từ:**

* I1, I6: Chuyên sâu về Memory và logic điều phối.
* I2: Sơ đồ kiến trúc tổng quan.
* I3, I5: Chức năng Tool và ví dụ thực tế.
* I4, I7: Kiểm thử vận hành và thực thi Agent.

---
