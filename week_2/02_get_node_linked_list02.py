class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        current = self.head

        for i in range(0, index):
            current = current.next

        if current is None:
            return None

        return current.data




linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.get_node(2))
# print(linked_list.get_node(1))
# print(linked_list.get_node(2))

# linked_list.print_all()