array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


# 일단 병합의 개념

# 일단 각각의 배열이 순서대로 정리되어 있어야함 ===> 합칠때 어떻게?

def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1
    # 일단 1번 배열이 없는 경 (2번 배열로 채우기)
    if array1_index == len(array1):
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1
    # 일단 2번 배열이 없는 경 (1번 배열로 채우기)
    if array2_index == len(array2):
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!