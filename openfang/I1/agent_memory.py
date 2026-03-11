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
        elif "lúc nãy" in message:
            if memory:
                print("Memory:", memory[-1])
            else:
                print("Chưa có hành động nào trước đó.")

        else:
            print("Không hiểu yêu cầu.")


# Chạy agent
if __name__ == "__main__":

    agent = Agent("MemoryAgent")

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            break

        agent.run(user_input)