
def dfs(L):
    global cnt
    if L >= m:
        for c in ans:
            print(c, end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if not check[i]:
                check[i] = 1
                ans[L] = i
                dfs(L+1)
                check[i] = 0


n, m = map(int, input().split())
ans = [0] * m
check = [0] * (n+1)
cnt = 0
dfs(0)
print(cnt)