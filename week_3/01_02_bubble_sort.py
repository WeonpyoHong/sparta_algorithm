
# 버블 소트의 알고리즘 ===> 가장 큰 숫자가 맨 뒤로 가게 되어있음.


input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):     # 비교횟수를 결정하는 for문 (비교횟수는 -1씩 줄기)   #0  1  2  3  < 4
        for j in range(n - i - 1):    # 실제 배열 앞뒤 숫자 비교를 위한 for 문
            # print(f"i: {i}, j: {j}")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]



bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 시간복잡도

# 대략적으로는 O(N^2)



# 동일한 알고리즘 temp 변수 이용해서 ===========================

some_array = [4, 6, 2, 9, 1]

def bubble_sort2(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp



bubble_sort2(some_array)
print(some_array)