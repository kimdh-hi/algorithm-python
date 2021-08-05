'''
3
3 3 5
2 3 4
6 5 2

Bottom-up
한 번에 오른쪽, 아래쪽 방향으로만 이동 가능한 경우 [n][n]에 도착할 수 있는 최소 비용

1. dp 리스트에 [0][0]을 기준으로 첫번째 행, 첫번째 열을 초기화
2. 초기화된 dp리스트를 기반으로 위, 아래에서 오는 경우중 최소값을 선택하여 갱신
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = arr[0][0]

# dp 리스트 첫행, 첫열 초기화
for i in range(1,n):
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i-1][0] + arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[n-1][n-1])
