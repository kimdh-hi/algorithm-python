'''
풀이

1. (0,0) 좌표를 큐에 넣고 시작
2. 큐에서 pop후 나온 좌표가 오,왼,위,아래로 이동가능하다면 큐에 삽입
    큐에 삽입시 거리를 표시하는 행렬에 시작 좌표로부터 떨어진 거리를 저장
3. 거리를 저장하는 배열에 저장된 값은 시작좌표에서 임의 인덱스까지의 최단거
'''

import sys
d_x = [1,0,-1,0]
d_y = [0,1,0,-1]
#d_x, d_y = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
maze = [sys.stdin.readline().rstrip() for i in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]
queue = [(0,0)]     # 시작좌표
distance[0][0] = 1   # 시작좌표 marking

while queue:
    x, y = queue.pop(0)

    if x == n-1 and y == m-1:
        print(distance[x][y])
        break
    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]
        if 0 <= new_x < n and 0 <= new_y < m:
            if distance[new_x][new_y] == 0 and maze[new_x][new_y] == '1':
                queue.append((new_x,new_y))
                distance[new_x][new_y] = distance[x][y] + 1







