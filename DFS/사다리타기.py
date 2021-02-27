'''
도착 지점으로부터 왼쪽,오른쪽,위 순으로 탐색하며 재귀
    왼쪽,오른쪽을 먼저 탐색하는 것이 Point!
'''

import sys

def dfs(h, w):
    if h == 0:
        print(w)
        sys.exit(0)
    else:
        for i in range(3):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0<=nh<n and 0<=nw<n and check[nh][nw] == 0 and arr[nh][nw] == 1:
                check[nh][nw] = 1
                dfs(nh, nw)
                check[nh][nw] = 0



n = 10
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
dw = [1,-1,0]
dh = [0,0,-1]
for i in range(n):
    if arr[n-1][i] == 2:
        check[n-1][i] = 1
        dfs(n-1, i)