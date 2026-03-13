
# [DOCS] CHI TIẾT KIỂM THỬ VÀ HƯỚNG DẪN CHẠY

## 1. Hệ thống Kiểm thử Tự động (Automated Testing)

Hệ thống sử dụng **Pytest** để đảm bảo tính ổn định với 8/8 Test Cases đạt trạng thái **PASSED**.

### 1.1 Danh mục các bài Test

| Tên bài Test | Thành phần kiểm tra | Mục tiêu |
| --- | --- | --- |
| `test_tool_uppercase` | Tool Uppercase | Xác nhận chuỗi đầu vào được chuyển thành chữ in hoa chính xác. |
| `test_tool_double` | Tool Double | Xác nhận phép nhân đôi số nguyên hoạt động đúng logic. |
| `test_agent_run` | Class Agent | Kiểm tra Agent có nhận diện và gọi đúng Tool từ Dictionary không. |
| `test_agent_memory` | Memory System | Xác nhận hành động được lưu vào list và truy xuất đúng lịch sử. |
| `test_tool_summarize` | Reviewer Agent | Kiểm tra logic tách chuỗi lấy câu đầu tiên để tóm tắt. |
| `test_main_pipeline` | Multi-Agent Workflow | Xác nhận dữ liệu truyền từ Agent 1 sang Agent 2 không bị ngắt quãng. |

---

## 3. Hướng dẫn chạy Kiểm thử (How-to-run Test)

Bạn thực hiện lệnh theo thứ tự sau:

1. **Cài đặt môi trường test:**
```bash
pip install pytest

```


2. **Chạy test cho Agent & Memory:**
```bash
pytest openfang/I4/test_agent.py -v

```


3. **Chạy test cho Reviewer:**
```bash
pytest openfang/I4/test_reviewer.py -v

```


4. **Chạy test tích hợp toàn hệ thống:**
```bash
python -m unittest -v openfang.I5.test_main_pipeline

```



---


