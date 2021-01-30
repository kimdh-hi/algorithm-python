'''
입력
5 9
1 2 3 2 6 2 3 5 7
'''

# n: 캐시 사이즈
# m: 작업수
n, m = map(int, input().split())

# 대기 중인 작업
wait_q = list(map(int, input().split()))

# 캐시 (최초 비어있는 상태 0)
c = [0]*n


for i in range(m):
    task = wait_q.pop(0)
    pos = -1
    for j in range(n): # 캐시 사이즈만큼 루프, pos값 hit시 hit 발생인덱스(j), miss시 -1 유지
        if c[j] == task: # hit 체크
            pos = j

    if pos == -1: # miss
        for k in range(n - 1, 0, -1):  # miss발생, 캐시사이즈-1번째 부터 왼쪽에서 오른쪽으로 복사
            c[k] = c[k - 1]
    else: # hit
        for k in range(pos, 0, -1): # hit발생 인덱스부터 왼쪽원소들을 오른쪽으로 복사
            c[k] = c[k-1]

    c[0] = task
    print(c)

#print(c)







