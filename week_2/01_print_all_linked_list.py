
# 링크드 리스트 만들기

# [3] -> [4]
# data, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node

# print(node.data)
# print(node.next.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 노드 추가하기
    def append(self, data):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    # 모든 원소 출력하기
    def print_all(self):
        current = self.head
        print(current.data)
        while current.next is not None:
            current = current.next
            print(current.data)



linked_list = LinkedList(3)
# print(linked_list.head)

linked_list.append(4)
linked_list.append(5)

linked_list.print_all()