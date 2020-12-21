import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는
# 라면 중 제일 많은 라면을 받는 게 목표
# 제일 많은 -> 정렬?!

#1. 현재 재고의 상태에 따라 최고값을 받아야 함(동적으로 변경되는 상태)
#2. 제일 많은 값만 가져가면 됨

#1. 데이터를 넣을 때마다 최소/최대값을 동적으로 변경시키며
#2. 최소/최대값을 발로 꺼낼 수 있는 자료구조
# ======> 힙(heap)

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0   # 현재 몇일날째인지 (오늘이 몇일인지에 따라서 가져올 수 있는 재고가 다름)
    max_heap = []

    while stock < k:
        # date를 기준으로 반복을 해야함
        for date_index in range(current_day_index, len(dates)):
            print(date_index, dates[date_index],"일째", supplies[date_index],"채울재고", stock,"현재재고")
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])  # (굶어죽기 전에 해당하는 날짜 내에서) 최대값 추가하기
            else:
                current_day_index = date_index
                break
        print("max_heap", max_heap)
        answer += 1
        stock += -heapq.heappop(max_heap)
        print("stock is: ", stock)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))