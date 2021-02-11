'''
ABC... 필수과목이 순서대로 주어짐
    필수과목은 반드시 들어야 함
    필수과목은 이전 과목을 반드시 수료 후에 들어야 함
    A -> B -> C 의 순서여야 함.
'''

q = list(input())
n = int(input())
ans = []
for i in range(n):
    arr = list(input())
    idx = 0
    for a in arr:
        if q[idx] == a:
            idx += 1
        if idx == len(q): break
    if idx < len(q):
        print("#",i+1," NO")
    else:
        print("#", i + 1, " YES")

