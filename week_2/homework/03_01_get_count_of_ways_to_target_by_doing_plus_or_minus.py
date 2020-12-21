numbers = [1, 1, 1, 1, 1]


# 간소화해서 생각해보기 ====> 경우의 수를 다 따져야함


target_number = 3


# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 됨

result_array = []

# all_ways = result = []
# current_index = 0
# current_sum = 0
#  2,  3,  1
# +2  +3
# -2

# 재귀적으로 내부에서 경우의 수를 가진 함수를 다시 불러내어
# 모든 경우의 수를 출력하는 방법
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array):
        all_ways.append(current_sum)
        return
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum + numbers[current_index], all_ways
    )
    get_all_ways_to_by_doing_plus_or_minus(
        array, current_index + 1, current_sum - numbers[current_index], all_ways
    )


print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result_array))
print(result_array)


