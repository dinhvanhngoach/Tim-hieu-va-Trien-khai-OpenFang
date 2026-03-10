# OpenFang – Notes Day 1

## 1. OpenFang là gì? Dùng để làm gì

OpenFang là một **AI Agent Operating System mã nguồn mở** được xây dựng bằng **Rust**.  
Hệ thống cho phép các nhà phát triển tạo ra **AI Agent tự động** có khả năng thực hiện các nhiệm vụ mà không cần con người giám sát liên tục.

OpenFang cung cấp các agent tích hợp sẵn gọi là **Hands** như:

- Researcher
- Browser

Các agent này có thể:

- Thu thập dữ liệu
- Phân tích thông tin
- Tự động hóa quy trình làm việc

OpenFang được sử dụng để:

- Xây dựng hệ thống **AI Automation**
- Tạo các **AI Agent tự động**
- Triển khai AI trong các ứng dụng thực tế

---

# 2. Kiến trúc OpenFang

Các thành phần chính trong OpenFang:



## Agent (Hand)

Agent là **đơn vị thực thi tự động** trong hệ thống.

Agent hoạt động theo vòng lặp:

Agent được **Kernel của OpenFang tạo và quản lý**.

Lifecycle của Agent:

- Running
- Suspended
- Terminated


## Tool / Skills

Tool là các chức năng mà agent có thể gọi để thực hiện hành động.

Ví dụ:

- web_search
- web_fetch
- file_read
- shell_exec

OpenFang hiện có **53+ built-in tools**.

Các tool chạy trong **WASM sandbox** để đảm bảo:

- cách ly
- bảo mật
- an toàn hệ thống


## Memory

Memory là hệ thống lưu trữ thông tin của agent.

Bao gồm:

- SQLite (lưu dữ liệu)
- Vector Embeddings (tìm kiếm semantic)
- Knowledge Graph

Memory giúp agent:

- ghi nhớ thông tin
- duy trì ngữ cảnh
- sử dụng dữ liệu giữa các lần chạy

---

# 3. Ví dụ OpenFang trên GitHub

Repository:
