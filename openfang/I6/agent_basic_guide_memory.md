# I6 — Nguyễn Đang Trường — Ghi chú về Agent Cơ bản & Kiểm thử (OpenFang)

### Agent Cơ bản là gì?
Tài liệu này mô tả cấu trúc và cách vận hành của Agent cơ bản được xây dựng trong giai đoạn tìm hiểu framework **OpenFang**. Agent đóng vai trò là bộ não điều phối các công cụ (tools) để xử lý yêu cầu từ người dùng.

Hệ thống được thiết kế theo hướng linh hoạt, cho phép mở rộng thêm công cụ mới mà không cần sửa đổi cấu trúc cốt lõi của Agent. Cơ chế này đảm bảo tính tách biệt giữa logic điều phối và các chức năng thực thi chuyên biệt.



### Quy trình vận hành & Kiểm thử (2 giai đoạn)
Quy trình này đảm bảo hệ thống không chỉ hoạt động mà còn đạt độ chính xác cao nhất:

1. **Vận hành thủ công (Ngày 2):** Khởi chạy Agent qua terminal để tương tác trực tiếp, nhập tên tool và dữ liệu để kiểm tra kết quả tức thì.
2. **Kiểm thử tự động (Ngày 3):** Sử dụng framework **Pytest** để thực hiện kiểm thử tự động, xác nhận độ ổn định của Tools, Agent và Memory đạt 100%.

### Phân loại các công cụ & Test Cases
| Thành phần | Chức năng / Mục đích Test | Đầu vào (Input) |
| :--- | :--- | :--- |
| **`uppercase`** | Chuyển văn bản thành chữ in hoa. | String |
| **`double`** | Nhân đôi giá trị đầu vào kèm xử lý lỗi. | Integer/String số |
| **`pytest`** | Xác nhận 4/4 test case báo PASSED. | Automation Script |

### Cấu trúc nâng cấp Ngày 3 (Memory & Test)
Trong Ngày 3, hệ thống được nâng cấp thêm khả năng ghi nhớ và bộ khung kiểm thử theo công thức:
`Hệ thống = [Agent Cơ bản] + [Cơ chế Memory (lưu context)] + [4 Test Cases quan trọng]`

* **Cơ chế Memory:** Agent sử dụng một danh sách `memory` để lưu trữ hành động. Kết quả của lần gọi trước được lưu lại để Agent có thể phản hồi câu hỏi "lúc nãy mày làm gì?".
* **Xử lý lỗi (Error Handling):** Tích hợp logic xử lý đầu vào cho `tool_double`. Nếu nhận văn bản thay vì số, hệ thống sẽ in thông báo rõ ràng thay vì dừng chương trình đột ngột.
* **4 Test Cases quan trọng:** Kiểm tra tính đúng đắn của `uppercase`, `double`, sự tồn tại của tool trong Agent và khả năng ghi nhớ của Memory.

---

### Nhật ký lỗi & Giải pháp (ERRORS_LOG)
Quá trình triển khai và nâng cấp ghi nhận các vấn đề trọng tâm sau:

* **Lỗi 1: ModuleNotFoundError (Lỗi đường dẫn):** Không tìm thấy module `src.spikes` do sai lệch cấu trúc repo.
    * **Giải pháp:** Loại bỏ các dòng import không cần thiết và định nghĩa trực tiếp cấu trúc Agent trong file thực thi.
* **Lỗi 2: KeyError / Tool Not Found:** Người dùng nhập dữ liệu trực tiếp vào ô yêu cầu tên công cụ.
    * **Giải pháp:** Tuân thủ đúng thứ tự nhập liệu (Tên tool trước). Cải tiến code hiển thị danh sách tool sẵn có.
* **Lỗi 3: ValueError (Ép kiểu dữ liệu):** Chương trình dừng đột ngột khi nhập chữ vào tool `double`.
    * **Giải pháp:** Sử dụng `try-except` hoặc kiểm tra đầu vào trước khi thực hiện tính toán số học.
* **Lỗi 4: Lỗi Import khi Test (Ngày 3):** Không tìm thấy `tool_double` trong file test do lấy nhầm source cũ.
    * **Giải pháp:** Đảm bảo sử dụng đúng file `agent_basic.py` phiên bản mới nhất từ folder I3.

### Tóm tắt ngắn (3-5 dòng cho team):
> **Agent Cơ bản & Memory** trong OpenFang đã hoàn thiện khả năng điều phối và ghi nhớ lịch sử hội thoại. Quy trình kiểm thử với Pytest đạt kết quả **4/4 PASSED**, xác nhận tính ổn định của hệ thống. Nhóm cần lưu ý việc sử dụng đúng tệp nguồn đồng nhất giữa các folder I1, I3 và I4 để tránh lỗi import trong quá trình tích hợp.

---
*Ghi chú bởi: I6 — Nguyễn Đang Trường | Cập nhật lần cuối: Ngày 3 — Thứ Tư*