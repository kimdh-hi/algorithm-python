from sys import stdin

n, m = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))

lt = 0
rt = max(tree)
while lt <= rt:
    mid = (lt + rt) // 2
    tmp = 0
    for t in tree:
        tmp += t - mid if t -mid > 0 else 0
    if tmp >= m:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)

