# main.py
# I3 - Pipeline 2 agent phối hợp
# Agent 1 (Processor): xử lý input bằng tool_uppercase hoặc tool_double
# Agent 2 (Reviewer):  nhận kết quả từ Agent 1 và tóm tắt

from agent_second import Reviewer  # Reviewer định nghĩa trong agent_second.py (cùng folder)

# --- TOOLS ---
def tool_uppercase(text):
    return text.upper()

def tool_double(number):
    return int(number) * 2

# --- AGENT 1: Processor ---
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list

    def run(self, tool_name, input_data):
        print(f"\n[Agent {self.name} dang xu ly input...]")
        if tool_name in self.tools:
            try:
                result = self.tools[tool_name](input_data)
            except (TypeError, ValueError) as e:
                print("Loi: Du lieu dau vao khong hop le cho tool nay.")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return None
            except Exception as e:
                print("Loi: Agent 1 gap su co khong mong doi.")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return None
            print("Agent 1 output:", result)
            return result
        else:
            print("Khong tim thay tool")
            return None

# --- MAIN PIPELINE (tách thành hàm để test end-to-end) ---
def run_pipeline(tool_name: str, user_input: str):
    tools = {
        "uppercase": tool_uppercase,
        "double": tool_double
    }

    agent1 = Agent(
        name="Processor",
        description="Xu ly input bang tools",
        tools_list=tools
    )
    reviewer = Reviewer()

    # Bước 1+2: Agent 1 xử lý
    output_agent1 = agent1.run(tool_name, user_input)

    # Nếu Agent 1 lỗi hoặc không tìm thấy tool -> không gọi Reviewer
    if output_agent1 is None:
        print("Agent 1 gap loi hoac tool khong ton tai, KHONG goi Reviewer.")
        return None, None

    # Bước 3: Reviewer đánh giá kết quả (chuyển sang string phòng trường hợp output là số)
    summary = reviewer.run(str(output_agent1))
    return output_agent1, summary


if __name__ == "__main__":
    # Bước 1: user nhập input
    tool = input("Nhap tool (uppercase/double): ")
    user_input = input("Nhap du lieu: ")

    # Chạy pipeline đầy đủ
    output_agent1, summary = run_pipeline(tool, user_input)
