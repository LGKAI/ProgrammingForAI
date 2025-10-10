class Queue:
    def __init__ (self, limit = None):
        self.__data__ = []
        self.__length__ = 0
        if limit is None:
            self.limit = 1000
        else:
            self.limit = limit
    
    def enqueue(self, item):
        if self.isFull():
            return
        self.__data__.append(item)
        self.__length__ += 1

    def dequeue(self):
        if self.isEmpty():
            return
        self.__length__ -= 1
        return self.__data__.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        return self.__data__[0]
    
    def isEmpty(self):
        return self.__length__ == 0
    
    def isFull(self):
        return self.__length__ == self.limit
    
    def size(self):
        return self.__length__
    
def reverse_queue(queue):
    stack = []
    while not queue.isEmpty():
        stack.append(queue.dequeue())
    while stack:
        queue.enqueue(stack.pop())


if __name__ == "__main__":
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)

    reverse_queue(q)

    while not q.isEmpty():
        print(q.dequeue(), end = " ")