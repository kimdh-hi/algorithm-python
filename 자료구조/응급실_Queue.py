'''
Queue

n명의 환자 중 m번째 환자는 몇 번째로 진료 받을 수 있는가
- 입력되는 순서대로 진료의 기회가 있음
- n명의 환자들은 각각 위험도를 갖고있음
- 자신의 위험도보다 높은 인원이 있다면 순서가 뒤로 밀림

중복 위험도가 있을 수 있기 때문에 입력받을 때 튜플로 최초 진료 순서와 위험도를 함께 저장.
'''

from collections import deque

n, m = map(int, input().split()) # 환자수, 타켓환자인덱스

# key = 최초 입력된 순서 0 ~ n-1
# val = 위험도
dq = [(key, val) for key, val in enumerate(list(map(int, input().split())))]
dq = deque(dq)
ans = 0 # 진료횟수
while True:
    curr = dq.popleft()
    if any(curr[1] > x[1] for x in dq): # 뽑힌 값의 위험도가 대기중인 환자의 위험도보다 큰 지 비교
        dq.append(curr) # 대기환자명단에 위험도가 더 큰 환자가 있다면 가장 뒤로 append
    else: # 자신보다 위험도가 높은 환자가 없는 경우
        ans += 1 # 진료횟수 증가
        if curr[0] == m: # 진료받는 환자의 번호가 타겟환자번호와 같은지 비교
            print(ans)
            break

