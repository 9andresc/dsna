import importlib
import sys
import unittest

sys.path.append("./")

linked_list = importlib.import_module("linked-list")


class TestLL(unittest.TestCase):
    def setUp(self):
        head = linked_list.Element(1)
        self.linked_list = linked_list.LinkedList(head)

    def test_append(self):
        """Tests if element was appended"""
        element = linked_list.Element(2)
        self.linked_list.append(element)
        self.assertEqual(self.linked_list.head.next.value, 2)

    def test_get_position(self):
        """Tests if position returns an element"""
        element = linked_list.Element(2)
        self.linked_list.append(element)
        self.assertEqual(self.linked_list.get_position(2), 2)

    def test_delete(self):
        """Tests if element was deleted"""
        element = linked_list.Element(2)
        self.linked_list.append(element)
        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.get_position(2), None)


if __name__ == "__main__":
    unittest.main()
