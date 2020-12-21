
# 소수 배열로 반환하기

# 더 빠른 알고리즘 찾기 =============================


input = 20

# 주어진 자연수 N이 소수이기 위한 필요충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중하나는 반드시 N의 제곱근 이하

def find_prime_list_under_number(number):
    prime_list = []

    for num in range(2, number + 1):
        for n in prime_list:
            print(num, n)
            if num % n == 0 and n * n <= num :
                break
        else:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)




# https://qastack.kr/programming/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr