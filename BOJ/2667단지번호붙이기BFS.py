'''
https://www.acmicpc.net/problem/2667
풀이
BFS방식
'''
import sys

N = int(input())
matrix = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
d_x = [1,0,-1,0]
d_y = [0,-1,0,1]

def bfs(x, y, cnt):
    global house
    queue = []
    queue.append((x, y))
    visited[x][y] = cnt
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if  visited[new_x][new_y] == 0 and matrix[new_x][new_y] == '1':
                    visited[new_x][new_y] = cnt
                    queue.append((new_x, new_y))
                    house += 1

cnt = 0
house = 1
house_cnt = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and visited[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)
            house_cnt.append(house)
            house = 1
#print(cnt)
print(len(house_cnt))
for i in sorted(house_cnt):
    print(i)




