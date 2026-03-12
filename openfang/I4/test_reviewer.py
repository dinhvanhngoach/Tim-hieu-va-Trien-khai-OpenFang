# test_reviewer.py
# I4 - Phạm Quốc Đạt
# Ngày 4: Viết test cho Reviewer agent và tool_summarize

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_second import tool_summarize, Reviewer


class TestReviewer(unittest.TestCase):

    # Test case 1: tool_summarize hoạt động đúng với text có dấu chấm
    def test_tool_summarize_basic(self):
        text = "Hello world. This is a test. Another sentence."
        result = tool_summarize(text)
        self.assertEqual(result, "Hello world")

    # Test case 2: tool_summarize với text 1 câu không có dấu chấm
    def test_tool_summarize_no_dot(self):
        text = "Hello world"
        result = tool_summarize(text)
        self.assertEqual(result, "Hello world")

    # Test case 3: Reviewer agent khởi tạo đúng
    def test_reviewer_init(self):
        reviewer = Reviewer()
        self.assertEqual(reviewer.name, "Reviewer")
        self.assertIsNotNone(reviewer.description)

    # Test case 4: Reviewer agent chạy được với input hợp lệ
    def test_reviewer_run(self):
        reviewer = Reviewer()
        # Không raise exception là pass
        try:
            reviewer.run("This is Agent 1 output. Some more text.")
            passed = True
        except Exception:
            passed = False
        self.assertTrue(passed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
