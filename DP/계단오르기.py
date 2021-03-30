
def dfs(s):
    if dp[s] > 0:
        return dp[s]
    if s == 1 or s == 2:
        return s
    else:
        dp[s] = dfs(s-1) + dfs(s-2)
        return dp[s]

n = int(input())
dp = [0] * (n+1)
print(dfs(n))
