import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    req = k - stock

    arr = []
    for i in range(len(dates)):
        arr.append((dates[i], supplies[i]))
    arr = sorted(arr, key=lambda x: x[1], reverse=True)
    stock_sum = 0
    cnt = 0
    for a in arr:
        if stock_sum < req and a[0] < k:
            stock_sum += a[1]
            cnt += 1

    return cnt


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))