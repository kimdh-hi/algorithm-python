'''
노드의 수가 많아진다면 인접행렬의 효율이 떨어질 수 있음
따라서 노드의 수가 많다면 인접리스트를 사용하도록..
'''
n, m = map(int, input().split())

def dfs(v):
    global ans
    check[v] = 1 # v번 방문 체크
    if v == n: # v가 n인 경우 (타겟=n)
        # for i in range(1,n+1): # 거쳐간 노드 출력
        #     if check[i] == 1:
        #         print(i, end = ' ')
        # print()
        ans += 1 # 경로 수 증가
        return
    else:
        # 각 정점(v)에서 1~n까지의 정점으로 이동 가능한지 확인
        # 이동 가능하다면 해당 정점이 이미 방문된 정점인지 확인
        for i in range(1, n+1):
            if matrix[v][i] == 1 and check[i] == 0:
                dfs(i) # 확인 후 방문하도록 재귀(스텍에 push)
                check[i] = 0 # 종료후 돌아올 때 방문여부 초기화

matrix = [[0]*(n+1) for _ in range(n+1)]
check = [0] * (n+1)
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1 # 방향그래프
dfs(1)
print(ans)

# 인접행렬 출력
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(matrix[i][j], end=' ')
#     print()
#

