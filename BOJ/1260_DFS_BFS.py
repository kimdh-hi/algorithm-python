n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def dfs(v, visited):
    visited.append(v)
    print(v, end = ' ')
    for i in range(1, n+1):
        if matrix[v][i] == 1 and i not in visited:
            dfs(i, visited)

def bfs(v):
    queue = [v]
    visited = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if matrix[v][i] == 1 and i not in visited:
                queue.append(i)
                visited.append(i)
dfs(v, [])
print()
bfs(v)
