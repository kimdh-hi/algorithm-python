import sys

def dfs(x,y,h):
    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and check[nx][ny] == 0 and arr[nx][ny] > h:
            dfs(nx,ny,h)


sys.setrecursionlimit(100000)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
cnt = 0
ans = 0

for h in range(100):
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and check[i][j] == 0:
                check[i][j] = 1
                cnt += 1
                dfs(i,j,h)
    ans = max(ans, cnt)
    if cnt == 0: break

print(ans)