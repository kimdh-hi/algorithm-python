'''
https://www.acmicpc.net/problem/7576
BFS

틀림

기존 bfs와 다른점
1. 탐색을 시작할 수 있는 노드가 한 개가 아님
2. 여러 노드에서 동시에 탐색을 허용
3. 큐에 시작 가능한 노드를 모두 담은 후 시작 Point!!
4. 노드 방문 기록을 남길 추가적인 배열이 필요 없음

왜 틀린지 모르겠음.
'''

import sys
from collections import deque

m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))
# quit_cond = min(map(min, box))
# if quit_cond >= 1: # 최소값이 1 이상 즉, 토마토가 모두 담긴 상태라면 0출력 종료
#     print(0)
#     exit()


queue = deque()
d_x = [-1,0,1,0]
d_y = [0,-1,0,1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if box[new_x][new_y] == 0:
                    box[new_x][new_y] = box[x][y] + 1
                    queue.append([new_x, new_y])

# 시작 가능한 좌표를 큐에 저장
# 익은 토마토가 있는 모든 위치
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
bfs()
if 0 in box:
    print(-1)
else:
    print(max(map(max, box))-1)