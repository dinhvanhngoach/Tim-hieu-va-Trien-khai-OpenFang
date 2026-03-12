import os
import sys
import unittest

# Thêm đường dẫn để import được main.py và agent_second.py của I4
I4_DIR = os.path.join(os.path.dirname(__file__), "..", "I4")
sys.path.insert(0, os.path.abspath(I4_DIR))

import main as main_i4  # type: ignore


class TestMainPipeline(unittest.TestCase):
    """
    End-to-end test cho pipeline 2 agent trong I4/main.py
    - Agent 1: Processor (uppercase / double)
    - Agent 2: Reviewer (tóm tắt output của Agent 1)
    """

    def test_pipeline_success_uppercase(self):
        """Agent 1 + Reviewer chạy thành công với tool_uppercase."""
        output_agent1, summary = main_i4.run_pipeline("uppercase", "hello world.")

        self.assertEqual(output_agent1, "HELLO WORLD.")
        # Reviewer tóm tắt bằng câu đầu tiên (bỏ phần sau dấu chấm)
        self.assertEqual(summary, "HELLO WORLD")

    def test_pipeline_agent1_error_skip_reviewer(self):
        """
        Nếu Agent 1 lỗi (vd: double nhận text sai kiểu) thì:
        - output_agent1 là None
        - summary là None
        - Reviewer không được gọi.
        """
        output_agent1, summary = main_i4.run_pipeline("double", "abc")

        self.assertIsNone(output_agent1)
        self.assertIsNone(summary)


if __name__ == "__main__":
    unittest.main(verbosity=2)

