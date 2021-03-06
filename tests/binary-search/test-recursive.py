import importlib
import sys
import unittest

sys.path.append("./")

binary_search = importlib.import_module("binary-search")


class TestBSR(unittest.TestCase):
    def test_not_value(self):
        """Test that a not found value returns -1"""
        items = [1, 3, 9, 11, 15, 19, 29]
        value = 30
        result = binary_search.recursive(items, value)

        self.assertEqual(result, -1)

    def test_found_value(self):
        """Test that a found value returns 1"""
        items = [1, 3, 9, 11, 15, 19, 29]
        value = 1
        result = binary_search.recursive(items, value)

        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
