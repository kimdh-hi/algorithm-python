import heapq
'''
라면 재고는 하루에 하나씩 계속해서 감소한다.
라면의 재고가 k일이 되기 전까지 재고가 0미만이 되지 않도록 공급받아야 한다.
'''
ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    res = 0
    heap = []
    idx = 0
    while stock <= k:
        while idx < len(dates) and dates[idx] <= stock:
            heapq.heappush(heap, -supplies[idx]) # 최대힙
            idx += 1
        max_heap_pop = heapq.heappop(heap)
        stock = stock + -max_heap_pop
        res += 1

    return res


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))