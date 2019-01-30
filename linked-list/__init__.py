class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = element
        else:
            self.head = element

    def get_position(self, position):
        current = self.head
        current_position = 1

        while current:
            if current_position == position:
                return current.value

            current = current.next
            current_position += 1

    def insert(self, element, position):
        current = self.head
        current_position = 1

        if position > 1:
            while current:
                if current_position == position:
                    element.next = current.next
                    current.next = element

                current = current.next
                current_position += 1
        elif position == 1:
            element.next = self.head
            self.head = element

    def delete(self, value):
        current = self.head

        if current == None:
            return
        elif current.value == value:
            self.head = current.next
            return

        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return

            current = current.next
