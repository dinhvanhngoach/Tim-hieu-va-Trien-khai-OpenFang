# Báo cáo tìm hiểu: Agency Agents

> **Nguồn:** https://github.com/msitarzewski/agency-agents  
> **Ngày báo cáo:** 17/03/2026  
> **License:** MIT | **Stars:** ~4.1k+ | **Forks:** ~685+

---

## 1. Tổng quan

**Agency Agents** là một bộ sưu tập các AI agent personalities được thiết kế thủ công kỹ lưỡng — mỗi agent là một chuyên gia AI với cá tính riêng, quy trình làm việc cụ thể và deliverables đo lường được.

> **Ý tưởng cốt lõi:** Thay vì dùng một AI generic cho mọi việc, bạn lắp ráp một "dream team" gồm các chuyên gia AI không bao giờ ngủ, không bao giờ phàn nàn và luôn deliver kết quả.

**Xuất phát điểm:** Project được sinh ra từ một thread trên Reddit và qua nhiều tháng lặp đi lặp lại cải tiến.

---

## 2. Đặc điểm của mỗi Agent

Mỗi agent trong bộ sưu tập đều có 4 thuộc tính:

| Thuộc tính | Mô tả |
|---|---|
| **Specialized** | Chuyên môn sâu trong lĩnh vực của họ, không phải template prompt generic |
| **Personality-Driven** | Có giọng nói riêng, phong cách giao tiếp và cách tiếp cận đặc trưng |
| **Deliverable-Focused** | Tạo ra code thực, quy trình thực và kết quả đo lường được |
| **Production-Ready** | Workflows đã được battle-tested với success metrics cụ thể |

---

## 3. Cấu trúc thư mục — Các bộ phận trong Agency

```
agency-agents/
├── engineering/          # Kỹ thuật & lập trình
├── design/               # Thiết kế
├── marketing/            # Marketing & tăng trưởng
├── product/              # Quản lý sản phẩm
├── sales/                # Bán hàng
├── strategy/             # Chiến lược (có playbooks, runbooks, coordination)
├── project-management/   # Quản lý dự án
├── support/              # Hỗ trợ khách hàng
├── testing/              # Kiểm thử
├── integrations/         # Tích hợp công cụ
├── paid-media/           # Quảng cáo trả phí
├── game-development/     # Phát triển game
├── spatial-computing/    # Spatial computing
├── specialized/          # Các agent đặc biệt
├── examples/             # Ví dụ sử dụng
└── scripts/              # Script tự động cài đặt
```

---

## 4. Danh sách Agent theo từng bộ phận

### 💻 Engineering Division

| Agent | Chuyên môn | Khi nào dùng |
|---|---|---|
| Frontend Developer | React/Vue/Angular, UI, Core Web Vitals | Web app hiện đại, UI pixel-perfect |
| Backend Architect | API design, database, scalability | Server-side, microservices, cloud |
| Mobile App Builder | iOS/Android, React Native, Flutter | App native và cross-platform |
| Senior Developer | Code review, mentoring, architecture | Cần tư vấn senior, refactor code |
| AI Engineer | LLM integration, ML pipelines | Tích hợp AI vào sản phẩm |
| DevOps Automator | CI/CD, Docker, infrastructure | Tự động hóa deployment |
| Rapid Prototyper | MVP nhanh, proof of concept | Cần thử nghiệm ý tưởng nhanh |

### 🎨 Design Division
Các agent chuyên về UI/UX, visual design, brand identity.

### 📣 Marketing Division

| Agent | Chuyên môn |
|---|---|
| Content Creator | Tạo nội dung đa dạng kênh |
| Growth Hacker | Tăng trưởng người dùng, viral tactics |
| Social Media Strategist | Chiến lược mạng xã hội |
| Instagram Curator | Nội dung và tăng trưởng Instagram |
| Reddit Community Builder | Xây dựng cộng đồng trên Reddit |
| App Store Optimizer | ASO cho iOS và Android |

### 📦 Product Division
Agents quản lý product roadmap, user research, feature prioritization.

### 💼 Sales Division
Agents chuyên về lead generation, outreach, closing deals.

