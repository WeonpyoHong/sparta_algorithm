finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 순차탐색 - 2

def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:    # 빅오표기법으로 O(N)만큼의 시간복잡도
        find_count += 1
        if target == number:
            print(find_count)
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True