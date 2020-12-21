class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 링크드리스트 끝에서 K번째에 있는 값 출력하기
# K만큼의 거리를

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 두개의 인덱스간의 거리를 항상 K만큼을 유지하는 방법
    # 1.노드를 두개 잡는다.
    # 2.한 노드를 다른 노드보다 k만큼 떨어지게 한다.
    # 3.그리고 계속 한 칸씩 같이 이동한다.
    # 4.만약 더 빠른 노드가 끝에 도달했다면
    # 5.느린노드는 끝에서 K만큼 떨어진 노드가 되므로 바로 반환

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# linked_list.append(9)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!