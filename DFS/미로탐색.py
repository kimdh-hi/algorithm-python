'''
0,0부터 [n-1,n-1]까지의 경우의 수
'''
def dfs(x,y):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
    else:
        for i in range(4):
            nx = x + d_x[i]
            ny = y + d_y[i]
            if 0<=nx<n and 0<=ny<n and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                dfs(nx, ny)
                maze[nx][ny] = 0

ans = 0
n = 7
maze = [list(map(int, input().split())) for _ in range(n)]
d_x = [-1,0,1,-0]
d_y = [0,1,0,-1]
maze[0][0] = 1
dfs(0,0)
print(ans)
