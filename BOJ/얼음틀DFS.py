import sys

n, m = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    matrix.append(arr)


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs(x - 1, y)
        dfs(x , y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1
print(cnt)