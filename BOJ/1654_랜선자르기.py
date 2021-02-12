import sys

input = sys.stdin.readline

n, m = map(int, input().split())
line = []
for _ in range(n):
    line.append(int(input()))

low = 1
high = max(line)
ans = 0
while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for l in line:
        cnt += (l // mid)
    if cnt >= m:
        if mid > ans:
            ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)