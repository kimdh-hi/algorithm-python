'''
인접행렬 (가중치 그래프)

n = 정점의 수
m = 간선의 수

[1,2,7] => 1에서 2로 7의 가중치로
[1,3,4] => 1에서 3으로 4의 가중치로
'''


n, m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

map = [[0 for _ in range(n)]] * n


