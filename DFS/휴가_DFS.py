
def dfs(L, total):
    global ans
    if L == n: # 배열의 끝 인덱스에 도달했다면
        if ans < total:
            ans = total # 수당 총계 계산, 갱신
        return
    else:
        if L + tl[L] < n+1: # 현재 상담날짜에서 소요시간을 더한 값이 초과되지 않는다면
            dfs(L + tl[L], total + pl[L]) # 소요시간만큼 이동해서 상담, 현재상담급여 누적
        dfs(L + 1, total) # 바로 다음 날짜부터 시



n = int(input())
tl = list() # 소요시간
pl = list() # 수당
ans = 0
for i in range(n):
    t, p = map(int, input().split())
    tl.append(t)
    pl.append(p)
dfs(0, 0)
print(ans)