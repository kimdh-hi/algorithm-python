shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    p_idx = 0
    coupons.sort(reverse=True)
    c_idx = 0
    result = 0

    while p_idx < len(prices) and c_idx < len(coupons):
        result += prices[p_idx] * (coupons[c_idx] / 100)
        p_idx += 1
        c_idx += 1

    if p_idx < len(prices):
        for i in range(p_idx, len(prices)):
            result += prices[i]

    return int(sum(shop_prices) - result)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.