from collections import deque
n, k = map(int, input().split())

arr = list(range(1,n+1))
dq = deque(arr)

while dq:
    for _ in range(k-1): # k번째 전까지 rotate
        tmp = dq.popleft()
        dq.append(tmp)
    if len(dq) > 1: # deque에 원소가 2개 이상이라면 앞원소 제거
        dq.popleft()
    else: # 원소가 하나만 남았다면 출력
        print(dq.popleft())



