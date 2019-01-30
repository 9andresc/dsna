import sys
import unittest

sys.path.append("./")

import stack


class TestStack(unittest.TestCase):
    def setUp(self):
        top = stack.Element(1)
        self.stack = stack.Stack(top)

    def test_push(self):
        """Tests if element was added"""
        element = stack.Element(2)
        self.stack.push(element)

        self.assertEqual(self.stack.top.value, 2)

    def test_pop(self):
        """Tests if element was removed"""
        element = stack.Element(2)
        self.stack.push(element)
        removed_element = self.stack.pop()

        self.assertEqual(removed_element.value, 2)
        self.assertEqual(self.stack.top.value, 1)


if __name__ == "__main__":
    unittest.main()
