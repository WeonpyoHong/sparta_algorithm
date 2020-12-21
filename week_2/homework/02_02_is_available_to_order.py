shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 이진탐색을 통해 확인하는 방법 구현

# 시간 복잡도 O(N * log N) +  O(M * log N)
# ===> O (N + M) log N


def is_available_to_order(menus, orders):

    def is_existing_target_number_binary(order, menus):    # 시간복잡도가 얼마나 걸릴까?
        start_index = 0
        end_index = len(menus) - 1
        mid_index = (start_index + end_index) // 2
        while start_index <= end_index:                 # 이진탐색 O(log N)
            if menus[mid_index] == order:
                return True
            elif menus[mid_index] < order:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
            mid_index = (start_index + end_index) // 2

        return False

    menus.sort()    # 정렬의 시간 복잡도는 배열의 길이를 N이라고 한다면 O(N * log N)

    for order in orders:   # M * 이진탐색 O(log N)
        if not is_existing_target_number_binary(order, menus):
            return False

    return True



result = is_available_to_order(shop_menus, shop_orders)
print(result)