# Báo cáo tìm hiểu: OpenFang — Clip Hand

---

## 1. Tổng quan về OpenFang

OpenFang là một hệ điều hành agent (Agent OS) hiệu năng cao, mã nguồn mở, được xây dựng hoàn toàn bằng Rust. Điểm khác biệt cốt lõi: thay vì chờ người dùng ra lệnh như chatbot thông thường, OpenFang chạy các agent tự động 24/7 theo lịch, xây dựng knowledge graph, và báo cáo kết quả về dashboard.

---

## 2. Clip Hand là gì?

**Clip Hand** là một trong các "Hands" (tác nhân tự động) của OpenFang, chuyên biến video dài thành các short clip viral thông qua một pipeline 8 giai đoạn hoàn toàn tự động.

> Phù hợp cho các nhóm vận hành kênh short video — có thể tạo ra tới **50 video mỗi ngày** mà không cần tăng nhân sự tương ứng.

---

## 3. Pipeline 8 giai đoạn

| # | Giai đoạn | Mô tả | Công cụ |
|---|-----------|--------|---------|
| 1 | **Tải nguồn video** | Tải từ YouTube, Vimeo, Twitter, 1000+ nguồn | yt-dlp |
| 2 | **Phát hiện highlight** | AI phân tích metadata, âm thanh, nội dung để tìm khoảnh khắc nổi bật | AI + ffprobe |
| 3 | **Cắt clip** | Trích xuất đoạn video tốt nhất | FFmpeg |
| 4 | **Crop dọc (vertical)** | Chuyển sang tỷ lệ 9:16 cho TikTok/Reels/Shorts | FFmpeg |
| 5 | **Tạo phụ đề** | 5 STT backends chuyển giọng nói thành văn bản, burn vào video | 5 STT backends |
| 6 | **Tạo thumbnail** | AI chọn frame đẹp nhất, tạo ảnh bìa hấp dẫn | AI |
| 7 | **Chấm điểm chất lượng** | AI voiceover tuỳ chọn + scoring để chọn clip tốt nhất | AI scoring |
| 8 | **Xuất & đăng tự động** | Batch export, tự động đăng lên 40+ kênh | 40 channel adapters |

---

## 4. Dependencies cần cài đặt

Clip Hand yêu cầu 3 công cụ bên ngoài:

### 4.1 FFmpeg *(2–5 phút cài đặt)*
- **Chức năng:** Xử lý toàn bộ video — cắt clip, thêm phụ đề, crop dọc, tạo thumbnail.
- **Windows:** `winget install Gyan.FFmpeg`
- **macOS:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`

### 4.2 FFprobe *(đi kèm FFmpeg)*
- **Chức năng:** Phân tích metadata video như codec, độ phân giải, thời lượng, bitrate.
- Không cần cài riêng — được tích hợp sẵn khi cài FFmpeg.

### 4.3 yt-dlp *(1–2 phút cài đặt)*
- **Chức năng:** Tải video từ YouTube, Vimeo, Twitter và hơn 1000 trang khác. Cũng lấy phụ đề có sẵn để bỏ qua bước STT nếu có.
- **Windows:** `winget install yt-dlp.yt-dlp`
- **macOS:** `brew install yt-dlp`
- **Linux:** `pip install yt-dlp`

---

## 5. Ứng dụng thực tế

- Tự động chỉnh sửa video dài từ nhiều nguồn
- Tạo clip dọc 9:16 sẵn sàng đăng lên TikTok, Instagram Reels, YouTube Shorts
- Tự động thêm phụ đề và thumbnail hấp dẫn
- Lên lịch và đăng bài tự động lên Telegram, WhatsApp và 38 kênh khác
- Có thể tạo tới 50 video/ngày không cần can thiệp thủ công

---

## 6. Tóm tắt

| Hạng mục | Thông tin |
|----------|-----------|
| Loại | Autonomous Hand (agent tự động) |
| Chức năng | Biến video dài → short clips viral |
| Pipeline | 8 giai đoạn |
| Công cụ cốt lõi | FFmpeg + yt-dlp + 5 STT backends |
| Đầu ra | Clip dọc 9:16 + phụ đề + thumbnail |
| Đăng tự động | Telegram, WhatsApp và 38 kênh khác |
| Nền tảng | OpenFang (Rust, mã nguồn mở) |

---

*Báo cáo được tổng hợp ngày 17/03/2026*
