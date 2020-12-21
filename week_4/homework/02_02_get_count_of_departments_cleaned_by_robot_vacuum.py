current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 1. 현재 위치를 청소한다.
# BFS를 구현 visited = [1, 2, 3]
# 0은 청소하기 않은 장소
# 1은 청소하지 못하는 장소
# 2는 청소한 장소

# 2. 현재위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로
# 탐색을 진행한다. (-> 방향)

#방향의 개념
#    row  col
# 북  -1   0
# 동   0   1
# 남   1   0
# 서   0  -1

dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]
#     북  동  남  서

# 북 왼 회전? (북 -> 서) 0 -> 3
# 서 왼 회전? (서 -> 남) 3 -> 2
# 남 왼 회전? (남 -> 동) 2 -> 1
# 동 왼 회전? (동 -> 북) 1 -> 0

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
# 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.

# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고
# 2번으로 돌아간다.(한번 더 왼쪽으로 회전)

# c. 네 방향 모두 청소가 되어있거나 벽인 경우에는
# 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# (모든 방향이 청소되어 있다면 뒤로 한칸 후진 하면 됨)


# 북 뒤 후진? (남) 0 -> 2
# 서 뒤 후진? (동) 3 -> 1
# 남 뒤 후진? (북) 2 -> 0
# 동 뒤 후진? (서) 1 -> 3

def get_d_index_when_go_back(d):
    return (d + 2) % 4


# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서,
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.



def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])  # 현재위치 및 방향 기록

    while queue:
        print(queue)
        r, c, d = queue.pop(0)
        temp_d = d      # 현재의 방향

        for i in range(4): # 4방향을 다 확인
            #일단 왼쪽으로 회전한다면
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            #회전시에 새로운 좌표
            new_r = r + dr[temp_d]
            new_c = c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break
            # c. 네 방향 모두 청소가 되어있거나 벽인 경우에는
            # 바라보는 방향을 유지한 채로 한칸 후진을 하고 2번으로 돌아간다.
            elif i == 3: # 4방향을 다 확인했는데 청소할 곳이 없다면
                new_r = r + dr[get_d_index_when_go_back(temp_d)]
                new_c = c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])

                # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서,
                # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned



# 57 이 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))



print(current_room_map)


#===================================================

current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 1, 1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 2, 2, 2, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 2, 0, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]