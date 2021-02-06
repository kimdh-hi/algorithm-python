'''
n까지 자연수가 저장된 배열에서 양끝의 수로만 만들 수 있는 증가수열
증가수열 구성시 배열의 어느쪽에서 빠져온건지 저장 (Left, Right)

증가수열에 사용된 수는 배열에서 pop됨
배열에 요소가 한개만 남으면 L로 처리
'''

import time
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

q = deque(arr)

ans_str = ""
curr = 0
s_t = time.time()
while q:
    # 왼쪽값이 오른쪽값보다 작고 최근 증가수열 값보다 클 때,
    # 왼쪽값이 오른쪽값보다 크지만 오른쪽값이 최근 증가수열 값보다 작은 경우
    if (q[0] < q[-1] and q[0] > curr) or (q[0] > q[-1] and q[-1] < curr and q[0] > curr):
        curr = q[0]
        ans_str += "L"
        q.popleft()
    elif (q[-1] < q[0] and q[-1] > curr) or (q[-1] > q[0] and q[0] < curr and q[-1] > curr):
        curr = q[-1]
        ans_str += "R"
        q.pop()
    # 배열이 홀수인 경우 시작값과 끝값이 같은 값을 가르키게 됨, 이 값이 최근 증가수열보다 크다면 L로 삽입
    elif q[-1] == q[0] and q[0] > curr:
        ans_str += "L"
        q.pop()
        curr = q[0]
    else: # 양쪽끝 값 중 어떤 것도 증가수열이 될 수 없을 때 루프 종료.
        break
e_t = time.time()-s_t
print(e_t)
print(len(ans_str))
print(ans_str)
'''
LLRL
'''