# I6 — Nguyễn Đang Trường — Ghi chú về Memory trong OpenFang

### Memory trong OpenFang là gì?
Trong hệ sinh thái OpenFang, Memory không chỉ đơn thuần là việc lưu lại lịch sử trò chuyện mà là một **hệ thống quản lý tri thức đa tầng**. Vì các mô hình ngôn ngữ lớn (LLM) vốn dĩ không có trí nhớ tự thân (stateless), OpenFang sử dụng kiến trúc **Bộ nhớ ngoài (External Memory)** để giúp Agent có khả năng ghi nhớ dài hạn và hiểu ngữ cảnh sâu sắc.

Cơ chế này giúp Agent vượt qua giới hạn về "cửa sổ ngữ cảnh" (context window) của mô hình AI, đảm bảo sự liên tục và chính xác của thông tin xuyên suốt các lần gọi.

### Quy trình hoạt động của Memory (4 bước chính)
Quy trình này hoạt động khép kín để đảm bảo Agent luôn có đủ thông tin cần thiết:

1. **Lưu trữ hội thoại (Persistence):** Ghi lại toàn bộ nội dung tương tác vào hệ thống lưu trữ bền vững, thường là **SQLite**. Dữ liệu được tổ chức theo từng **Session** (phiên làm việc) để phân biệt các cuộc hội thoại khác nhau.
2. **Mã hóa ngữ nghĩa (Semantic Memory):** Để tránh gây tràn bộ nhớ LLM, Agent thực hiện "nén ý nghĩa" bằng cách chuyển các đoạn hội thoại quan trọng thành **Vector Embeddings** và lưu vào **Vector Database**.
3. **Truy xuất & Tái dựng (Retrieval & Reconstruction):** Khi có câu hỏi mới, Agent "hồi tưởng" theo hai hướng: lấy các tin nhắn gần nhất (ngắn hạn) và tìm kiếm ký ức liên quan trong Vector DB (dài hạn).
4. **Nhắc bài cho LLM (Context Injection):** Agent tổng hợp dữ liệu và soạn thành một bản hướng dẫn (Prompt) đầy đủ gửi cho LLM.



### Phân loại các tầng lưu trữ
| Thành phần | Công nghệ | Mục đích chính |
| :--- | :--- | :--- |
| **Truy xuất ngắn hạn** | SQLite / Session | Duy trì mạch hội thoại tức thì (5-10 câu gần nhất). |
| **Truy xuất dài hạn** | Vector Database | Tìm kiếm lại thông tin cũ dựa trên ý nghĩa (Semantic Search). |
| **Persistence** | SQLite | Đảm bảo lịch sử không bị mất khi hệ thống khởi động lại. |

### Cấu trúc bản "Nhắc bài" (Context Injection)
Để LLM có thể trả lời chính xác, Agent sẽ tự động soạn thảo Prompt theo công thức:
`Prompt = [Chỉ thị hệ thống] + [Các tin nhắn gần đây] + [Ký ức cũ liên quan] + [Câu hỏi hiện tại]`

### Tại sao cần Semantic Memory?
Khác với tìm kiếm từ khóa thông thường, **Semantic Memory** cho phép Agent tìm lại thông tin dựa trên **ý nghĩa ngữ cảnh**. Điều này giúp Agent có "bộ nhớ dài hạn", hiểu được sở thích hoặc các dữ liệu quan trọng bạn đã đề cập từ rất lâu trong quá khứ.

### Tóm tắt ngắn (3-5 dòng cho team):
> **Memory** trong OpenFang là kiến trúc bộ nhớ ngoài giúp Agent duy trì ngữ cảnh bằng cách lưu lịch sử vào SQLite và mã hóa ý nghĩa thành Vector Embeddings. Khi nhận yêu cầu, Agent sẽ truy xuất tin nhắn gần nhất cùng các "ký ức" liên quan để tái dựng ngữ cảnh và "nhắc bài" vào prompt cho LLM. Cơ chế này đảm bảo sự liên tục, chính xác và giúp Agent vượt qua giới hạn bộ nhớ của mô hình AI.

---
*Ghi chú bởi: I6 — Nguyễn Đang Trường | Ngày 1 — Thứ Hai*