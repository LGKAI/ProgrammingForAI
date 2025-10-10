class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def delete_head(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if self.head is None: return
        elif self.head.next is None:
            self.head = None
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None

    def is_palindrome(self):
        cur = self.head
        tail = self.head
        while tail.next:
            tail = tail.next
        while cur is not None and tail is not None:
            if cur.data != tail.data: return False
            cur = cur.next
            tail = tail.prev
        return True

    def display(self):
        cur = self.head
        while cur is not None:
            print(cur.data, "-> ", end = "")
            cur = cur.next
        print("None")


if __name__ == "__main__":
    l = DoublyLinkedList()
    l.add_tail(1)
    l.add_tail(2)
    l.add_tail(1)
    l.display()
    print(l.is_palindrome())
    l.delete_tail()
    l.display()