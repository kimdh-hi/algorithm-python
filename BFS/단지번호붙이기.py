from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
dq = deque()
ans = []
anscnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = 0
            dq.append((i,j))
            arr[i][j] = 0
            while dq:
                cnt += 1
                x, y = dq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1:
                        dq.append((nx,ny))
                        arr[nx][ny] = 0
            ans.append(cnt)
            anscnt += 1

print(anscnt)
ans = sorted(ans)
for a in ans:
    print(a)
