# agent_basic.py

# --- PHẦN CỦA I2: ĐỊNH NGHĨA TOOL ---
def tool_uppercase(text):
    """Hàm chuyển văn bản thành chữ hoa"""
    return text.upper()

def tool_double(number):
    """Nhận vào 1 số nguyên và trả về số đó nhân đôi"""
    return int(number) * 2


# --- CẤU TRÚC AGENT (I1 & I2 PHỐI HỢP) ---
class Agent:
    def __init__(self, name, description, tools_list):
        self.name = name
        self.description = description
        self.tools = tools_list

    def run(self, tool_name, input_data):
        print(f"\n[Agent {self.name} dang hoat dong...]")
        if tool_name in self.tools:
            try:
                result = self.tools[tool_name](input_data)
            except (TypeError, ValueError) as e:
                print(f"Su dung cong cu: {tool_name}")
                print("Loi: Du lieu dau vao khong hop le cho tool nay.")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return
            except Exception as e:
                print(f"Su dung cong cu: {tool_name}")
                print("Loi: Tool gap su co khong mong doi (agent khong bi crash).")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return
            print(f"Su dung cong cu: {tool_name}")
            print(f"Ket qua cuoi cung: {result}")
        else:
            print(f"Loi khong tim thay cong cu '{tool_name}' trong he thong!")


# --- CHẠY THỬ ---
if __name__ == "__main__":

    danh_sach_tools = {
        "uppercase": tool_uppercase,
        "double": tool_double
    }

    agent = Agent(
        name="TextProcessor",
        description="Agent ho tro xu ly van ban bang cac cong cu co san.",
        tools_list=danh_sach_tools
    )

    tool = input("Nhap ten tool (uppercase / double): ")
    user_input = input("Nhap du lieu: ")

    agent.run(tool, user_input)
