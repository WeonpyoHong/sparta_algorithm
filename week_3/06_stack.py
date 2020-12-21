class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 스택자료 구조 (Last-In First-Out)
# 넣은 순서를 쌓아두고 있는 구조

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None




stack = Stack()
stack.push(3)
print(stack.peek())  #한번 확인해보기
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())

