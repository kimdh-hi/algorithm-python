
n = int(input())
rocks = []
for i in range(n):
    a,b,c = map(int, input().split())
    rocks.append((a,b,c))
rocks.sort(reverse=True)
dp = [0] * n
dp[0] = rocks[0][1]
res = rocks[0][1]
for i in range(1, n):
    maxh = 0
    for j in range(i-1, -1, -1):
        if rocks[j][2] > rocks[i][2] and dp[j] > maxh:
            maxh = dp[j]
    dp[i] = maxh + rocks[i][1]
    if dp[i] > res:
        res = dp[i]

print(res)