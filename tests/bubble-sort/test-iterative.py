import importlib
import sys
import unittest

sys.path.append("./")

import utils

bubble_sort = importlib.import_module("bubble-sort")


class TestBSI(unittest.TestCase):
    def test_sorting(self):
        """Tests if the list is sorted"""
        items = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        bubble_sort.iterative(items)
        self.assertTrue(utils.is_sorted(items))


if __name__ == "__main__":
    unittest.main()
