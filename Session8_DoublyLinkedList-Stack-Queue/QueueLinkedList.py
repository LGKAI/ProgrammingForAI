class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, limit = None):
        self.front = None
        self.rear = None
        self.__length__ = 0
        if limit is None:
            self.limit = 1000
        else:
            self.limit = limit
    
    def enqueue(self, item):
        if self.isFull():
            return 
        new = Node(item)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        self.__length__ += 1

    def dequeue(self):
        if self.isEmpty():
            return 
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.__length__ -= 1
        return temp.data
    
    def front(self):
        if self.isEmpty():
            return None
        return self.front.data
    

if __name__ == "__main__":
    pass
