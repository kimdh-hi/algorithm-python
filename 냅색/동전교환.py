
n = int(input())

coin = list(map(int, input().split()))
target = int(input())
dp = [1000] * (target+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], target+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)

print(dp[target])