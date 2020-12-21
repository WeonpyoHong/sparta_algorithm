seat_count = 9
vip_seat_array = [4, 7]


# 왜 피보나치 인가?

# 좌석이 i개 있다.
# 1번의 경우의 수
# i번째 좌석에 i번 티켓을 가진 사람이 그대로 앉는 경우
# 1 2 3 4 5 6 .... i
# i - 1 좌석들을 맘대로 배치가능

# 2번의 경우의 수
# i 번째 티켓을 가진 사람이 i - 1번째 앉을 경우(이런 경우는 마지막 두자리는 고정)
# 1 2 3 4 5 6 ...i - 1, i
# i - 2 좌석들을 맘대로 배치가능

# F(N) = N 명의 사람들을 좌석에 배치하는 방법
#      = (N - 1 명의 사람들을 좌석에 배치하는 방법) + (N - 2 명 사람들을 좌석에 배치하는 방법)
#      = F(N-1) + F(N-2)

# F(2) = 2
# F(3) = 3


memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    #기록하고 반환
    fibo_memo[n] = nth_fibo
    return nth_fibo



def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1    # 곱연산을 위해
    current_index = 0
    #[(1,2,3)4,(5,6),7,(8,9)]
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)      #일단 좌석의 갯수
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
