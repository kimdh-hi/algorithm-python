def fibonacci(n):
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 1

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(fibonacci(100))