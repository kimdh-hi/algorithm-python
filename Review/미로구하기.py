

def dfs(x, y):
    global res
    if x == n and y == n:
        res += 1
    else:
        for i in range(4):
            nx = x_d[i]
            ny = y_d[i]
           if 0<=nx<=n and 0<=ny<=n and maze[nx][ny]==0:
                maze[nx][ny]=1
                dfs(nx,ny)
                maze[nx][ny]=0

if __name__ == "__main__":
    x_d = [1, 0 ,-1, 0]
    y_d = [0, -1, 0, 1]
    res = 0
    n = 6