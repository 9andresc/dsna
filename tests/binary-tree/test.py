import importlib
import sys
import unittest

sys.path.append("./")

binary_tree = importlib.import_module("binary-tree")


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        root = binary_tree.Node(5)
        tree = binary_tree.BinaryTree(root)
        tree.root.left = binary_tree.Node(4)
        tree.root.left.left = binary_tree.Node(2)
        tree.root.left.left.left = binary_tree.Node(1)
        tree.root.left.left.right = binary_tree.Node(3)
        tree.root.right = binary_tree.Node(6)
        tree.root.right.right = binary_tree.Node(7)
        self.tree = tree

    def test_level_order_search(self):
        """Tests if value was found"""
        self.tree.traversal_style = "level_order"

        self.assertTrue(self.tree.search(7))

    def test_level_order_print(self):
        """Tests if printed traversal is correct"""
        self.tree.traversal_style = "level_order"

        self.assertEqual(self.tree.print(), "5-4-6-2-7-1-3")

    def test_pre_order_search(self):
        """Tests if value was found"""
        self.tree.traversal_style = "pre_order"

        self.assertTrue(self.tree.search(7))

    def test_pre_order_print(self):
        """Tests if printed traversal is correct"""
        self.tree.traversal_style = "pre_order"

        self.assertEqual(self.tree.print(), "5-4-2-1-3-6-7")

    def test_in_order_search(self):
        """Tests if value was found"""
        self.tree.traversal_style = "in_order"

        self.assertTrue(self.tree.search(7))

    def test_in_order_print(self):
        """Tests if printed traversal is correct"""
        self.tree.traversal_style = "in_order"

        self.assertEqual(self.tree.print(), "1-2-3-4-5-6-7")

    def test_post_order_search(self):
        """Tests if value was found"""
        self.tree.traversal_style = "post_order"

        self.assertTrue(self.tree.search(7))

    def test_post_order_print(self):
        """Tests if printed traversal is correct"""
        self.tree.traversal_style = "post_order"

        self.assertEqual(self.tree.print(), "1-3-2-4-7-6-5")


if __name__ == "__main__":
    unittest.main()
