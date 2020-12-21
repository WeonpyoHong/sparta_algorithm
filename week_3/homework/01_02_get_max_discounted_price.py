shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# sort(), pop() 이용한 풀이법 ==============================

def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()

    sum_of_prices = 0

    while shop_prices:
        price = prices.pop()
        if coupons:
            coupon = coupons.pop()
            sum_of_prices += price * (1 - coupon * 0.01)
        else:
            sum_of_prices += price

    return sum_of_prices


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.