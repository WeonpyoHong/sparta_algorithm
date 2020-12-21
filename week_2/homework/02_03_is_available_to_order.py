shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# Set 사용해보기
# set는 이진탐색보다 더 효율적인 자료구조형

# a = set([1, 2, 3, 4, 5, 1, 2, 3])

def is_available_to_order(menus, orders):
    # 배열을 set로 변환하기
    menus_set = set(menus)     # 세트로 정렬하는데  O(N) 만큼의 시간이 걸림

    for order in orders:     # O (M) 만큼의 시간이 걸림
        if order not in menus_set:   # 존재여부는 O(1) 만큼의 시간이 걸림     =====> O(N) + O(M) = O(N+M)
            return False

    return True



result = is_available_to_order(shop_menus, shop_orders)
print(result)