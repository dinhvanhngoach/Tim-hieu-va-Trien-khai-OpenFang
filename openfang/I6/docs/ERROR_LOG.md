
# [DOCS] XỬ LÝ LỖI HỆ THỐNG 

## 1. Bảng tổng hợp Lỗi, Nguyên nhân và Giải pháp

Đây là bảng chi tiết tất cả các vấn đề phát sinh khi làm và giải pháp.

### Bảng Nhật ký lỗi (Errors Log Full)

| Tên Lỗi | Nguyên nhân thực tế | Giải pháp triển khai |
| --- | --- | --- |
| **ModuleNotFoundError** (Lỗi đường dẫn) | Cấu trúc repo thực tế không khớp với tài liệu mẫu của framework OpenFang (thiếu `src.spikes`). | Loại bỏ các dòng import phụ thuộc không cần thiết; định nghĩa trực tiếp cấu trúc Agent/Tool bên trong file thực thi. |
| **KeyError / Tool Not Found** | Người dùng nhập tên tool sai chính tả hoặc nhập dữ liệu vào ô yêu cầu tên công cụ. | Sử dụng cơ chế kiểm tra `if tool_name in self.tools` và in ra danh sách tool hợp lệ để hướng dẫn người dùng. |
| **ValueError** (Lỗi ép kiểu) | Nhập ký tự chữ vào tool `double` khiến hàm `int()` bị crash đột ngột. | Bọc logic xử lý trong khối `try-except` để bắt lỗi và in thông báo hướng dẫn thay vì dừng chương trình. |
| **NameError** (Biến chưa định nghĩa) | Kết quả của Agent 1 không được gán vào biến trước khi truyền sang cho Reviewer. | Đảm bảo biến `output_agent1` được khởi tạo và nhận giá trị từ phương thức `run()` của Agent 1. |
| **TypeError** (Sai định dạng) | Agent 2 (Reviewer) không đọc được kết quả nếu Agent 1 trả về kiểu dữ liệu số (`int`). | Sử dụng hàm `str()` để đồng nhất mọi kết quả đầu ra của Agent 1 về dạng văn bản trước khi truyền qua Pipeline. |
| **Logic Halt** (Ngắt luồng) | Pipeline vẫn tiếp tục gọi Agent 2 ngay cả khi Agent 1 thực hiện lỗi (trả về `None`). | Thêm kiểm tra điều kiện `if output_agent1:` trước khi gọi Agent 2 để bảo vệ hệ thống khỏi dữ liệu lỗi. |
| **Import Error (Test)** | File test gọi nhầm source code cũ từ các folder I1, I2 chưa cập nhật tính năng mới. | Đảm bảo sử dụng đường dẫn tệp nguồn đồng nhất (thường là từ folder I3 hoặc I4) khi thực hiện lệnh chạy test. |

---
