array = [5, 3, 2, 1, 6, 8, 7, 4]


# 병합 정렬 =======> 분할정복(Divide and Conquer)의 개념을 이용

# 분할 단계 O(logN) + 병합단계 O(N) ====> 전체 시간복잡도 (N * logN) 만큼 걸림

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[0:mid])
    right_array = merge_sort(array[mid:len(array)])
    print(array)
    print('left_array', left_array)
    print('right_array', right_array)

    return merge(left_array, right_array)     # 분할단계 ====> 시간 복잡도  logN  만큼의 시간   N / 2^k = 1


def merge(array1, array2):
    result = []        # 병합단계 ===> 시간복잡도 array1길이 + array2길이 = array 즉, O(N)만큼
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!