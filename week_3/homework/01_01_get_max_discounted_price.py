shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 조건 필요: 할인쿠폰은 한제품에 한번씩만 적용

def get_max_discounted_price(prices, coupons):
    def insertion_sorting(array):
        n = len(array)
        for i in range(1, n):
            for j in range(i):
                if array[i - j - 1] > array[i - j]:
                    array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
                else:
                    break

    insertion_sorting(prices)
    insertion_sorting(coupons)

    total_price = 0

    price_len = len(prices)
    coupons_len = len(coupons)

    # print("길이:", price_len, coupons_len )
    while price_len >= 1 and coupons_len >= 1 :
            total_price += prices.pop() * (100 - coupons.pop())/100
            price_len -= 1
            coupons_len -= 1

    while price_len >= 1:
        total_price += prices.pop()
        price_len -= 1

    return total_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.