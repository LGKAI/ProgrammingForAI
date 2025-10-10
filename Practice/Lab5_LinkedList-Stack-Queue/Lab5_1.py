class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head = new

    def addTail(self, data):
        new = Node(data)
        if self.head is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def removeHead(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next

    def removeTail(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            cur.next = None
            self.tail = cur

    def removeAll(self):
        self.head = self.tail = None
    
    def removeBefore(self, val):
        if self.head is None or self.head.next is None:
            return
        prev = None
        cur = self.head
        while cur.next:
            if cur.next.data == val:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                if cur == self.tail:
                    self.tail = prev
            prev = cur
            cur = cur.next

    def removeAfter(self, val):
        if self.head is None or self.head.next is None:
            return
        cur = self.head
        while cur:
            if cur.data == val:
                if cur.next:
                    if cur.next == self.tail:
                        self.tail = cur
                    cur.next = cur.next.next
            cur = cur.next

    def addPos(self, data, pos):
        new = Node(data)
        if pos == 0:
            new.next = self.head
            self.head = new
            return
        cur = self.head
        count = 0
        while cur and count < pos - 1:
            cur = cur.next
            count += 1
        new.next = cur.next
        cur.next = new
        if new.next is None:
            self.tail = new

    def removePos(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
            return
        cur = self.head
        count = 0
        while cur and count < pos - 1:
            cur = cur.next
            count += 1
        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next

    def addBefore(self, data, val):
        new = Node(data)
        if self.head is None:
            return
        if self.head.data == val:
            new.next = self.head
            self.head = new
        prev = None
        cur = self.head
        while cur and cur.data != val:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        new.next = cur
        prev.next = new
        if cur == self.tail:
            self.tail = new
        
    def addAfter(self, data, val):
        new = Node(data)
        if self.head is None:
            return
        cur = self.head
        while cur:
            if cur.data == val:
                new.next = cur.next
                cur.next = new
            if new.next is None:
                self.tail = new
            cur = cur.next

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data, end = " -> ")
            cur = cur.next
        print("None")

    def countElements(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def countAppearance(self, value):
        count = 0
        cur = self.head
        while cur:
            if cur.data == value:
                count += 1
            cur = cur.next
        return count
    
    def reverseList(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head, self.tail = self.tail, self.head

    def removeDuplicate(self):
        if self.head is None:
            return
        cur = self.head
        seen = set([cur.data])
        while cur.next:
            if cur.next.data in seen:
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
            else:
                seen.add(cur.next.data)
                cur = cur.next

    def removeElement(self, key):
        while self.head and self.head.data == key:
            self.head = self.head.next
        if self.head is None:
            self.tail = None
            return
        cur = self.head
        while cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
            else:
                cur = cur.next


if __name__ == "__main__":
    l = SingleLinkedList()
    l.addHead(1)
    l.addTail(2)
    l.addTail(3)
    l.addTail(4)
    l.addTail(1)
    l.addTail(5)
    l.removeAfter(1)
    l.printList()
    print(l.countElements())