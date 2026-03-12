# agent_second.py

# Tool: tóm tắt text thành 1 câu
def tool_summarize(text):
    # lấy câu đầu tiên làm tóm tắt đơn giản
    summary = text.split(".")[0]
    return summary


# Agent Reviewer
class Reviewer:
    def __init__(self):
        self.name = "Reviewer"
        self.description = "Receive a text and give a short evaluation or summary."

    def run(self, text):
        print("Reviewer is analyzing the text...")

        summary = tool_summarize(text)

        print("Summary:", summary)
        return summary

# chạy thử agent
if __name__ == "__main__":

    agent = Reviewer()

    text = input("Enter text: ")

    agent.run(text)