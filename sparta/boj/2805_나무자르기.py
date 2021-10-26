
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# minh: 1 (나무의 최소높이는 1)
# maxh: 현재 나무 중 최고높이
minh, maxh = 1, max(trees)

while minh <= maxh:
    mid = (minh + maxh) // 2 # 목재절단기의 높이
    tmp = 0 # 벌목되는 나무들의 길이의 합

    for t in trees:
        if t > mid: # 벌목되는 높이에 해당하는 나무만 벌모되도록
            tmp = tmp + (t - mid)

    # mid의 높이로 벌목한 결과 목표로 한 길이보다 큰 경우
    if tmp >= m:
        minh = mid + 1 # 최소값을 중간값+1로 갱신해서 더 높은 높이에서 벌목되어 더 작은 길이가 벌목되도록 한다.
    else:
        maxh = mid - 1 # 최대값을 중간값+1로 갱신해서 더 낮은 높이에서 벌목되어 더 큰 길이가 벌목되도록 한다.

print(maxh)