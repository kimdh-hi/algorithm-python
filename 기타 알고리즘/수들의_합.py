
n ,m = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0
l = 0
r = 1
sum = arr[l]

while True:
    if sum < m: # 부분수열의 합계가 타겟보다 작은 경우
        if r < n: # 배열 인덱스 내에 있는 지 확인
            sum += arr[r] 
            r += 1
        else:
             break
    elif sum == m:
        ans += 1
        sum -= arr[l]
        l += 1
    else:
        sum -= arr[l]
        l += 1

print(ans)