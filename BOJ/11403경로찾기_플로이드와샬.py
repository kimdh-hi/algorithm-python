'''
플로이드 와샬
'''

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
# k - 거쳐가는 노드
for k in range(n):
    # i - 출발노드
    for i in range(n):
        # j - 도착노드
        for j in range(n):
            if matrix[i][j] == 1: continue
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
