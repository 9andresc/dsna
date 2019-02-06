from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1


class Node(object):
    def __init__(self, value):
        self.value = value
        self.color = None
        self.parent = None
        self.left = None
        self.right = None

    def get_parent(self):
        return self.parent

    def get_grandparent(self):
        parent = self.get_parent()
        if parent == None:
            return None

        return parent.get_parent()

    def get_sibling(self):
        parent = self.get_parent()
        if parent == None:
            return None

        if self == parent.left:
            return parent.right
        else:
            return parent.left

    def get_uncle(self):
        parent = self.get_parent()
        if parent == None:
            return None

        return parent.get_sibling()

    def rotate_left(self):
        right_child = self.right
        parent = self.get_parent()
        self.right = right_child.left
        right_child.left = self
        self.parent = right_child

        if self.right != None:
            self.right.parent = self

        if parent != None:
            if self == parent.left:
                parent.left = right_child
            elif self == parent.right:
                parent.right = right_child

        right_child.parent = parent

    def rotate_right(self):
        left_child = self.left
        parent = self.get_parent()
        self.left = left_child.right
        left_child.right = self
        self.parent = left_child

        if self.left != None:
            self.left.parent = self

        if parent != None:
            if self == parent.left:
                parent.left = left_child
            elif self == parent.right:
                parent.right = left_child

        left_child.parent = parent


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        self._insert_recursive(self.root, node)

        self._insert_repair_tree(node)

        while self.root.get_parent() != None:
            self.root = self.root.get_parent()

    def _insert_recursive(self, parent, node):
        if parent != None and parent.value > node.value:
            if parent.left != None:
                self._insert_recursive(parent.left, node)
            else:
                parent.left = node
        elif parent != None:
            if parent.right != None:
                self._insert_recursive(parent.right, node)
            else:
                parent.right = node

        node.parent = parent
        node.color = Color.RED

    def _insert_repair_tree(self, node):
        if node.get_parent() == None:
            self._insert_case1(node)
        elif node.get_parent().color == Color.BLACK:
            self._insert_case2(node)
        elif node.get_uncle().color == Color.RED:
            self._insert_case3(node)
        else:
            self._insert_case4(node)

    def _insert_case1(self, node):
        node.color = Color.BLACK

    def _insert_case2(self, node):
        pass

    def _insert_case3(self, node):
        node.get_parent().color = Color.BLACK
        node.get_uncle().color = Color.BLACK
        node.get_grandparent().color = Color.RED
        self._insert_repair_tree(node.get_grandparent())

    def _insert_case4(self, node):
        parent = node.get_parent()
        grandparent = node.get_grandparent()

        if node == grandparent.left.right:
            parent.rotate_left()
            node = node.left
        elif node == grandparent.right.left:
            parent.rotate_right()
            node = node.right

        parent = node.get_parent()
        grandparent = node.get_grandparent()

        if node == parent.left:
            grandparent.rotate_right()
        else:
            grandparent.rotate_left()

        parent.color = Color.BLACK
        grandparent.color = Color.RED
