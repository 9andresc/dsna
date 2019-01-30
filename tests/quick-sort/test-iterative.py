import importlib
import sys
import unittest

sys.path.append("./")

import utils

quick_sort = importlib.import_module("quick-sort")


class TestQSI(unittest.TestCase):
    def test_sorting(self):
        """Tests if the items are sorted"""
        items = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        quick_sort.iterative(items)

        self.assertTrue(utils.is_sorted(items))


if __name__ == "__main__":
    unittest.main()
