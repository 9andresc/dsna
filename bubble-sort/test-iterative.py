import unittest

from iterative import bsi


def is_sorted(input_list):
    """Checks whether the list is sorted or not"""
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))


class TestBSI(unittest.TestCase):
    def test_sorting(self):
        """Tests if the list is sorted"""
        input_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        bsi(input_list)
        self.assertTrue(is_sorted(input_list))


if __name__ == "__main__":
    unittest.main()
