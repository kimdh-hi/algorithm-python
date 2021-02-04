'''
n개 노래를 m개 디스크에 저장해야함
디스크 간의 크기가 최소화 되어야 제조원가가 내려감.

n개의 노래를 m개의 디스크에 저장하고 디스크 간의 크기 차이를 최소화할 수 있는 디스크의 최대 용량
'''
n, m = map(int, input().split())
songs = list(map(int, input().split()))

def check(v):
    sum = 0 # 한 개 DVD에 들어가는 노래 길이
    cnt = 1 # DVD 수
    for s in songs:
        if sum + s > v: # 한 DVD에서 정해진 용량(v)을 넘어선다면
            cnt += 1 # DVD증가
            sum = s # 다음 DVD에 노래 추가
        else:
            sum += s # 현재 DVD에 노래 추가
    return cnt # DVD수 리턴

maxx = max(songs)
lt = 1 # 노래 최소 길이
rt = sum(songs) # 노래 길이의 합
ans = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if mid >= maxx and check(mid) <= m: # DVD가 타겟DVD수보다 작다면 ok
        ans = mid # 일단 결과 저장
        rt = mid-1 # DVD 간의 크기 차이를 줄이기 위해 더 작은 용량으로 나눌 수 있는지 확인
    else: # 타겟 DVD수보다 크다면
        lt = mid + 1 # 한 개 DVD의 용량을 늘림

print(ans)

'''
입력
9 3 
1 2 3 4 5 6 7 8 9

출력
17
'''
