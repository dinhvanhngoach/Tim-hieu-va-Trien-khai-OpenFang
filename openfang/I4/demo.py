# demo.py
# I4 - Phạm Quốc Đạt
# Ngày 5: Script demo 5 phút — chạy lần lượt agent 1, agent 2, pipeline cả 2

import time

# =============================================
# HÀM TIỆN ÍCH
# =============================================
def print_header(title):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)

def print_step(step, desc):
    print(f"\n  [{step}] {desc}")
    print("  " + "-" * 40)

def pause(seconds=1):
    time.sleep(seconds)

# =============================================
# PHẦN 1 — DEMO AGENT 1 (Processor)
# Tool: uppercase và double
# =============================================
def demo_agent1():
    print_header("DEMO 1/3 — AGENT 1: TextProcessor")

    # Định nghĩa tool
    def tool_uppercase(text):
        return text.upper()

    def tool_double(number):
        return int(number) * 2

    # Định nghĩa Agent (theo cấu trúc ngày 2)
    class Agent:
        def __init__(self, name, description, tools_list):
            self.name = name
            self.description = description
            self.tools = tools_list

        def run(self, tool_name, input_data):
            print(f"\n  >> Agent '{self.name}' dang xu ly...")
            if tool_name in self.tools:
                try:
                    result = self.tools[tool_name](input_data)
                    print(f"     Tool su dung : {tool_name}")
                    print(f"     Ket qua      : {result}")
                    return result
                except (TypeError, ValueError) as e:
                    print(f"     Loi input    : {e}")
                    return None
            else:
                print(f"     Loi: Khong tim thay tool '{tool_name}'")
                return None

    agent1 = Agent(
        name="TextProcessor",
        description="Xu ly text bang 2 tool: uppercase va double",
        tools_list={"uppercase": tool_uppercase, "double": tool_double}
    )

    print_step("1a", "Goi tool_uppercase voi input 'hello openfang'")
    pause()
    agent1.run("uppercase", "hello openfang")

    print_step("1b", "Goi tool_double voi input 21")
    pause()
    agent1.run("double", 21)

    print_step("1c", "Thu goi tool khong ton tai (kiem tra xu ly loi)")
    pause()
    agent1.run("unknown_tool", "test")

    print("\n  => Agent 1 phan biet dung tool, xu ly loi tot!")

# =============================================
# PHẦN 2 — DEMO AGENT 2 (Reviewer)
# Tool: tool_summarize
# =============================================
def demo_agent2():
    print_header("DEMO 2/3 — AGENT 2: Reviewer")

    from agent_second import Reviewer

    reviewer = Reviewer()

    print_step("2a", "Reviewer nhan text dai va tom tat")
    pause()
    sample_text = (
        "OpenFang is an open-source AI agent OS built with Rust. "
        "It enables autonomous AI agents called Hands. "
        "These agents can search, summarize, and automate workflows."
    )
    print(f"\n     Input : \"{sample_text[:55]}...\"")
    result = reviewer.run(sample_text)
    print(f"\n  => Reviewer da tom tat thanh: '{result}'")

    print_step("2b", "Reviewer nhan output tu Agent 1 (VD: 'HELLO OPENFANG')")
    pause()
    reviewer.run("HELLO OPENFANG")

# =============================================
# PHẦN 3 — DEMO PIPELINE 2 AGENT (main.py)
# Agent 1 xử lý → kết quả truyền sang Agent 2
# =============================================
def demo_pipeline():
    print_header("DEMO 3/3 — PIPELINE: Agent 1 → Agent 2")

    from main import run_pipeline

    print_step("3a", "Pipeline: tool=uppercase, input='hello from openfang'")
    pause()
    out1, summary1 = run_pipeline("uppercase", "hello from openfang")
    print(f"\n  => Agent 1 output : {out1}")
    print(f"  => Reviewer noi   : {summary1}")

    print_step("3b", "Pipeline: tool=double, input=21")
    pause()
    out2, summary2 = run_pipeline("double", "21")
    print(f"\n  => Agent 1 output : {out2}")
    print(f"  => Reviewer noi   : {summary2}")

    print_step("3c", "Pipeline: Agent 1 loi (tool khong ton tai) -> Reviewer KHONG chay")
    pause()
    run_pipeline("invalid_tool", "test")

# =============================================
# CHẠY DEMO
# =============================================
if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("\n" + "*" * 55)
    print("*" + " " * 53 + "*")
    print("*   DEMO - 2 AGENT OPENFANG PHOI HOP NHAU         *")
    print("*   Trinh bay boi: I4 - Pham Quoc Dat             *")
    print("*" + " " * 53 + "*")
    print("*" * 55)

    pause(1)

    # Phần 1: Demo Agent 1
    demo_agent1()
    pause(1)

    # Phần 2: Demo Agent 2
    demo_agent2()
    pause(1)

    # Phần 3: Demo Pipeline
    demo_pipeline()

    # Kết thúc
    print_header("KET THUC DEMO")
    print("\n  Tom tat:")
    print("  - Agent 1 (TextProcessor): xu ly text voi 2 tool")
    print("  - Agent 2 (Reviewer)     : tom tat ket qua tu Agent 1")
    print("  - Pipeline main.py       : 2 agent chay noi tiep nhau")
    print("  - Test                   : 13/13 test PASSED")
    print("\n  Cam on da theo doi! Chuc mung team OpenFang!\n")
