import unittest

from iterative import bsi


class TestBSI(unittest.TestCase):
    def test_not_found_value(self):
        """Test that a not found value returns -1"""
        input_list = [1, 3, 9, 11, 15, 19, 29]
        value = 30
        result = bsi(input_list, value)
        self.assertEqual(result, -1)

    def test_found_value(self):
        """Test that a found value returns 1"""
        input_list = [1, 3, 9, 11, 15, 19, 29]
        value = 1
        result = bsi(input_list, value)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
