
# 소수 배열로 반환하기

# 더 빠른 알고리즘 찾기 =============================


input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for num in range(2, number + 1):

        # 만약 num이 20 이라고 한다면
        # n은 2 3 4 5 6 7 8 9 10 11 ... 19 검사
        # 2로 나누어 떨어지면 4, 6, 8은 볼 것도 없음
        # 2 ~ n - 1 중에서 소수인 녀석들만 검사해도 됨

        for n in prime_list:
            if num % n == 0:
                break
        else:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)
