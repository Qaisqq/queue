class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

class QueueLinkedList():
    def __init__(self):
        self.LL = LinkedList()

    def en_queue(self, value):
        new_node = Node(value)
        if self.LL.head is None:
            self.LL.head = new_node
        else:
            current_node = self.LL.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.LL.count += 1

    def de_queue(self):
        if self.LL.head is None:
            raise IndexError("Queue is empty")
        first_value = self.LL.head.value
        self.LL.head = self.LL.head.next
        self.LL.count -= 1
        return first_value