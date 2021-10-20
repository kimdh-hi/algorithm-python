
def solve(h, m):
    if m-45 < 0:
        tmp = m-45
        m = 60 + tmp
        if h-1 < 0:
            h = 23
        else:
             h -= 1
    else:
        m -= 45

    return h, m

h, m = map(int, input().split())

h, m = solve(h, m)
print(h, m)