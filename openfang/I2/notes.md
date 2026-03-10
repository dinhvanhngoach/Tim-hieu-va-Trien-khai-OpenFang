\## Ngày 1 - I2 (Tô Việt Thường)



\### OpenFang là gì?

OpenFang là một \*\*Agent Operating System\*\* mã nguồn mở viết bằng Rust (chạy dưới dạng single binary), cho phép triển khai và chạy các agent tự hành (autonomous agents) liên tục 24/7 theo lịch trình. Nó khác với các framework như LangChain hay CrewAI vì là một hệ điều hành thực thụ với kernel, scheduler, bảo mật WASM sandbox, và hỗ trợ nhiều LLM provider.



\### Sơ đồ kiến trúc OpenFang đơn giản

Em vẽ sơ đồ tập trung vào 3 thành phần chính theo yêu cầu:

\- \*\*Agent (Hand)\*\*: Đơn vị tự hành (autonomous execution unit), chạy vòng lặp: quan sát → suy nghĩ bằng LLM → hành động (gọi tool) → lưu kết quả. Được kernel spawn và giám sát, có lifecycle riêng (Running, Suspended, Terminated).

\- \*\*Tool / Skills\*\*: Các chức năng bên ngoài mà agent gọi được (function calling), hiện có 53+ built-in, chạy an toàn trong \*\*WASM sandbox\*\* để cách ly và bảo mật.

\- \*\*Memory\*\*: Cơ chế lưu trữ context dài hạn/ngắn hạn, dùng \*\*SQLite\*\* (lưu cấu trúc) + \*\*vector embeddings\*\* (tìm kiếm semantic) + knowledge graph, giúp agent nhớ thông tin giữa các lần chạy.



Sơ đồ em vẽ: Agent (Hand) ở trung tâm, kết nối trực tiếp với Tools (gọi và nhận kết quả) và Memory (lưu/đọc context), được Kernel spawn từ Input/Trigger.



Đính kèm (trong folder openfang/I2):

\- architecture\_openfang.drawio (file gốc draw.io)

\- architecture\_openfang.png (ảnh sơ đồ)


