'''
n명의 바둑이로 kg에 가장 가까운 합을 구하시오
'''



def dfs(L, part_sum, entire_sum):
    global ans
    # 현재 까지의 부분집합 + (전체집합 - 현재 까지 모든집합) = 앞으로 방문될 모든 집합
    # 앞으로 방문될 모든 집합을 더해도 현재 최대값보다 작다면 현 상태에서 재귀는 무의미
    if part_sum + (total - entire_sum) < ans:
        return
    if L == n: # 끝까지 재귀를 마친 경우
        # 부분집합의 합이 타겟값보다 작고 현재까지 최대값보다 큰 경우 최대값 갱신
        if part_sum <= kg and part_sum > ans:
            ans = part_sum
        else:
            return
    else:
        # 상태노드의 한쪽은 현재 바둑이를 포함시키므로 part_sub에 추가
        # 상태노드의 다른 한쪽은 현재 바둑이를 포함시키지 않으므로 part_sub그대로 전달
        dfs(L+1, part_sum + dogs[L], entire_sum + dogs[L])
        dfs(L+1, part_sum, entire_sum + dogs[L])

kg, n = map(int, input().split())
dogs = []
for _ in range(n):
    dogs.append(int(input()))
total = max(dogs)
ans = -214000000 # 최대값 비교를 위한 최소값
dfs(0,0,0) # dfs(인덱스, 부분집합의합, 인덱스까지의 집합의 합)
print(ans)