'''
N개 자연수 중 증가수열을 이룰 수 있는 최대 길이

dp리스트의 인덱스 == 입력받은 리스트의 값
두번째 원소부터 이전 값과 비교할 때 최대 부분수열 길이 값도 함께 비교하며 갱신
'''

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0) # 인덱스 1부터 시작
dp = [0] * (n+1) # arr에서 dp의 인덱스번 째 값이 끝 값인 경우의 최대길이를 저장
dp[1] = 1 # 첫번째 자리가 끝 값이 된 경우는 길이는 1
ans = 0

for i in range(2, n+1):
    maxlen = 0
    for j in range(i-1, 0, -1): # 이전 값부터 첫번째 값까지 비교
        if arr[j] < arr[i] and dp[j] > maxlen: # 이전값이 현재값(끝값)보다 작을 때 최대부분수열 길이를 갱신
            maxlen = dp[j]
    dp[i] = maxlen + 1 # 갱신된 최대 부분수열길이에 현재 값을 끝에 두므로 +1
    if dp[i] > ans:
        ans = dp[i]
print(ans)