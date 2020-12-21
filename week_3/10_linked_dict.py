
# 링크드 딕셔너리(해쉬테이블에서 발생한 충돌 해결)
# 내부에 객체(리스트 내부엔 튜플로 관리)를 가진 객체

class LinkedTuple:
    def __init__(self):
        # 파이썬은 기본적으로 배열을 제공하지 않음
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []   #[LinkedTuple(),LinkedTuple(),LinkedTuple(),LinkedTuple(),...]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)
