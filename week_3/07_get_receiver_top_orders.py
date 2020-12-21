top_heights = [6, 9, 5, 7, 4]

# 스택의 개념을 이용한 문제


# [0, 0, 2, 2, 4]
# [0, 0, 0, 0, 0]

#  <- <- <- <- <-
#  6  9  5  7  4
# [0, 0, 0, 0, 4]

#  <- <- <- <-
#  6  9  5  7
# [0, 0, 0, 2, 4]

#  <- <- <-
#  6  9  5
# [0, 0, 2, 2, 4]

#  <- <-
#  6  9
# [0, 0, 2, 2, 4]

#  <-
#  6
# [0, 0, 2, 2, 4]

# [6, 9, 5, 7, 4]
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:    # 시간복잡도 O(N)   =========> 총 시간복잡도 O(N^2)
        height = heights.pop()         # (4) 3 2 1 0
        for idx in range(len(heights) - 1, -1, -1):  # O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!




# range함수에 대한 이해 ================================
for idx in range(5 - 1, 0, -1):
    print(idx)