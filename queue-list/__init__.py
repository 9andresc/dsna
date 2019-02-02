class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self, head_value=None):
        self.head = Element(head_value)

    def get_head(self):
        return self.head.value

    def get_tail(self):
        current = self.head

        while current.next:
            current = current.next

        return current.value

    def enqueue(self, value):
        if self.head.value:
            current = self.head

            while current.next:
                current = current.next

            current.next = Element(value)
        else:
            self.head = Element(value)

    def dequeue(self):
        head = self.head

        if head and head.value:
            self.head = self.head.next
            head.next = None

        return head.value if head else None
