import sys
from collections import deque

# def bfs(s):
#     q = deque([s])
#     visited = [0] * n
#
#     while q:
#         v = q.popleft()
#         for i in matrix[v]:
#             if not visited[i]:
#                 visited[i] = 1
#                 q.append(i)
#     print(*visited)
#
# n = int(input())
# matrix = [[] for _ in range(n)]
#
# for i in range(n):
#     arr = list(map(int, sys.stdin.readline().split()))
#     for j in range(n):
#         if arr[j] == 1:
#             matrix[i].append(j)
# print(matrix)
# for i in range(n):
#     bfs(i)


'''
dfs방식으로 그래프를 순회하며 visited배열을 갱신하며 방문했는 지를 출력
'''
import sys
from collections import deque

n = int(input())
visited = []
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
matrix.sor
def dfs(v):
    for i in range(n):
        if matrix[v][i] and i not in visited:
            print(i)
            visited.append(i)
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if j in visited:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
print(visited)
