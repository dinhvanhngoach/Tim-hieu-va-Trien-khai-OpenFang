#agent 1 xử lý input và truyền kết quả sang Reviewer
#import Reviewer vào agent_basic.py và gọi nó sau khi Agent 1 xử lý xong
# agent_second.py
# agent_basic.py
from agent_second import Reviewer

# --- TOOL ---
def tool_uppercase(text):
    return text.upper()

def tool_double(number):
    return int(number) * 2

# --- AGENT 1 ---
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list

    def run(self, tool_name, input_data):

        print(f"\n[Agent {self.name} dang hoat dong...]")

        if tool_name in self.tools:

            result = self.tools[tool_name](input_data)

            print(f"Su dung cong cu: {tool_name}")
            print(f"Ket qua: {result}")

            return result

        else:
            print("Khong tim thay tool")
            return None

# --- MAIN ---
if __name__ == "__main__":

    danh_sach_tools = {
        "uppercase": tool_uppercase,
        "double": tool_double
    }
    agent1 = Agent(
        name="TextProcessor",
        description="Xu ly input bang tools",
        tools_list=danh_sach_tools
    )
    reviewer = Reviewer()
    tool = input("Nhap tool (uppercase / double): ")
    user_input = input("Nhap du lieu: ")

    # Agent 1 xử lý
    result = agent1.run(tool, user_input)

    # Agent 2 nhận kết quả
    reviewer.run(str(result))
