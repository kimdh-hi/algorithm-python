'''
n가지 동전이 각기 n원씩 b개가 있다고 가정
target만큼의 금액을 거슬러줄 수 있는 경우의 수

각 금액의 수만큼 반복 (0부터 개수까지 반복하며 쓰지 않는 경우까지 처리)
'''

def dfs(L, sum):
    global ans
    if sum > target: return
    if L == n:
        if sum == target:
            ans += 1
        return
    else:
    # 동전의 수만큼 반복 (0부터 시작 !! 사용하지 않는 경우도 처리)
    # 반복시 금액 * 동전수 만큼 누적하며 재귀호출
        for i in range(b[L]+1):
            dfs(L+1, sum + (a[L] * i))


target = int(input()) # 교환해줄 금액
n = int(input()) # 동전의 가지수
a = list() # 동전의 금액
b = list() # 동전의 개수
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
dfs(0,0)
print(ans)

