input = [4, 6, 2, 9, 1]


# 선택정렬 알고리즘 생각해보기

# 결국, 버블소트와 반대로 가장 작은 숫자를 맨앞으로 빼놓는 원리

some_array = [9, 6, 4, 2, 1]


input = [4, 6, 2, 9, 1]

[1,6,2,9,4]
[1,2,6,9,4]
[1,2,4,9,6]
[1,2,4,6,9]


for i in range(len(some_array)):
    min_num_index = i
    for j in range(i+1,len(some_array)):
        if some_array[j] < some_array[min_num_index]:  #일단 가장작은 인덱스만 기억해놨다가
            min_num_index = j
    some_array[i], some_array[min_num_index] = some_array[min_num_index], some_array[i]


print(some_array)




# 처음구현 했던 알고리즘===============================================

# for i in range(len(some_array)):
#     current_num = some_array[i]
#     min_num = some_array[i]
#     min_num_index = i
#     for j in range(i+1,len(some_array)):
#         print(f"i번재 {i} j번째 {j} 현재숫자 {current_num} 최소숫자 {min_num} 인덱스 {min_num_index}")
#         if some_array[i] > some_array[j]:
#             min_num = some_array[j]
#             min_num_index = j
#             print(f"최소숫자의 인식 {min_num} 인덱스 {min_num_index}")
#     if min_num < current_num:
#         print(f"숫자 체인지 {some_array[i], some_array[min_num_index]}")
#         some_array[i], some_array[min_num_index] = some_array[min_num_index], some_array[i]




