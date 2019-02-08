import pprint
import sys
import unittest

pp = pprint.PrettyPrinter(indent=2)
sys.path.append("./")

import graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = graph.Graph()

        self.graph.set_node_names(
            (
                "Mountain View",  # 0
                "San Francisco",  # 1
                "London",  # 2
                "Shanghai",  # 3
                "Berlin",  # 4
                "Sao Paolo",  # 5
                "Bangalore",  # 6
            )
        )

        self.graph.insert_edge(51, 0, 1)  # MV <-> SF
        self.graph.insert_edge(51, 1, 0)  # SF <-> MV
        self.graph.insert_edge(9950, 0, 3)  # MV <-> Shanghai
        self.graph.insert_edge(9950, 3, 0)  # Shanghai <-> MV
        self.graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
        self.graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
        self.graph.insert_edge(9900, 1, 3)  # SF <-> Shanghai
        self.graph.insert_edge(9900, 3, 1)  # Shanghai <-> SF
        self.graph.insert_edge(9130, 1, 4)  # SF <-> Berlin
        self.graph.insert_edge(9130, 4, 1)  # Berlin <-> SF
        self.graph.insert_edge(9217, 2, 3)  # London <-> Shanghai
        self.graph.insert_edge(9217, 3, 2)  # Shanghai <-> London
        self.graph.insert_edge(932, 2, 4)  # London <-> Berlin
        self.graph.insert_edge(932, 4, 2)  # Berlin <-> London
        self.graph.insert_edge(9471, 2, 5)  # London <-> Sao Paolo
        self.graph.insert_edge(9471, 5, 2)  # Sao Paolo <-> London

    def test_dfs(self):
        """Tests if path is correct"""
        self.assertListEqual(
            self.graph.dfs_names(2),
            [
                "London",
                "Shanghai",
                "Mountain View",
                "San Francisco",
                "Berlin",
                "Sao Paolo",
            ],
        )

    def test_bfs(self):
        """Tests if path is correct"""
        self.assertListEqual(
            self.graph.bfs_names(2),
            [
                "London",
                "Shanghai",
                "Berlin",
                "Sao Paolo",
                "Mountain View",
                "San Francisco",
            ],
        )


if __name__ == "__main__":
    unittest.main()
