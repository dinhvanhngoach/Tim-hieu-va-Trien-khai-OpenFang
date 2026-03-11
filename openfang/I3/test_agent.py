import unittest
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
        result = agent.tools
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()
