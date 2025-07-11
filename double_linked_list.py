class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return 
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            last = current
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        if not current:
            return
        
        while current.next:
            current = current.next
        
        while current:
            print(current.data, end=' ')
            current = current.prev
        print()

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display_forward()   # 5 10 20
dll.display_backward()  # 20 10 5
dll.delete(10)
dll.display_forward()   # 5 20
