class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_head(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def delete_tail(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
            self.tail = cur

    def add_before_tail(self, data):
        if self.head is None or self.head == self.tail:
            return
        new = Node(data)
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        new.next = self.tail
        cur.next = new


if __name__ == "__main__":
    pass