# agent_second.py

def tool_summarize(text):
    """Tool tóm tắt đơn giản"""
    summary = str(text).split(".")[0]
    return summary


class Reviewer:
    def __init__(self):
        self.name = "Reviewer"
        self.description = "Receive processed text and summarize."

    def run(self, text):
        print("\n[Reviewer dang danh gia ket qua...]")

        summary = tool_summarize(text)

        print("Summary:", summary)

        return summary
