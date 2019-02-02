import importlib
import sys

sys.path.append("./")

queue_list = importlib.import_module("queue-list")
stack_list = importlib.import_module("stack-list")


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root, traversal_style="level_order"):
        self.root = root
        self.traversal_style = traversal_style

    def search(self, value):
        def level_order(node=self.root):
            nodes_queue = queue_list.Queue()

            while node:
                if node.value == value:
                    return True

                if node.left:
                    nodes_queue.enqueue(node.left)
                if node.right:
                    nodes_queue.enqueue(node.right)

                node = nodes_queue.dequeue()

            return False

        def pre_order(node=self.root, found=False):
            if node:
                if node.value == value:
                    return True
                found = pre_order(node.left, found)
                found = pre_order(node.right, found)

            return found

        def in_order(node=self.root, found=False):
            if node:
                found = in_order(node.left, found)
                if node.value == value:
                    return True
                found = in_order(node.right, found)

            return found

        def post_order(node=self.root, found=False):
            if node:
                found = post_order(node.left, found)
                found = post_order(node.right, found)
                if node.value == value:
                    return True

            return found

        return locals()[self.traversal_style]()

    def print(self):
        def level_order(node=self.root, traversal=""):
            nodes_queue = queue_list.Queue()

            while node:
                traversal += str(node.value) + "-"

                if node.left:
                    nodes_queue.enqueue(node.left)
                if node.right:
                    nodes_queue.enqueue(node.right)

                node = nodes_queue.dequeue()

            return traversal

        def pre_order(node=self.root, traversal=""):
            if node:
                traversal += str(node.value) + "-"
                traversal = pre_order(node.left, traversal)
                traversal = pre_order(node.right, traversal)

            return traversal

        def in_order(node=self.root, traversal=""):
            if node:
                traversal = in_order(node.left, traversal)
                traversal += str(node.value) + "-"
                traversal = in_order(node.right, traversal)

            return traversal

        def post_order(node=self.root, traversal=""):
            if node:
                traversal = post_order(node.left, traversal)
                traversal = post_order(node.right, traversal)
                traversal += str(node.value) + "-"

            return traversal

        return locals()[self.traversal_style]()[:-1]
