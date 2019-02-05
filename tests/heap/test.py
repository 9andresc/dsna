import importlib
import sys
import unittest

sys.path.append("./")

import heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = heap.Heap()

    def test_insert(self):
        """Tests if values were correctly added"""
        self.heap.insert(3)
        self.heap.insert(2)
        self.heap.insert(1)

        self.assertEqual(self.heap.get_min(), 1)

    def test_delete(self):
        """Tests if value was correctly removed"""
        self.heap.insert(3)
        self.heap.insert(2)
        self.heap.insert(1)
        self.heap.delete(0)

        self.assertEqual(self.heap.get_min(), 2)


if __name__ == "__main__":
    unittest.main()
