import importlib
import sys
import unittest

sys.path.append("./")

binary_search_tree = importlib.import_module("binary-search-tree")


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.binary_search_tree = binary_search_tree.BinarySearchTree()

    def test_insert(self):
        """Tests if values were added"""
        self.binary_search_tree.insert(2)
        self.binary_search_tree.insert(1)
        self.binary_search_tree.insert(3)

        self.assertEqual(self.binary_search_tree.root.value, 2)
        self.assertEqual(self.binary_search_tree.root.left.value, 1)
        self.assertEqual(self.binary_search_tree.root.right.value, 3)

    def test_search(self):
        """Tests if values can be found"""
        self.binary_search_tree.insert(2)
        self.binary_search_tree.insert(1)
        self.binary_search_tree.insert(3)

        self.assertTrue(self.binary_search_tree.search(1))
        self.assertTrue(self.binary_search_tree.search(2))
        self.assertTrue(self.binary_search_tree.search(3))
        self.assertFalse(self.binary_search_tree.search(4))

    def test_print(self):
        """Tests if values are correctly printed"""
        self.binary_search_tree.insert(2)
        self.binary_search_tree.insert(1)
        self.binary_search_tree.insert(3)

        self.assertEqual(self.binary_search_tree.print(), "1-2-3")


if __name__ == "__main__":
    unittest.main()
