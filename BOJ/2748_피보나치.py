
dp = [1 for i in range(91)]
dp.insert(0, 1)

def fibo(n):
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
print(fibo(n))
