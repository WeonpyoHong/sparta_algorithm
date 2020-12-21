from collections import deque

c = 11
b = 2

# 코니의 위치 변화
# 코니는 청음 위치에서 1초후 1만큼, 매초마다 이전 이동거리 +1만큼 움직입니다.
# 즉, 증가하는 속도가 1초마다 1씩 증가한다는 소리죠.

# 속도
# 1 2 3 4 5 6 7 8 9

# 위치
# 3 4 6 9 13....

# 브라운의 위치 변화

# B - 1, B + 1, 2 * B
# 2
# 1-1. 2 - 1 = 1
# 1-2. 2 + 1 = 3
# 1-3. 2 * 2 = 4

# 브라운의 위치는 변화무쌍 함

# 모든 경우의 수를 다 나열(탐색)해야겠구나 ===> BFS를 써야겠구나

# "잡았다!"라는 의미는 똑같은 시간에 똑같은 위치에 존재해야 함

# 규칙적 -> 배열 / 자유자재 -> 딕셔너리

# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶음

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))    #위치와 시간이 동시에 일치해야지만 만남
    visited = [{} for _ in range(200001)]    # 200000개의 딕셔너리를 배열에 넣음

    #[{},{},{},{},{},{}]

    # visited[위치][시간]
    # visited[3]에 5라는 키가 있냐? 라고 3위치에 5초에 간적이 있냐?
    # visited[cony_loc] time

    # 모든 위치에 몇초에 갈 수 있는지
    # 0    1  2  -> visited[2] = { 0 : True, 2: True }
    # 2 -> 1  0  -> visited[1] = { 1 : True }
    #   -> 3  2  -> visited[3] = { 1 : True }
    #   -> 4  3  -> visited[4] = { 1 : True }
    #         4
    #         8


    # visited[0] = {
    #     2: True
    # }
    # visited[1] = {
    #     1: True,
    #     3: True,
    #     4: True
    # }
    # visited[2] = {
    #     0: True,
    #     2: True,
    #     3: True,
    #     4: True,
    #     8: True
    # }
    # visited[time][cony_loc]     #시간과 위치를 알고있으면
    # visited[1][3]
    # 3 in visited[1] 가 충족을 함 ===> 도달했는지 안 도달했는지를 저장할 수 있게


    while cony_loc <= 200000:
        cony_loc += time    # 시간만큼 +1 +2 +3 +4
        if time in visited[cony_loc]:
            return time

        for i in range(0,len(queue)):  # 현재 큐의 길이만큼 반복
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                queue.append((new_position, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!