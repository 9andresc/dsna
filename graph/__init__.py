import importlib
import sys

sys.path.append("./")

queue_list = importlib.import_module("queue-list")


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.node_names = []
        self._node_map = {}

    def insert_edge(self, edge_value, node_from_value, node_to_value):
        nodes = {node_from_value: None, node_to_value: None}

        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break

        for node_value in nodes:
            nodes[node_value] = nodes[node_value] or self._insert_node(node_value)

        node_from = nodes[node_from_value]
        node_to = nodes[node_to_value]
        edge = Edge(edge_value, node_from, node_to)
        node_from.edges.append(edge)
        node_to.edges.append(edge)
        self.edges.append(edge)

    def _insert_node(self, node_value):
        node = Node(node_value)
        self.nodes.append(node)
        self._node_map[node_value] = node
        return node

    def set_node_names(self, names):
        self.node_names = list(names)

    def get_edge_list_names(self):
        return [
            (
                edge.value,
                self.node_names[edge.node_from.value],
                self.node_names[edge.node_to.value],
            )
            for edge in self.edges
        ]

    def get_adjacency_list_names(self):
        def convert_to_names(pair):
            node_number, value = pair
            return (self.node_names[node_number], value)

        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None

            return map(convert_to_names, adjacency_list_for_node)

        adjacency_list = self._get_adjacency_list()
        return [
            map_conversion(adjacency_list_for_node)
            for adjacency_list_for_node in adjacency_list
        ]

    def _get_adjacency_list(self):
        max_index = self._find_max_index()
        adjacency_list = [[] for _ in range(max_index)]

        for edge in self.edges:
            from_value, to_value = edge.node_from.value, edge.node_to.value
            adjacency_list[from_value].append((to_value, edge.value))

        return [e or None for e in adjacency_list]

    def get_adjacency_matrix(self):
        max_index = self._find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]

        for edge in self.edges:
            from_index, to_index = edge.node_from.value, edge.node_to.value
            adjacency_matrix[from_index][to_index] = edge.value

        return adjacency_matrix

    def _find_max_index(self):
        if len(self.node_names) > 0:
            return len(self.node_names)

        max_index = -1

        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value

        return max_index

    def dfs_names(self, start_node_number):
        return [self.node_names[number] for number in self._dfs(start_node_number)]

    def _dfs(self, start_node_number):
        self._clear_visited()
        start_node = self._find_node(start_node_number)
        return self._dfs_helper(start_node)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def _find_node(self, node_number):
        return self._node_map.get(node_number)

    def _dfs_helper(self, start_node):
        ret_list = [start_node.value]
        start_node.visited = True

        edges_out = [e for e in start_node.edges if e.node_to.value != start_node.value]

        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self._dfs_helper(edge.node_to))

        return ret_list

    def bfs_names(self, start_node_number):
        return [self.node_names[number] for number in self._bfs(start_node_number)]

    def _bfs(self, start_node_number):
        self._clear_visited()
        node = self._find_node(start_node_number)

        ret_list = [node.value]
        node.visited = True

        queue = queue_list.Queue()

        while node:
            edges_out = [e for e in node.edges if e.node_to.value != node.value]
            for edge in edges_out:
                if not edge.node_to.visited:
                    ret_list.append(edge.node_to.value)
                    edge.node_to.visited = True
                    queue.enqueue(edge.node_to)

            node = queue.dequeue()

        return ret_list
