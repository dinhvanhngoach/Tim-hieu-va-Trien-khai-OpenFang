#agent 1 xử lý input và truyền kết quả sang Reviewer
#import Reviewer vào agent_basic.py và gọi nó sau khi Agent 1 xử lý xong
# agent_second.py ( I1 ) 
# agent_basic.py ( I3 )

# agent_basic.py

from agent_second import Reviewer

# --- TOOLS ---
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
        print(f"\n[Agent {self.name} dang xu ly input...]")
        if tool_name in self.tools:
            result = self.tools[tool_name](input_data)
            print("Tool duoc su dung:", tool_name)
            print("Ket qua sau khi xu ly:", result)
            return result
        else:
            print("Khong tim thay tool")
            return None

# --- MAIN PIPELINE ---
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
    # bước 1: user input
    tool = input("Nhap tool (uppercase/double): ")
    user_input = input("Nhap du lieu: ")

    # bước 2: Agent1 xử lý
    processed_result = agent1.run(tool, user_input)

    # bước 3: Reviewer nhận kết quả
    reviewer.run(processed_result)
    
#in ra màn hình Agent 1 output là gì, Review nói gì về output đó
# agent_basic.py
from agent_second import Reviewer

# --- TOOLS ---
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

    # Agent 1 xử lý
    output_agent1 = agent1.run(tool, user_input)

    # Reviewer đánh giá
    reviewer.run(output_agent1)
