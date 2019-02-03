class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    def __init__(self, top_value=None):
        self.top = Element(top_value)

    def get_top(self):
        return self.top.value

    def push(self, value):
        element = Element(value)
        element.next = self.top
        self.top = element

    def pop(self):
        top = self.top

        if top and top.value:
            self.top = self.top.next
            top.next = None

        return top.value if top else None
