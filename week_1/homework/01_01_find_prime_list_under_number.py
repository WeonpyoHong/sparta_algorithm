
# 소수 배열로 반환하기

# 소수는 자기자신과 1외에는 아무것도 나눌 수 없음

input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for num in range(2, number + 1):
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            prime_list.append(num)
    return prime_list



result = find_prime_list_under_number(input)
print(result)


