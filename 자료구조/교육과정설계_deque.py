
from collections import deque

arr = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(arr)
    for p in plan:
        if p in dq:
            t = dq.popleft()
            if t != p:
                break
    if not dq:
        print("#",i+1," YES",sep='')
    else:
        print("#", i + 1, " NO", sep='')


