
def dfs(L, score, time):
    global ans
    if time > m: return
    if L == n:
        if time <= m and score > ans:
            ans = score
        return
    else:
        dfs(L + 1, score+arr[L][0], time+arr[L][1])
        dfs(L + 1, score, time)

n, m = map(int, input().split())
arr = []
check = [0] * n
ans = -214000000
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
dfs(0,0,0)
print(ans)

