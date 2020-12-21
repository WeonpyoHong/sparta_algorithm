class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 링크드리스트 끝에서 K번째에 있는 값 출력하기
# 1 - LinkedList 길이 전부 알아내서 구하기
# 2 - 그 길이에서 k만큼 뺀 길이만큼 이동

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 0
        current = self.head
        while current.next is not None:
            length += 1
            current = current.next
        from_first = length + 1 - k
        current = self.head
        for i in range(0, from_first):
            current = current.next
        return current


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# linked_list.append(9)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!