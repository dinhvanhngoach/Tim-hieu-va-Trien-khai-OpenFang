# tool_double.py
# I3 - Viết tool thứ 2: nhận vào 1 số nguyên, trả về số đó nhân đôi

def tool_double(number):
    """Nhận vào 1 số nguyên và trả về số đó nhân đôi"""
    return int(number) * 2


# Test thử tool
if __name__ == "__main__":
    print(tool_double(5))   # 10
    print(tool_double(21))  # 42