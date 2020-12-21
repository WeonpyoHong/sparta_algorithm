from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    c = cony_loc
    b = brown_loc
    time = 0
    c_move = 1
    print("처음 위치 b위치:", b, "c위치:", c)
    while 0 <= c <= 200000 and 0 <= b <= 200000:

        if (c - b) > 1:
            b = 2 * b
        elif (c - b) == 1:
            b = b + 1
        else:
            b = b - 1

        c_move = c_move + 1
        c = c + c_move

        time += 1
        print("b위치:", b, "c위치:", c)
        if b == c:
            break

    return time


print(catch_me(c, b))  # 5가 나와야 합니다!