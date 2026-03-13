# agent_basic_I4.py
# I4 - Phạm Quốc Đạt
# Lấy code từ I1+I2+I3, gắn 2 tool, test và thêm nhập tay

#N
#Clone lại từ github nếu xung đột
#cd ~/Downloads
#git clone https://github.com/dinhvanhngoach/Tim-hieu-va-Trien-khai-OpenFang
#cd Tim-hieu-va-Trien-khai-OpenFang

# Để chắc chắn chạy code mới nhất từ GitHub thì chạy lần lượt 3 lệnh dưới:
#cd ~/Downloads/Tim-hieu-va-Trien-khai-OpenFang
#git pull origin main
#python openfang/I4/agent_basic_I4.py

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
        print(f"\n[Agent {self.name} dang chay...]")
        if tool_name in self.tools:
            try:
                result = self.tools[tool_name](input_data)
            except (TypeError, ValueError) as e:
                print(f"Tool su dung: {tool_name}")
                print("Loi: Du lieu dau vao khong hop le cho tool nay.")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return
            except Exception as e:
                print(f"Tool su dung: {tool_name}")
                print("Loi: Tool gap su co khong mong doi (agent khong bi crash).")
                print(f"Chi tiet loi: {type(e).__name__}: {e}")
                return
            print(f"Tool su dung: {tool_name}")
            print(f"Ket qua: {result}")
        else:
            print(f"Loi: khong tim thay cong cu '{tool_name}' trong he thong!")
            print(f"Cac tool co san: {list(self.tools.keys())}")

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":

    danh_sach_tools = {
        "uppercase": tool_uppercase,
        "double": tool_double
    }
    
    agent = Agent(
        name="TextProcessor",
        description="Agent xu ly van ban: chuyen chu hoa va nhan doi so.",
        tools_list=danh_sach_tools
    )

    # --- I4: TEST TỰ ĐỘNG VỚI CẢ 2 TOOL ---
    print("I4 - TEST TU DONG VOI 2 TOOL")
    
    # Test 1: Gọi tool_uppercase
    print("\n[TEST 1] Goi tool_uppercase:")
    agent.run("uppercase", "hello openfang")

    # Test 2: Gọi tool_double
    print("\n[TEST 2] Goi tool_double:")
    agent.run("double", 21)

    # Test 3: Đảm bảo agent không nhầm tool
    print("\n[TEST 3] Tool khong ton tai (kiem tra xu ly loi):")
    agent.run("unknown_tool", "test")

    print("\n[KET QUA] Agent phan biet dung 2 tool!")
    
    # --- PHẦN NHẬP TAY (như agent_basic.py của I2,I3) ---
    print("NHAP DU LIEU BANG TAY")
    tool = input("Chon tool (uppercase / double): ")
    user_input = input("Nhap du lieu: ")
    agent.run(tool, user_input)
