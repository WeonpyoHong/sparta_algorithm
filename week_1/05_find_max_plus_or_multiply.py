
# 알고리즘 더 풀어보기(1)
# 곱하기 또는 더하기

input = [0, 3, 5, 6, 1, 2, 4]

input = [1, 3, 5, 6, 1, 2, 4]



# 내 풀이법 (더한것과 곱한 것 숫자 비교하기)====================

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if (multiply_sum + number) > (multiply_sum * number):
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)



# 강사님 풀이법 =================================

# 0 또는 1일때.. (더하는 게 낫다)
# 18 * 1 = 18
# 18 + 1 = 19

# 총합이 0 또는 1 일때.. (곱하면 0이 되어버리거나 그대로..)


def find_max_plus_or_multiply2(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply2(input)
print(result)



