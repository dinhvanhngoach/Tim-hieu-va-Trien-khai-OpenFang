# main.py
# I3 - Pipeline 2 agent phối hợp
# Agent 1 (Processor): xử lý input bằng tool_uppercase hoặc tool_double
# Agent 2 (Reviewer):  nhận kết quả từ Agent 1 và tóm tắt

from agent_second import Reviewer

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
            result = self.tools[tool_name](input_data)
            print("Agent 1 output:", result)
            return result
        else:
            print("Khong tim thay tool")
            return None

# --- MAIN ---
if __name__ == "__main__":
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

    tool = input("Nhap tool (uppercase/double): ")
    user_input = input("Nhap du lieu: ")

    # Bước 1+2: Agent 1 xử lý
    output_agent1 = agent1.run(tool, user_input)

    # Nếu Agent 1 lỗi -> không gọi Reviewer
    if output_agent1 is None:
        print("Agent 1 gap loi hoac tool khong ton tai, KHONG goi Reviewer.")
    else:
        # Bước 3: Reviewer đánh giá kết quả
        reviewer.run(str(output_agent1))
