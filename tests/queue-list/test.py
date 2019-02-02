import importlib
import sys
import unittest

sys.path.append("./")

queue_list = importlib.import_module("queue-list")


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = queue_list.Queue(1)

    def test_enqueue(self):
        """Tests if element was enqueued"""
        self.queue.enqueue(2)

        self.assertEqual(self.queue.get_tail(), 2)

    def test_dequeue(self):
        """Tests if element was dequeued"""
        self.queue.enqueue(2)
        removed_element = self.queue.dequeue()

        self.assertEqual(removed_element, 1)
        self.assertEqual(self.queue.get_tail(), 2)


if __name__ == "__main__":
    unittest.main()
