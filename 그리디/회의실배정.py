'''
n개 예정된 회의를 한 개 회의실에서 겹치치 않고 완료할 수 있는 최대 수

조건
회의가 끝나는 동시에 시작 가능
회의의 시작과 끝 시간이 같은 회의도 존재
'''

n = int(input()) # 예정된 회의 수
res = 1 # 회의 수 (초기 정렬 후 첫번째 회의는 무조건 시작되기 때문에 1부터 카운트)
arr = [] # 예정된 회의 수
for i in range(n):
    s, e = map(int,input().split())
    arr.append((s,e)) # 시작시간과 끝시간을 튜플로 구성

# 정렬
# 조건1 = 끝나는 시간 기준 오름차순 반드시 빨리 끝나는 회의가 앞에 위치해야 함.
# 조건2 = 시작 시간 기준 오름차순 (시작시간과 끝나는 시간이 같은 경우도 있는 것 때문)
arr.sort(key=lambda x:(x[1],x[0]))

start, end = arr.pop(0) # 첫번째 회의는 무조건 시작됨
for i in range(n-1):
    start_tmp, end_tmp = arr[i]
    if start_tmp >= end: # 현재 진행중인 회의의 끝시간보다 시작시간이 같거나 크다면 시작 가능
        res += 1 # 회의 시작 (카운팅)
        start = start_tmp # 다음 시작될 회의시간으로 갱신
        end = end_tmp

print(res)

'''
예시 입력
3
3 3
1 3
2 3
'''
