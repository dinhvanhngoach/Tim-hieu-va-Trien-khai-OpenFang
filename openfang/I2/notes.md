# Vẽ sơ đồ kiến trúc OpenFang. Agent, Tool, Memory là gì

### Sơ đồ kiến trúc OpenFang (đơn giản)

Sơ đồ được xây dựng dựa trên **3 thành phần chính** theo yêu cầu:

#### 1. Agent (Hand)
Đơn vị tự hành (autonomous execution unit), chạy vòng lặp: quan sát → suy nghĩ bằng LLM → hành động (gọi tool) → lưu kết quả. Được kernel spawn và giám sát, có lifecycle riêng (Running, Suspended, Terminated).

#### 2. Tool / Skills

Các chức năng bên ngoài mà agent gọi được (function calling), hiện có 53+ built-in, chạy an toàn trong \*\*WASM sandbox\*\* để cách ly và bảo mật

---

#### 3. Memory

Cơ chế lưu trữ context dài hạn/ngắn hạn, dùng \*\*SQLite\*\* (lưu cấu trúc) + \*\*vector embeddings\*\* (tìm kiếm semantic) + knowledge graph, giúp agent nhớ thông tin giữa các lần chạy

---

### Mô tả sơ đồ kiến trúc

Trong sơ đồ:

Agent (Hand) ở trung tâm, kết nối trực tiếp với Tools (gọi và nhận kết quả)

Memory (lưu/đọc context), được Kernel spawn từ Input/Trigger.

---

### File đính kèm

Sơ đồ em vẽ: Agent (Hand) ở trung tâm, kết nối trực tiếp với Tools (gọi và nhận kết quả) và Memory (lưu/đọc context), được Kernel spawn từ Input/Trigger.

Đính kèm (trong folder openfang/I2):

\- architecture\_openfang.drawio (file gốc draw.io)

\- architecture\_openfang.png (ảnh sơ đồ)


