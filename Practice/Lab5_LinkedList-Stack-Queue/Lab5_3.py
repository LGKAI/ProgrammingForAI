class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack Implementation using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def initialize(self, data):
        self.top = Node(data)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def count(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.top is None

# Queue Implementation using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def initialize(self, data):
        new_node = Node(data)
        self.front = self.rear = new_node

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued_data

    def count(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.front is None


if __name__ == "__main__":
    # Stack
    stack = Stack()
    stack.initialize(10)
    stack.push(20)
    stack.push(30)
    print("Stack count:", stack.count())  # Output: 3
    print("Stack pop:", stack.pop())    # Output: 30
    print("Is stack empty:", stack.is_empty())  # Output: False

    # Queue
    queue = Queue()
    queue.initialize(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue count:", queue.count())  # Output: 3
    print("Queue dequeue:", queue.dequeue())  # Output: 10
    print("Is queue empty:", queue.is_empty())  # Output: False
