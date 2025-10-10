class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, "-> ", end = "")
            current = current.next
        print("None")

    def find_first_node(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return cur
            else:
                cur = cur.next
        return None
    
    def get_length(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        return length
    
    def count_primes(self):
        cur = self.head
        count = 0
        while cur:
            if is_prime(cur.data):
                count += 1
            cur = cur.next
        return count
    
    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_2nd_node_head(self):
        if self.head is None or self.head.next is None:
            return
        self.head.next = self.head.next.next

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def delete_tail(self):
        if self.head is None: return
        cur = self.head
        if cur.next is None:
            self.head = None
        else:
            while cur.next.next:
                cur = cur.next
            cur.next = None
        
    def delete_node_before_tail(self):
        if self.head is None or self.head.next is None:
            return
        cur = self.head
        if cur.next.next is None:
            self.head = cur.next
            return
        while cur.next.next.next:
            cur = cur.next
        cur.next = cur.next.next

    def insert_at_pos(self, data, pos):
        if pos == 0:
            self.add_head(data)
        elif pos > self.get_length():
            self.add_tail(data)
        else:
            cur = self.head
            while pos != 1:
                cur = cur.next
                pos -= 1
            new = Node(data)
            new.next = cur.next
            cur.next = new

    def find_balance_point(self):
        cur = self.head
        all_sum = 0
        while cur is not None:
            all_sum += cur.data
            cur = cur.next
        k = 0
        sum_k = 0
        cur = self.head
        while cur is not None:
            sum_k += cur.data
            k += 1
            if abs(sum_k - (all_sum - sum_k)) < (all_sum / 2):
                return k
            cur = cur.next
        return -1

    def mergeLinkedList(l1, l2):
        l3 = LinkedList()
        cur1 = l1.head
        cur2 = l2.head
        while cur1 is not None and cur2 is not None:
            if cur1.data < cur2.data:
                l3.add_tail(cur1.data)
                cur1 = cur1.next
            else:
                l3.add_tail(cur2.data)
                cur2 = cur2.next
        while cur2 is not None:
            l3.add_tail(cur2.data)
            cur2 = cur2.next
        while cur1 is not None:
            l3.add_tail(cur1.data)
            cur1 = cur1.next
        return l3
    
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False


if __name__ == "__main__":
    l1 = LinkedList()
    for i in [1, 3, 5, 7, 9]:
        l1.add_tail(i)
    l1.display()
    
    l2 = LinkedList()
    for i in [2, 4, 6, 8, 10]:
        l2.add_tail(i)
    l2.display()

    l3 = LinkedList.mergeLinkedList(l1, l2)
    l3.display()
    l3.delete_node_before_tail()
    l3.display()
