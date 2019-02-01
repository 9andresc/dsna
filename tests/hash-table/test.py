import importlib
import sys
import unittest

sys.path.append("./")

hash_table = importlib.import_module("hash-table")


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = hash_table.HashTable(11)

    def test_put_and_get(self):
        """Tests if value was added"""
        self.ht.put(54, "cat")
        self.assertEqual(self.ht.get(54), "cat")


if __name__ == "__main__":
    unittest.main()
