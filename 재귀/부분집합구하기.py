
def dfs(v):
    if v > n: # 상태노드의 상태를 저장하는 리스트 출력
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end = ' ')
        print()
    else:
        check[v] = 1 # 현재 노드의 사용을 체크
        dfs(v+1)
        check[v] = 0 # 현재 노드를 사용하지 않음을 체크
        dfs(v-1)

n = int(input())
check = [0] * (n+1) # 상태노드의 상태를 저장
dfs(n)