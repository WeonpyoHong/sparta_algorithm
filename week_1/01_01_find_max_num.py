
# 최대값 찾기 -1

# 2가지 방법으로 풀기

# 1) 첫번째 방법
# for문을 2번 돌려서 실행
# 하나씩 뽑아서 for문을 도는 동안, 더 큰 숫자가 감지가 안되면 그 것이 바로 제일 큰 숫

input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:    # for문이 다 끝날때까지 break문이 한번도 실행되지 않으면 실행
            return num


result = find_max_num(input)
print(result)

# for ~ else문
# for문을 도는 동안, break가 발생하지 않으면 else문을 실행