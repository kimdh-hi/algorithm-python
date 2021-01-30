'''
풀이

DFS방식
:DFS재귀 호출시 전역번수인 cnt를 매개변수로 주고 외부에서 증가시키며 단지별 cnt값 유지
'''

import sys


def dfs(x,y,cnt):
    global house

    visited[x][y] = 1

    if matrix[x][y] == '1':
        house += 1
    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]
        if 0 <= new_x < N and 0 <= new_y < N:
            if visited[new_x][new_y] == 0 and matrix[new_x][new_y] == '1':
                dfs(new_x, new_y, cnt)

N = int(input())
matrix = [sys.stdin.readline().rstrip() for i in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
d_x = [0,1,0,-1]
d_y = [-1,0,1,0]
cnt = 1
house = 0
house_cnt = []
for x in range(N):
    for y in range(N):
        if matrix[x][y] == '1' and visited[x][y] == 0:
            dfs(x,y,cnt)
            house_cnt.append(house)
            house = 0
            cnt += 1

print(len(house_cnt))
for i in sorted(house_cnt):
    print(i)






