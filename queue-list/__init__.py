class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self, head):
        self.head = head
    
    def get_head(self):
        return self.head
    
    def get_tail(self):
        current = self.head

        while current.next:
            current = current.next
        
        return current
    
    def enqueue(self, element):
        if self.head:
            current = self.head
            
            while current.next:
                current = current.next
            
            current.next = element
        else:
            self.head = element
    
    def dequeue(self):
        head = self.head

        if self.head:
            self.head = self.head.next
            head.next = None

        return head
