'''
창고에 n개의 쌓인 적재물이 있다.
각 적재물은 적재된 만큼의 높이가 입력된다.
m회 창고정리 후에 적재물의 최고높이와 최저높이의 차이를 출력

창고정리는 적재물의 높이가 가장 높은 곳에서 낮은 곳으로 1만큼 옮기는 것.

매번 옮길때마다 정렬하는 방법도 있지만 루프 안에서 정렬은 쫌 ..
'''

L = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = [0] * 101 # 적재물 층수는 100을 넘지 않는다는 조건.
maxH = float('-inf')
minH = float('inf')
for x in arr:
    cnt[x] += 1
    if x > maxH: maxH = x # 최대값 조정
    if x < minH: minH = x # 최소값 조정

for _ in range(m):
    if cnt[maxH] == 1: # 최고높이의 적재물이 한 개인 경우
        cnt[maxH] -= 1
        maxH -= 1
        cnt[maxH] += 1
    else: # 최고높이 적재물이 두 개 이상인 경우, 최고높이는 감소되지 않음.
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1

    if cnt[minH] == 1: # 최저높이 적재물이 한 개인 경우
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
    else: # 최저높이 적재물이 두 개 이상인 경우, 최저높이는 높아지지 않음
        cnt[minH] -= 1
        cnt[minH + 1] += 1

print(maxH - minH)