shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        l = 0
        r = len(menus) - 1
        flag = False
        while l <= r:
            m = (l+r)//2
            if order is menus[m]:
                flag = True
                break
            elif order < menus[m]:
                r = m-1
            else:
                l = m+1
        if not flag:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)