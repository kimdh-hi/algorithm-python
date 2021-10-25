
n, m = map(int, input().split())
trees = list(map(int, input().split()))

minh, maxh = 1, max(trees)

while minh <= maxh:
    mid = (minh + maxh) // 2
    tmp = 0
    for t in trees:
        if t >= mid:
            tmp = tmp + (t - mid)

    # mid의 높이로 벌목한 결과 목표로 한 길이보다 큰 경우
    if tmp >= m:
        minh = mid + 1 # 이분탐색의 left에 해당하는 최소값을 보정
    else:
        maxh = mid - 1
print(maxh)