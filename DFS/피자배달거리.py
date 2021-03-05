'''
0 = 빈 곳
1 = 집
2 = 피자집

m개 피자집만을 선택할 것임 ( 부분집합 ! )
'''


def dfs(L, s):
    global ans
    if L == m:
        sum = 0
        for i in range(len(h)):
            tmp = 2147000000
            x1,y1 = h[i]
            for j in range(m):
                x2, y2 = p[check[j]]
                tmp = min(tmp, abs(x1-x2) + abs(y1-y2))
            sum += tmp
        if sum < ans:
            ans = sum
    else:
        for i in range(s, len(p)):
            check[L] = i
            dfs(L+1, i+1)

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
check = [0] * m
ans = 2147000000
h = []
p = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            h.append((i,j))
        elif arr[i][j] == 2:
            p.append((i,j))
dfs(0,0)
print(ans)