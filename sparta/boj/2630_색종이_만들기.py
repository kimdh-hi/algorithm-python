
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_cnt = 0
blue_cnt = 0
def dfs(x, y, n):
    global white_cnt
    global blue_cnt
    v = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if v is not paper[i][j]:
                dfs(x, y, n//2) # 1사분면
                dfs(x+n//2, y, n//2) # 2사분면
                dfs(x, y+n//2, n//2) # 3사분면
                dfs(x+n//2, y+n//2, n//2) # 4사분면
                return
    if  v == 0:
        white_cnt += 1
    else:
        blue_cnt += 1

dfs(0, 0, n)
print(white_cnt)
print(blue_cnt)