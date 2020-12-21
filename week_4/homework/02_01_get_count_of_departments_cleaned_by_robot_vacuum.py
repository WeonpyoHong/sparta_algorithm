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


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    position = (r, c)
    direction = d
    room_map[position[0]][position[1]] = 2
    count = 1
    # print(room_map)
    print(position)
    # if direction == 0:
    #     x = position[1] - 1
    #     y = position[0]
    # elif direction == 3:
    #     x = position[1]
    #     y = position[0] - 1
    # elif direction == 2:
    #     x = position[1] + 1
    #     y = position[0]
    # elif direction == 1:
    #     x = position[1]
    #     y = position[0] + 1


    while position[0] >= 0 and position[0] < (len(room_map)) and position[1] >= 0 and position[1] < (len(room_map[0])):
        print("진입")
        count += 1
        print("현재방향", direction)
        if direction == 0:
            if room_map[position[0]][position[1]-1] == 0:
                direction = 3
                room_map[position[0]][position[1]-1] = 2
                position = (position[0],position[1]-1)
                print(position)
                continue

            elif room_map[position[0]+1][position[1]] == 0:
                direction = 2
                room_map[position[0] + 1][position[1]] = 2
                position = (position[0] + 1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1]+1] == 0:
                direction = 1
                room_map[position[0]][position[1]+1] = 2
                position = (position[0], position[1]+1)
                print(position)
                continue

            elif room_map[position[0]-1][position[1]] == 0:
                direction = 0
                room_map[position[0]-1][position[1]] = 2
                position = (position[0]-1, position[1])
                print(position)
                continue
            else:
                if room_map[position[0]+1][position[1]] == 1:
                    print(position)
                    break
                else:
                    position = (position[0]+1, position[1])
                    print(position)
                    continue


        if direction == 1:
            if room_map[position[0] - 1][position[1]] == 0:
                direction = 0
                room_map[position[0] - 1][position[1]] = 2
                position = (position[0] - 1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1] - 1] == 0:
                direction = 3
                room_map[position[0]][position[1] - 1] = 2
                position = (position[0], position[1] - 1)
                print(position)
                continue

            elif room_map[position[0]+1][position[1]] == 0:
                direction = 2
                room_map[position[0]+1][position[1]] = 2
                position = (position[0]+1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1]+1] == 0:
                direction = 1
                room_map[position[0]][position[1]+1] = 2
                position = (position[0], position[1]+1)
                print(position)
                continue

            else:
                if room_map[position[0]][position[1]-1] == 1:
                    print(position)
                    break
                else:
                    position = (position[0], position[1]-1)
                    print(position)
                    continue

        if direction == 2:
            if room_map[position[0]][position[1]+1] == 0:
                direction = 1
                room_map[position[0]][position[1]+1] = 2
                position = (position[0], position[1]+1)
                print(position)
                continue

            elif room_map[position[0]-1][position[1]] == 0:
                direction = 0
                room_map[position[0]-1][position[1]] = 2
                position = (position[0]-1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1]-1] == 0:
                direction = 3
                room_map[position[0]][position[1]-1] = 2
                position = (position[0], position[1]-1)
                print(position)
                continue

            elif room_map[position[0]+1][position[1]] == 0:
                direction = 2
                room_map[position[0]+1][position[1]] = 2
                position = (position[0]+1, position[1])
                print(position)
                continue

            else:
                if room_map[position[0]-1][position[1]] == 1:
                    print(position)
                    break
                else:
                    position = (position[0]-1, position[1])
                    print(position)
                    continue

        if direction == 3:
            if room_map[position[0] + 1][position[1]] == 0:
                direction = 2
                room_map[position[0] + 1][position[1]] = 2
                position = (position[0] + 1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1] + 1] == 0:
                direction = 1
                room_map[position[0]][position[1] + 1] = 2
                position = (position[0], position[1] + 1)
                print(position)
                continue

            elif room_map[position[0]-1][position[1]] == 0:
                direction = 0
                room_map[position[0]-1][position[1]] = 2
                position = (position[0]-1, position[1])
                print(position)
                continue

            elif room_map[position[0]][position[1]-1] == 0:
                direction = 3
                room_map[position[0]][position[1]-1] = 2
                position = (position[0], position[1]-1)
                print(position)
                continue

            else:
                if room_map[position[0]][position[1]+1] == 1:
                    print(position)
                    break
                else:
                    position = (position[0], position[1]+1)
                    print(position)
                    continue
    print(room_map)
    return count



# 52 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))


print(current_room_map)
