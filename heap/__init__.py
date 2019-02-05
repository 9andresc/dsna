class Heap(object):
    def __init__(self):
        self.nodes = []

    def get_min(self):
        return self.nodes[0]

    def get_parent_index(self, i):
        return int((i - 1) / 2)

    def get_left_index(self, i):
        return 2 * i + 1

    def get_right_index(self, i):
        return 2 * i + 2

    def has_left_index(self, i):
        left_index = self.get_left_index(i)
        return left_index < len(self.nodes)

    def has_right_index(self, i):
        right_index = self.get_right_index(i)
        return right_index < len(self.nodes)

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def heapify_up(self, node_index):
        parent_index = self.get_parent_index(node_index)

        while node_index != 0 and self.nodes[parent_index] > self.nodes[node_index]:
            self.swap(node_index, parent_index)
            node_index = self.get_parent_index(node_index)

    def heapify_down(self, parent_index):
        if self.has_left_index(parent_index):
            left_index = self.get_left_index(parent_index)
            if self.nodes[left_index] < self.nodes[parent_index]:
                self.swap(left_index, parent_index)
                self.heapify_down(left_index)
        elif self.has_right_index(parent_index):
            right_index = self.get_right_index(parent_index)
            if self.nodes[right_index] < self.nodes[parent_index]:
                self.swap(right_index, parent_index)
                self.heapify_down(right_index)

    def insert(self, value):
        self.nodes.append(value)
        node_index = len(self.nodes) - 1
        self.heapify_up(node_index)

    def delete(self, node_index):
        if node_index >= 0 and node_index < len(self.nodes):
            self.nodes[node_index] = float("-inf")
            self.heapify_up(node_index)
            self.nodes[0] = self.nodes.pop()
            self.heapify_down(0)
