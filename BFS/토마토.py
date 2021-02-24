from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
check = [[0]*n for _ in range(m)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = -214000000
dq = deque()
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            dq.append((i,j)) # 토마토가 들어있는 위치
            check[i][j] = 0
while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and arr[nx][ny] == 0:
            arr[nx][ny] = 1
            check[nx][ny] = check[x][y] + 1
            dq.append((nx, ny))
flag = 1
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            flag = 0
            break
if flag:
    for c in check:
        if ans < max(c):
            ans = max(c)
    print(ans)
else:
    print(-1)


