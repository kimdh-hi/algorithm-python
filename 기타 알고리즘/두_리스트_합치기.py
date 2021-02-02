'''
정렬된 두 리스트 합치기
'''
n = int(input())
narr = list(map(int, input().split()))

m = int(input())
marr = list(map(int, input().split()))

ans = [] # 정답배열

nidx = 0
midx = 0

# 두 배열의 인덱스를 달리하여 두 배열의 다른 인덱스가 가리키는 원소 중 작은 것을 골라냄
while nidx < n and midx < m: # 두 배열의 인덱스 중 벗어나는 인덱스가 발생하는 경우 루프종료
    if narr[nidx] <= marr[midx]: # 현재 가리키는 narr의 원소값이 작거나 같은 경우
        ans.append(narr[nidx]) # 정답배열에 삽입
        nidx += 1 # narr 인덱스 증가
    else:
        ans.append(marr[midx])
        midx += 1

if nidx < n:
    ans += narr[nidx:]
else:
    ans += marr[midx:]

print(ans)