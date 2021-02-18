
from collections import deque

n = 7

maze = [list(map(int, input().split())) for _ in range(n)]
d_x = [1,0,-1,0]
d_y = [0,1,0,-1]
visited = [[0]*n for _ in range(n)]
dq = deque()
dq.append((0,0))
maze[0][0] = 1
while dq:
    x, y = dq.popleft()
    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]
        if 0 <= new_x < n and 0 <= new_y < n:
            if maze[new_x][new_y] != 1:
                maze[new_x][new_y] = 1
                dq.append((new_x, new_y))
                visited[new_x][new_y] = visited[x][y] + 1

if visited[n-1][n-1] > 0:
    print(visited[n-1][n-1])
else:
    print(-1)