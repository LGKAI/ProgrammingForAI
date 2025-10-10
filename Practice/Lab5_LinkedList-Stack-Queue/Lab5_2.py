class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Thêm nút vào đầu danh sách
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Thêm nút vào cuối danh sách
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Chèn nút sau một nút nhất định
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    # Xóa một nút
    def delete_node(self, node):
        if self.head is None or node is None:
            return
        if node == self.head:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node = None

    # Duyệt danh sách từ đầu đến cuối
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Thêm dữ liệu
    dll.push(3)
    dll.push(2)
    dll.push(1)  # Danh sách: 1 <-> 2 <-> 3
    dll.append(4)  # Danh sách: 1 <-> 2 <-> 3 <-> 4
    
    # Chèn vào giữa
    dll.insert_after(dll.head.next, 2.5)  # Danh sách: 1 <-> 2 <-> 2.5 <-> 3 <-> 4

    # In danh sách
    print("Danh sách sau khi thêm:")
    dll.print_list()

    # Xóa nút
    dll.delete_node(dll.head.next.next)  # Xóa nút 2.5
    print("Danh sách sau khi xóa:")
    dll.print_list()
