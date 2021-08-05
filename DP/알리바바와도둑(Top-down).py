

def dfs(x, y):
    if x==0 and y==0:
        return dp[x][y]
    else:
        dfs(x-1, y)
        
        dfs(x, y-1)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dfs(n-1, n-1)


