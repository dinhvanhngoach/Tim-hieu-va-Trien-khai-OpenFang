# agent_memory.py

# Memory để lưu hành động trước đó
memory = []

# Tool: chuyển chữ thường sang chữ hoa
def uppercase_tool(text):
    result = text.upper()
    memory.append(f"Converted '{text}' to '{result}'")
    return result


# Agent
class Agent:
    def __init__(self, name):
        self.name = name

    def run(self, message):

        # Nếu yêu cầu uppercase
        if "uppercase" in message:
            word = message.split()[-1]
            result = uppercase_tool(word)
            print("Result:", result)

        # Nếu hỏi agent đã làm gì trước đó
        elif "lúc nãy mày làm gì" in message or "luc nay may lam gi" in message:
            if memory:
                print("Memory:", memory[-1])
            else:
                print("Chua co hanh dong nao truoc do.")

        else:
            print("Khong hieu yeu cau. Thu: 'uppercase <tu>' hoac 'luc nay may lam gi'")



# Chạy agent
if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    agent = Agent("MemoryAgent")

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            break

        agent.run(user_input)