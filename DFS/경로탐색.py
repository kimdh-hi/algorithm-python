'''
DFS 경로탐색

방향 없는 그래프
1부터 n정점까지의 경로의 수 출력
'''
n, m = map(int, input().split()) # n=정점수 m=간선수
matrix = [[0]*30 for _ in range(30)]
check = [0] * 30 # 정점 방문여부 체크 배열
ans = 0

# 인접행렬 초기화
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1

def dfs(v):
    global ans
    if v == n: # 방문한 정점이 목적지인 n과 같은 경우
        ans += 1 # 경로수 + 1
    else:
        for i in range(1, n+1): # 다음 정점으로 이동 가능 여부 확인
            if matrix[v][i] == 1 and check[i] == 0: # 다음 정점으로의 경로가 있고, 다음 정점이 방문되지 않았는 지
                check[i] = 1 # 방문체크
                dfs(i) # 다음 방문되는 정점으로 재귀
                check[i] = 0 # 재귀를 마치고 돌아올 때 방문했던 정점을 미방문 처리

check[1] = 1 # 1번 정점에서 시작하므로 체크 후 함수수행
dfs(1)
print(ans)




'''
입력예시
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
'''
