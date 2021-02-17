'''
N개 동전을 3명에서 나누어 줄 때, 세사람이 나누어 갖는 동전의 합계의 최대값과 최소값의 최소차
단, 세사람의 총액은 달라야 함.
'''
def dfs(L):
    global ans
    if L == n:
        gap = max(money) - min(money)
        if gap < ans:
            tmp = set() # 총액이 같은지 확인하기 위함
            for m in money:
                tmp.add(m)
            if len(tmp) == 3:
                ans = gap
        return
    else:
        for i in range(3):
            money[i] += c[L] # i번째 사람에게 누적 후 다음 동전인덱스로 .
            dfs(L+1)
            money[i] -= c[L] # 돌아올 때 더해준 값을 빼주어야 함.

n = int(input())
c = []
for i in range(n):
    c.append(int(input()))

ans = 21400000
money = [0] * 3
dfs(0)
print(ans)