### 🧠 Strategy Division
Có 3 loại tài liệu chiến lược:
- **Playbooks** — kịch bản xử lý từng tình huống cụ thể
- **Runbooks** — quy trình vận hành step-by-step
- **Coordination** — phối hợp giữa nhiều agents

### Các bộ phận khác
- **Project Management** — Sprint planning, task tracking
- **Support** — Customer support chuyên nghiệp
- **Testing** — QA, test automation
- **Game Development** — Game design, mechanics
- **Spatial Computing** — AR/VR development
- **Specialized** — Các agent đặc biệt (reality checker, whimsy injector...)

---

## 5. Cách sử dụng

### Option 1 — Dùng với Claude Code (Khuyến nghị nhất)

```bash
# Copy toàn bộ agents vào thư mục Claude Code
cp -r agency-agents/* ~/.claude/agents/

# Kích hoạt agent trong session Claude Code
# "Hey Claude, activate Frontend Developer mode and help me build a React component"
```

### Option 2 — Dùng làm tài liệu tham khảo

Mỗi file agent chứa:
- Identity & personality traits
- Core mission & workflows
- Technical deliverables kèm code examples
- Success metrics & communication style

Chỉ cần browse, copy và adapt agent phù hợp với nhu cầu.

### Option 3 — Tích hợp với các tool khác

```bash
# Bước 1: Generate integration files cho tất cả tool hỗ trợ
./scripts/convert.sh

# Bước 2: Cài đặt tự động (auto-detect tool đã cài)
./scripts/install.sh

# Hoặc target tool cụ thể
./scripts/install.sh --tool cursor
./scripts/install.sh --tool copilot
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
```

**Các tool được hỗ trợ:** Claude Code, Cursor, GitHub Copilot, Aider, Windsurf, Gemini CLI, OpenCode.

---

## 6. Cách mỗi Agent file được cấu trúc

Mỗi file `.md` trong repo là một "persona card" gồm:

```markdown
## Identity
[Tên, vai trò, personality traits]

## Core Mission
[Mục tiêu chính của agent này]

## Workflows
[Quy trình làm việc step-by-step]

## Deliverables
[Output cụ thể: code, documents, reports]

## Success Metrics
[Cách đo lường kết quả]

## Communication Style
[Cách agent giao tiếp, tone of voice]
```

---

## 7. Điểm mạnh nổi bật

- **Không cần cài đặt phức tạp** — chỉ copy file `.md` là dùng được
- **Hoạt động với nhiều AI tool** — Claude, Cursor, Copilot, Aider, Windsurf...
- **Mã nguồn mở MIT** — tự do sử dụng, chỉnh sửa, đóng góp
- **Cộng đồng đang phát triển** — PRs welcome, 142+ commits
- **Strategy layer đầy đủ** — có cả playbooks, runbooks cho quy trình vận hành
- **Có scripts tự động** — `convert.sh` và `install.sh` giúp setup nhanh

---

## 8. So sánh với các project đã tìm hiểu

| | Agency Agents | Always-On Memory Agent | OpenFang Clip Hand |
|---|---|---|---|
| Mục đích | Bộ AI specialists cho mọi lĩnh vực | Bộ nhớ AI liên tục 24/7 | Tạo short video clips |
| Nền tảng | Markdown files (tool-agnostic) | Python + Google ADK | Rust + OpenFang |
| Cần cài đặt | ❌ Không | ✅ Cần Python + API key | ✅ Cần nhiều dependencies |
| AI Model | Bất kỳ (Claude, GPT, Gemini...) | Gemini Flash-Lite | Groq / llama |
| Use case | Workflow cá nhân & team | Knowledge management | Content production |
| Phù hợp với | Mọi người dùng AI | Developer/researcher | Content creator |

---

## 9. Tóm tắt nhanh

| Hạng mục | Thông tin |
|---|---|
| Repo | msitarzewski/agency-agents |
| License | MIT (miễn phí hoàn toàn) |
| Ngôn ngữ | Markdown (không cần code) |
| Số bộ phận | 14+ divisions |
| Tool tương thích | Claude Code, Cursor, Copilot, Aider, Windsurf, Gemini CLI |
| Cần API key | Tùy tool AI bạn dùng |
| Đóng góp | PRs welcome |

---

*Báo cáo được tổng hợp ngày 17/03/2026*
