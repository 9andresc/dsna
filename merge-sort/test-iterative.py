import sys
import unittest

sys.path.append("./")

from utils import is_sorted
from iterative import msi


class TestMSI(unittest.TestCase):
    def test_sorting(self):
        """Tests if the list is sorted"""
        items = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        msi(items)
        self.assertTrue(is_sorted(items))


if __name__ == "__main__":
    unittest.main()