Cập nhật agent_basic.py:

- Sử dụng dictionary để quản lý các tool.
- Agent nhận danh sách tool thông qua biến `tools_list`.
- Kiểm tra tool tồn tại trước khi gọi.
- Thêm thông báo lỗi khi tool không hợp lệ.
- Thêm phần `__main__` để test agent độc lập.

Cập nhật agent_secon.py:

1. Tạo tool `tool_summarize` để tóm tắt văn bản bằng cách lấy câu đầu tiên của đoạn text.
2. Xây dựng agent mới tên là `Reviewer` với nhiệm vụ nhận văn bản và đưa ra tóm tắt ngắn gọn.
3. Trong hàm `run`, agent gọi `tool_summarize` để xử lý nội dung đầu vào.
4. Thêm câu lệnh `return summary` để có thể sử dụng kết quả cho agent khác trong hệ thống.
5. Thêm khối `if __name__ == "__main__"` để có thể chạy và test agent độc lập.

Câpj nhật agent_memory.py

1. Tạo biến `memory` dạng list để lưu lại các hành động trước đó của agent.
2. Tạo tool `uppercase_tool` để chuyển chữ thường thành chữ hoa và lưu kết quả vào memory.
3. Khi tool được gọi, agent sẽ lưu thông tin dạng: "Converted 'text' to 'TEXT'".
4. Trong hàm `run`, agent kiểm tra nội dung message:
   - Nếu có từ khóa `uppercase` → gọi tool chuyển chữ hoa.
   - Nếu người dùng hỏi "lúc nãy mày làm gì" → agent đọc dữ liệu trong memory và trả lời hành động gần nhất.
5. Thêm vòng lặp `while True` để agent có thể nhận nhiều input liên tiếp.
6. Thêm xử lý `utf-8` cho `stdout` để tránh lỗi hiển thị tiếng Việt trong terminal.

Phần main.py đã chạy được lẫn từng agent riêng lẻ