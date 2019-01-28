import sys
import unittest

sys.path.append("./")

from utils import is_sorted

from iterative import qsi


class TestQSI(unittest.TestCase):
    def test_sorting(self):
        """Tests if the items are sorted"""
        items = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        qsi(items)
        self.assertTrue(is_sorted(items))


if __name__ == "__main__":
    unittest.main()
