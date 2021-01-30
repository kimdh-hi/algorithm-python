import sys
from collections import deque

N = int(input())
m = []
for i in range(N):
    m.append(list(map(int, input().split())))

def bfs(s):
    q = deque([s])
    visited = [0] * N
    while q:
        node = q.popleft()
        for i in m[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    print(*visited)

for i in range(N):
    bfs(i)


# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if m[i][k] and m[k][j]:
#                 print(k,i,j)
#                 m[i][j] = 1
#
# print(m)
