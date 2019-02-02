import importlib
import sys
import unittest

sys.path.append("./")

stack_list = importlib.import_module("stack-list")


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = stack_list.Stack(1)

    def test_push(self):
        """Tests if element was added"""
        self.stack.push(2)

        self.assertEqual(self.stack.get_top(), 2)

    def test_pop(self):
        """Tests if element was removed"""
        self.stack.push(2)
        removed_element = self.stack.pop()

        self.assertEqual(removed_element, 2)
        self.assertEqual(self.stack.get_top(), 1)


if __name__ == "__main__":
    unittest.main()
