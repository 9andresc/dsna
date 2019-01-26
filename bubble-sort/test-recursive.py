import sys
import unittest

sys.path.append("./")

from utils import is_sorted
from recursive import bsr


class TestBSR(unittest.TestCase):
    def test_sorting(self):
        """Tests if the list is sorted"""
        input_list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
        bsr(input_list)
        self.assertTrue(is_sorted(input_list))


if __name__ == "__main__":
    unittest.main()
