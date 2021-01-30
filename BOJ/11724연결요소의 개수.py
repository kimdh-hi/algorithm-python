'''
연결요소의 개수

풀이

DFS
각 정점 간 연결되어 있는 덩어리의 개수
1. 양방향 그래프로 초기화
2. 1부터 n+1까지 방문되었던 노드를 제외하고 dfs함수 수행
3. dfs가 한번 끝날 때마다 한 개 덩어리가 count된
'''
import sys
sys.setrecursionlimit(50000)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
visited = []

def dfs(v):
    visited.append(v)
    for i in range(1, n+1):
        if matrix[v][i] and i not in visited:
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        cnt += 1

print(cnt)
