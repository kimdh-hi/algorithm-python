import time
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1
curr = 0
res = ""
tmp = []
s_t = time.time()
while lt <= rt:
    if a[lt] > curr: # 왼쪽값이 최근 증가수열값 보다 큰 경우
        tmp.append((a[lt], 'L')) # 일단 임시배열에 튜플로 삽입
    if a[rt] > curr: # 오른쪽값이 최근 증가수열값 보다 큰 경우
        tmp.append((a[rt], 'R')) # 일단 임시배열에 튜플로 삽입
    tmp.sort() # 임시배열 값을 증가수열 형태로 하기 위해 오름차순 정렬
    if len(tmp) == 0: # 임시배열의 길이가 0이라면 양쪽끝값에서 조건을 만족하는 값이 없다는 의미. 종료
        break
    else:
        res = res+tmp[0][1] # L, R 값 저장
        curr = tmp[0][0] # 최근 증가수열값 저장
        if tmp[0][1] == 'L':
            lt += 1 # 왼쪽값이 선택된 경우 왼쪽인덱스 증가
        else:
            rt -= 1 # 오른쪽값이 선택된 경우 오른쪽 인덱스 증가
    tmp.clear()
e_t = time.time() - s_t
print(e_t)
print(len(res))
print(res)
