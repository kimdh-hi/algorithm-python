'''
n길이의 랜선을 1 또는 2의 길이로 자르는 경우의 수

n=1, 경우의 수 = 1
n=2, 경우의 수 = 2
n=3, 경우의 수 = 3
n=4, 경우의 수 = 5
f(n) = f(n-2) + f(n-1)
'''

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[-1])