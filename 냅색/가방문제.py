'''
냅색 알고리즘

가방에 n의 무게를 담을 수 있을 때 최대 가치를 출력
'''


# n: 보석종류, m: 최대 담을 수 있는 무게
n, m = map(int, input().split())

back = list()
for i in range(n):
    # 보석의 무게, 가치 입력
    back.append(list(map(int, input().split())))

dp = [0] * (m+1)

for b in back:
    for i in range(b[0], m+1):
        dp[i] = max(dp[i-b[0]]+b[1], dp[i])

print(dp)
print(max(dp))

