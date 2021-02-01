from collections import deque
n, m = map(int, input().split())
matrix = [[0] * 30 for _ in range(30)]
check = [0] * 30
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1

q = deque()
q.append(1)
lv = 0

while q:
    v = q.popleft()
    for i in range(2, n+1):
        if matrix[v][i] == 1 and check[i] == 0:
            check[i] = check[v]+1
            q.append(i)

for i in range(len(check)):
    if check[i] > 0:
        print(i, " : ",check[i])



