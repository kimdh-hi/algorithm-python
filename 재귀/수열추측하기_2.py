import sys

def dfs(L, sum):
    if L == n and sum == m:
        for p in perm:
            print(p, end = ' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                perm[L] = i
                dfs(L+1, sum + (perm[L] * binom[L]))
                check[i] = 0

n, m = map(int, input().split())

binom = [1] * n
perm = [0] * n
check = [0] * (n+1)

for i in range(1, n):
    binom[i] = (binom[i-1] * (n-i)) // i

dfs(0,0)