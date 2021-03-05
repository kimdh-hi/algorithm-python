import sys
def dfs(x,y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and arr[nx][ny] == 1:
            arr[nx][ny] = -1
            dfs(nx,ny)

dx = [1,0,-1,0,-1,1,-1,1]
dy = [0,-1,0,1,-1,1,1,-1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: sys.exit(0)
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = -1
                dfs(i,j)
    print(cnt)
