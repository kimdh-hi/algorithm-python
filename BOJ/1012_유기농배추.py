'''
풀이

BFS
1. 입력 예시대로 입력 받음
2. 2차원 배열에 배추의 좌표값을 1로 초기화
3. BFS재귀호출
    3-1 BFS로 입력되는 좌표는 배추가 존재하는 좌표
    3-2 순회 중 재방문된 배추의 좌표를 무시하도록 호출된 배추의 좌표는 0으로 초기화
    3-3 왼쪽, 오른쪽, 위, 아래로 순회하도록 방향을 지정할 배열 할당
    3-4 farm배열의 크기를 초과하는 때에는 continue를 통해 이동좌표만을 변경
    3-5 이동 후 배추좌표의 값이 1이라면 해당 좌표를 매개변수로하여 재귀호출
    3-6 재귀호출된 좌표는 0이 되고 다시 왼,위,오,아 순으로 탐색 반복
4. BFS에서 빠져나온 것은 인접한 배추가 없다는 뜻이므로 다음 배추좌표가 들어가기 전에 벌레 마리수를 증가
'''
import sys
sys.setrecursionlimit(10000)

d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]

def bfs(x, y):
    farm[x][y] = 0
    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
            continue
        if farm[new_x][new_y] == 1:
            bfs(new_x, new_y)

T = int(input())
for _ in range(T):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    farm = [[0] * n for _ in range(m)]
    for _ in range(k): # 배추심기
        cabbage = list(map(int, sys.stdin.readline().split()))
        farm[cabbage[0]][cabbage[1]] = 1
    bug_cnt = 0
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                bfs(i,j)
                bug_cnt += 1
    print(bug_cnt)


# import sys
# sys.setrecursionlimit(50000)
#
# d_x = [-1, 0, 1, 0]
# d_y = [0, 1, 0, -1]
#
# def dfs(x, y):
#     farm[x][y] = 0
#     for i in range(4):
#         new_x = x + d_x[i]
#         new_y = y + d_y[i]
#         if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
#             continue
#         if farm[new_x][new_y] == 1:
#             dfs(new_x, new_y)
#
# N = int(input())
# for _ in range(N):
#     m,n,k = list(map(int,sys.stdin.readline().split()))
#     farm = [[0] * n for _ in range(m)]
#     for _ in range(k):
#         link = list(map(int,sys.stdin.readline().split()))
#         farm[link[0]][link[1]] = 1 # 배추 위치
#     cnt = 0
#     for i in range(m):
#         for j in range(n):
#             if farm[i][j] == 1:
#                 for i in range(m):
#                     print(farm[i])
#                 dfs(i, j)
#                 cnt += 1
#     print(cnt)