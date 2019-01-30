import importlib
import sys
import unittest

sys.path.append("./")

queue_list = importlib.import_module("queue-list")


class TestQueue(unittest.TestCase):
    def setUp(self):
        head = queue_list.Element(1)
        self.queue = queue_list.Queue(head)

    def test_enqueue(self):
        """Tests if element was enqueued"""
        element = queue_list.Element(2)
        self.queue.enqueue(element)

        self.assertEqual(self.queue.get_tail().value, 2)

    def test_dequeue(self):
        """Tests if element was dequeued"""
        element = queue_list.Element(2)
        self.queue.enqueue(element)
        removed_element = self.queue.dequeue()

        self.assertEqual(removed_element.value, 1)
        self.assertEqual(self.queue.get_tail().value, 2)


if __name__ == "__main__":
    unittest.main()
