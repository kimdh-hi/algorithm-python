
n, m = map(int, input().split())
node = []
for i in range(n):
    node.append(map(int, input().split()))

matrix = [[0]*n]*n

for i in range(n):
    i, j, d = node[i]
    matrix[i][j] = d

for i in range(n):
    for j in range(n):
        print(matrix[i][j])
    print()


