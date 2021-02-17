'''
노드의 수가 많아진다면 인접리스트 사용 !!
'''
def dfs(v):
    global cnt
    check[v] = 1
    if v == n:
        cnt += 1
    else:
        for newv in matrix[v]:
            if check[newv] == 0:
                dfs(newv)
                check[newv] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n+1)]
    check = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        # a에서 방문될 수 있는 정점인 b를 a에 추가
        matrix[a].append(b)
    # 인접리스트 출력
    # for m,i in enumerate(matrix):
    #     print(i, m)
    cnt = 0
    dfs(1)
    print(cnt)
