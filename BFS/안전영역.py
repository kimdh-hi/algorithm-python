from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
safe = [[0] * n for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dq = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] <= 4:
            dq.append((i,j))
            arr[i][j] = -1
            while dq:
                x, y = dq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] != -1 and arr[nx][ny] <= 4:
                        dq.append((nx,ny))
                        arr[nx][ny] = -1
#출력
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
