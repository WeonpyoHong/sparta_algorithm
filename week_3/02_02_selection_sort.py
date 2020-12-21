input = [4, 6, 2, 9, 1]

# 선택정렬 알고리즘

# 1. [4 6 2 9 1]
#     - - - - -
# 2. [1 6 2 9 4]
#       - - - -
# 3. [1 2 6 9 4]
#         - - -
# 4. [1 2 4 9 6]
#           - -



# for i in range(5 - 1):       # i = 0         1       2     3
#     for j in range(5 - i):   # j = 0 1 2 3 4 0 1 2 3 0 1 2 0 1
#         print(i + j)         #     0 1 2 3 4 1 2 3 4 2 3 4 3 4





def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):  # 인덱스를 i+j로 변환하는 효과
            print(f"i: {i}, j: {j}, i+j: {i+j}")
            if array[i+j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!



# 선택정렬 알고리즘 생각해보기

some_array = [4, 6, 2, 9, 1]

[1,6,2,9,4]
[1,2,6,9,4]
[1,2,4,9,6]
[1,2,4,6,9]


for i in range(len(some_array)):  #0
    current_num = some_array[i]
    min_num = 0
    min_num_index = 0
    for j in range(i+1,len(some_array)):    #1
        min_num = some_array[j]             #6
        print(f"i번재 {i} j번째 {j} 현재숫자 {current_num} 최소숫자 {min_num} 인덱스 {min_num_index}")
        if min_num < some_array[i]:
            min_num = some_array[j]
            min_num_index = j
            print(f"최소숫자의 인식 {min_num} 인덱스 {min_num_index}")
    if min_num < current_num:
        print(f"숫자 체인지 {some_array[i], some_array[min_num_index]}")
        some_array[i], some_array[min_num_index] = some_array[min_num_index], some_array[i]



print(some_array)