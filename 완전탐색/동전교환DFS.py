'''
동전교환 DFS

m원을 만들기 위한 동전의 최소 개수

dfs의 depth가 곧 동전의 개수임
'''
n = int(input()) # 동전 종류 수

coins = list(map(int, input().split())) # 동전 값
coins.sort(reverse=True) # 최적화를 위해 큰 동전부터 재귀가 되도록 함
m = int(input()) # 타켓 동전합계

ans = 9999999

def dfs(depth, sum):
    global ans
    if ans <= depth: # m값을 만족한 depth를 찾은 이후에 더 크거나 작은 depth값은 무시
        return
    if sum > m: # 합계가 초과된다면 재귀 종료
        return
    if sum == m: # 목표값과 합계값이 같은 경우
        ans = depth # depth값 저장
    for i in range(n): # 각 재귀마다 depth증가, 각 줄기마다 동전만큼 합계증가
        dfs(depth+1, sum + coins[i])

dfs(0 ,0)
print(ans)










#
#
# n = int(input()) # 동전 종류 수
#
# coins = list(map(int, input())) # 동전 값
#
# m = int(input()) # 타켓 동전합계
#
# coins.sort(reverse=True)
# res = 999999
#
# def dfs(level, sum):
#     global res
#     if sum > m:
#         return
#     if sum == m:
#         if level < res:
#             res = level
#     else:
#         for i in range(n):
#             dfs(level+1, sum + coins[i])
#
