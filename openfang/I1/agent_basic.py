# agent_basic.py

# --- PHẦN CỦA I2: ĐỊNH NGHĨA TOOL ---
def tool_uppercase(text):
    """Hàm chuyển văn bản thành chữ hoa"""
    return text.upper()

# --- CẤU TRÚC AGENT (I1 & I2 PHỐI HỢP) ---
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list  # I2: Agent giờ nắm giữ một danh sách tool

    def run(self, tool_name, input_data):
        print(f"\n[Agent {self.name} dang hoat dong...]")
        # Kiểm tra xem tool có trong danh sách không
        if tool_name in self.tools:
            result = self.tools[tool_name](input_data)
            print(f"Su dung cong cu: {tool_name}")
            print(f"Ket qua cuoi cung: {result}")
        else:
            print(f"Loi khong tim thay cong cu'{tool_name}' trong he thong!")

# --- CHẠY THỬ (I2 KIỂM TRA) ---
if __name__ == "__main__":
    # Đăng ký tool của bạn vào đây
    # Sau này I3, I4 chỉ cần thêm dòng mới vào dict này là xong
    danh_sach_tools = {
        "uppercase": tool_uppercase
    }

    agent = Agent(
        name="TextProcessor",
        description="Agent ho tro xu ly van ban bang cac cong cu co san.",
        tools_list=danh_sach_tools
    )

    # Test thử tool uppercase của I2
    user_input = input("Nhap noi dung can xu ly: ")
    agent.run("uppercase", user_input)