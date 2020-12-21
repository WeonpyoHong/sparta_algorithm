input = [4, 6, 2, 9, 1]



for i in range(1,5):    #1 2   3     4
   for j in range(i):   #0 0 1 0 1 2 0 1 2 3
       print(i - j)     #1 2 1 3 2 1 4 3 2 1   변환된 인덱스





def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:           #앞에 있는 애가 뒤에 있는 애보다 더 크다면
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break         #더 작지 않으면 앞에와는 더이상 비교하지 않음
    return



# 최선의 경우 시간복잡도가 N정도가 될 수 있으므로 (break문이 존재)
# 삽입정렬이 버블정렬과 선택정렬보다 좀 낫다.


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

