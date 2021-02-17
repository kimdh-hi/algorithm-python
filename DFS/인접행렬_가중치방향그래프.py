
n, m = map(int, input().split())
node = []
for i in range(m):
    node.append(map(int, input().split()))

matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y, d = node[i]
    print(x,y,d)
    matrix[x][y] = d

for i in range(1,n+1):
    for j in range(1,n+1):
        print(matrix[i][j], end=' ')
    print()


