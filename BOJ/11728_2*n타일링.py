def solve(n):
    d[1] = 1
    d[2] = 2
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n] % 10007

N = int(input())
d = [1 for i in range(N+1)]
print(solve(N))