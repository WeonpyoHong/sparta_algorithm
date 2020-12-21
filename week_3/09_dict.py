
# 단순한 해시테이블의 구현 ==========================
# 해시넘버를 배열의 갯수로 나눈 나머지의 자리에 넣기

dic = {}

items = [None] * 8

items[hash("slow") % 8] = "느린"
items[hash("fast") % 8] = "빠른"

# 시간복잡도는 얼마나 걸릴까?
# O(1)

# 딕셔너리의 내부는 배열로 구현되어 있다.

class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 키와 밸류 추가하기
    def put(self, key, value):
        index = hash(key) % len(self.items)    # 배열이 길이에 따라서
        self.items[index] = value

    # 키 값에 따른 밸류값 얻기
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))


# 해시가 겹쳐서 충돌이 나는 경우는? 해쉬테이블에서 발생한 충돌을 링크드 리스트로 해결하는 방법 ===============

#key -> ksdfksdf8 -> self.item[7] = [("ksdfksdf8","test")]
#key -> ksdfksdfk -> self.item[7] = [("ksdfksdf8","test")] -> [("ksdfksdfk","test33")]