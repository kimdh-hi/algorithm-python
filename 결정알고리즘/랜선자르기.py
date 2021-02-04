'''
n개 랜선을 m개의 같은 길이의 랜선으로 잘라 만들 수 있는 최대 랜선길이

* 이분검색을 배열의 인덱스가 아닌 값에 사용함.
'''
n, m = map(int, input().split())
line = []

for _ in range(n):
    line.append(int(input()))

# 중간길이로 랜선을 잘랐을 때 나눠지는 개수
def Count(length):
    cnt = 0
    for l in line:
        cnt += (l // length)
    return cnt

ans = 0
lt = 1 # 최소길이
rt = max(line) # 최대길이

while lt <= rt:
    mid = (lt+rt) // 2 # 이분검색
    tmp_cnt = Count(mid) # 이분검색을 통해 중간값을 기준으로 찾은 랜선수
    if tmp_cnt >= m: # 랜선수가 타겟 랜선수보다 크거나 같다면
        ans = mid # 일단 답변수에 넣고 최적해를 찾기 위해 다시 이분검색
        lt = mid+1 # 랜선길이를 늘려가며 최적해가 있는지 이분검색
    elif tmp_cnt < m: # 랜선수가 타겟 랜선수보다 적다면
        rt = mid-1 # 랜선길이를 감소해가며 다시 이분검색
print(ans)

'''
입력
4 11
802
743
457
539

출력
200
'''



