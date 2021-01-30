'''
BFS, 브루트포스

바이러스 = 2
벽 = 1
빈공간 = 0

1. 바이러스는 인접한 곳으로 퍼져 나감
2. 벽으로 둘러싸이면 퍼져나가지 못함
3. 3개의 벽을 사용하여 바이러스가 퍼진 후 0의 개수

풀이
1. matrix에서 임의의 0인 곳에 벽을 3개 세움
2. 바이러스를 퍼뜨림 bfs
3. 안전구역 counting

pypy통과
python3 시관초과 ..
'''

import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d_x = [1,0,-1,0]
d_y = [0,-1,0,1]
q = deque()

def bfs():
    global safe_area
    w_map = copy.deepcopy(matrix)
    # 바이러스 있는 모든 좌표를 큐에 넣고 bfs시작
    for i in range(n):
        for j in range(m):
            if w_map[i][j] == 2:
                q.append([i, j])

    # bfs (virus spread)
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if 0 <= new_x < n and 0 <= new_y < m:
                if w_map[new_x][new_y] == 0:
                    w_map[new_x][new_y] = 2
                    q.append([new_x, new_y])

    safe_cnt = 0
    for i in w_map:
        safe_cnt += i.count(0) # 0(빈 공간) counting
    safe_area = max(safe_area, safe_cnt) # 빈 공간의 최대값 저

# 3개 벽을 세우는 모든 경우
def setWall(cnt):
    if cnt == 3: # 벽이 3개가 된 경우 bfs를 호출하여 바이러스 퍼뜨림
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                setWall(cnt + 1)
                matrix[i][j] = 0

safe_area = 0
setWall(0)
print(safe_area)



