class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self, root_value=None):
        self.root = None if root_value == None else Node(root_value)

    def insert(self, value):
        if self.root:
            current = self.root

            while current:
                if current.value > value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
        else:
            self.root = Node(value)

    def search(self, value):
        current = self.root

        while current:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right

        return False

    def print(self):
        def in_order(node=self.root, traversal=""):
            if node:
                traversal = in_order(node.left, traversal)
                traversal += str(node.value) + "-"
                traversal = in_order(node.right, traversal)

            return traversal

        return in_order()[:-1]

