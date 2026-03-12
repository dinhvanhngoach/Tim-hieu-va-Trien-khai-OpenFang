import unittest
import os
import sys

# Thêm đường dẫn để import được agent_basic khi chạy từ thư mục khác
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_basic import tool_uppercase, tool_double, Agent

class TestAgentTools(unittest.TestCase):

    # Test case 1: kiểm tra tool_uppercase
    def test_tool_uppercase(self):
        result = tool_uppercase("hello")
        self.assertEqual(result, "HELLO")

    # Test case 2: kiểm tra tool_double
    def test_tool_double(self):
        result = tool_double(5)
        self.assertEqual(result, 10)

    # Test case 3: kiểm tra agent có gọi được tool
    def test_agent_run(self):
        tools = {
            "uppercase": tool_uppercase,
            "double": tool_double
        }
        agent = Agent(
            name="TestAgent",
            description="Agent test",
            tools_list=tools
        )
        self.assertIn("uppercase", agent.tools) 
        self.assertIn("double", agent.tools)

    # Test case 4: input sai kieu cho tool_double khong lam crash agent
    def test_agent_run_invalid_input_does_not_crash(self):
        tools = {
            "uppercase": tool_uppercase,
            "double": tool_double
        }
        agent = Agent(
            name="TestAgent",
            description="Agent test",
            tools_list=tools
        )
        # Neu Agent.run nem exception thi test se fail
        agent.run("double", "abc")
if __name__ == "__main__":
    unittest.main()
    
