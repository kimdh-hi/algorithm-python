'''
수직선상의 n개 마구간에 m마리의 말을 배치
    마구간 간의 최소거리가 최대로 되는 거리를 출력

마구간 간의 거리를 이분탐색하며 최대값을 찾아나감
'''
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort() # 수직선상의 배치를 위해 정렬

lt = arr[0] # 마구간의 첫번째 위치
rt = arr[-1] # 마구간의 마지막 위치
ans = 0

# 이분탐색 시작
while lt <= rt:
    mid = (lt+rt) // 2 # 가장 가까운 말의 최대 거리
    cnt = 1 # 첫번째 말은 첫번째 마구간에 무조건 위치됨
    idx = 0 # 마구간 위치 인덱스
    for i in range(1,n): # 두번째 말의 위치부터 탐색
        if (arr[i] - arr[idx]) >= mid: # 최대거리를 만족하는 경우
            idx = i # 조건 만족시 마구간위치 조정
            cnt += 1 # 말 배치
    if cnt < m: # m마리 미만으로 배치된 경우
        rt = mid - 1 # 최대거리 조정 (감소)
    else: # m마리 이상으로 배치된 경우
        ans = mid # 최대거리 임시저장
        lt = mid + 1 # 더 큰 최대거리로 만족하는지 다시 검사
print(ans)

'''
입력예시
5 3
1
2
8
4
9

출력
3
'''