
def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1:
            #arr[nx][ny] = 0
            dfs(nx, ny)

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
ans = []
anscnt = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i,j)
            anscnt += 1
            ans.append(cnt)
print(anscnt)
ans = sorted(ans)
for a in ans:
    print(a)