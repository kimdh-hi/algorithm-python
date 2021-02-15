'''
동전구하기 DFS풀이 (원래 DP로 풀어야 함.)

DFS 레벨 = 동전의 수

최적화
1. 찾아야 할 동전의 합보다 저 커진다면 이후 재귀 진행하지 않음
2. 이미 답을 찾은 동전수보다 레벨이 커진다면 (depth가 깊어진다면) 리턴
'''

def dfs(L, sum):
    global ans
    if sum > target or L > ans:
        return
    if sum == target:
        if L < ans:
            ans = L
        return
    else:
        for c in coin:
            dfs(L+1, sum+c)


n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
target = int(input())
ans = 214000000
dfs(0, 0)
print(ans)