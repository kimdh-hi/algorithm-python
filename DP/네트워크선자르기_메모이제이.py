
def dfs(l):
    if dp[l] > 0:
        return dp[l]
    if l == 1 or l == 2:
        return l
    else:
        dp[l] = dfs(l-1) + dfs(l-2)
        return dp[l]

n = int(input())
dp = [0]*(n+1)
print(dfs(n))