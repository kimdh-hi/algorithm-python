from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # n=대기중인 문서수, m=타겟문서인덱스
    arr = list(map(int, input().split())) # 대기중인 문서의 중요도
    t_idx = [0 for _ in range(n)] # 타겟문서 인덱스를 체크하기 위한 리스트
    t_idx[m] = 'check' # 타겟문서인덱스(위치) 체크
    dq1 = deque(arr)
    dq2 = deque(t_idx)
    cnt = 0 # 인쇄되는 문서수
    while True:
        if dq1[0] == max(dq1): # 프린터의 가장 앞 문서의 중요도가 전체 문서 중 가장 클 때,
            cnt += 1 # 일단 인쇄 함
            if dq2[0] == 'check': # 인쇄된 문서가 타겟문서인지 확인
                print(cnt) # 맞다면 인쇄수 프린트 후 break
                break
            else: # 타겟문서가 아니라면 그냥 인쇄된 것이므로 가장 앞 문서 제거
                dq1.popleft()
                dq2.popleft()
        else: # 프린터의 가장 앞 문서의 중요도가 전체 문서 중 가장 크지 않을 때,
            dq1.append(dq1.popleft()) # 앞에서 빼고 뒤로 삽입
            dq2.append(dq2.popleft())

