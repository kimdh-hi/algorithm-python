'''
n명의 승객 보트의 인원제한 2명 무게제한 mKg
탈출 가능한 보트의 최소 개수
'''
from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
q = deque(arr)
cnt = 0

while q:
    if len(q) == 1:
        cnt += 1
        break
    if q[0] + q[-1] > m:
        q.pop()
        cnt += 1
    else:
        q.pop()
        q.popleft()
        cnt += 1

print(cnt)
