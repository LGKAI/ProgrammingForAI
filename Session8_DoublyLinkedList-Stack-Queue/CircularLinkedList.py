class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def traverse(self):
        if self.head is None:
            return
        cur = self.head
        while True:
            print(cur.data, end = " -> ")
            cur = cur.next
            if cur == self.head:
                break
        print("None")
    
    def insert_at_start(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = new
        else:
            new.next = self.head
            self.tail.next = new
            self.head = new
        self.size += 1

    def insert_at_end(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = new
        else:
            new.next = self.head
            self.tail.next = new
            self.tail = new
        self.size += 1

    def delete_from_start(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.next = self.head.next  
            self.head = self.head.next  
        self.size -= 1

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head  
            self.tail = current  
        self.size -= 1


if __name__ == "__main__":
    pass