# test_agent.py
# I3: Viết test case 1, 2, 3
# I4 - Phạm Quốc Đạt: Thêm test case 4 về memory

import unittest
import sys
import os

# Thêm đường dẫn để import được agent_basic
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_basic import tool_uppercase, tool_double, Agent
from agent_memory import uppercase_tool, memory, Agent as MemoryAgent


class TestAgentTools(unittest.TestCase):

    # Test case 1 (I3): Kiểm tra tool_uppercase
    def test_tool_uppercase(self):
        result = tool_uppercase("hello")
        self.assertEqual(result, "HELLO")

    # Test case 2 (I3): Kiểm tra tool_double
    def test_tool_double(self):
        result = tool_double(5)
        self.assertEqual(result, 10)

    # Test case 3 (I3): Kiểm tra agent gọi được tool đúng
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
        # Kiểm tra agent có đủ 2 tool
        self.assertIn("uppercase", agent.tools)
        self.assertIn("double", agent.tools)

    # Test case 4 (I4): Kiểm tra agent nhớ được context (memory)
    def test_agent_memory(self):
        # Xóa memory trước khi test
        memory.clear()

        # Gọi uppercase_tool lần 1
        result1 = uppercase_tool("hello")
        self.assertEqual(result1, "HELLO")

        # Kiểm tra memory đã lưu hành động lần 1
        self.assertEqual(len(memory), 1)
        self.assertIn("hello", memory[0])
        self.assertIn("HELLO", memory[0])

        # Gọi uppercase_tool lần 2
        result2 = uppercase_tool("openfang")
        self.assertEqual(result2, "OPENFANG")

        # Kiểm tra memory nhớ cả 2 lần
        self.assertEqual(len(memory), 2)
        self.assertIn("openfang", memory[1])
        self.assertIn("OPENFANG", memory[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
