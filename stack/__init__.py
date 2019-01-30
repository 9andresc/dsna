class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, element):
        element.next = self.top
        self.top = element

    def pop(self):
        deleted = self.top

        if self.top:
            self.top = self.top.next
            deleted.next = None

        return deleted
