'''
메모리제한, 시간제한
테스트케이스 개수 N < 10,000,000
    천만개를 배열에 넣으면 메모리제한 걸림
입력정수가 10000까지로 제한되어 있음
    만개의 배열로 해결
==> 시간초과 ...
'''
N = 10001
tmp = [0 for i in range(N)]

c = int(input())

for i in range(c):
    n = int(input())
    tmp[n] = tmp[n]+1

idx = 0

while idx < N:
    if tmp[idx] != 0:
        print(idx)
        tmp[idx] = tmp[idx]-1
        idx -= 1
    idx += 1