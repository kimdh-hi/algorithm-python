import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    matrix.append(arr)
visited = [[0 for _ in range(m)] for _ in range(n)]
d_x = [1,0,-1,0]
d_y = [0,-1,0,1]

def bfs(a, b):
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if visited[new_x][new_y] == 0 and matrix[new_x][new_y] == 0:
                    q.append((new_x,new_y))
                    visited[new_x][new_y] = 1

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and matrix[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
