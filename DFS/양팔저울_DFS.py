'''

상태트리 각 노드에서 3개 가지로 분기
    1. 추를 왼쪽에 놓는 경우 (추무게 + )
    2. 추를 오른쪽에 놓는 경우 (추무게 - )
    3. 추룰 놓지 않는 경우
리프노드에 도달했을 때
'''

def dfs(L, weight):
    if L == n:
        if 0 < weight <= total:
            ans.add(weight)
        return
    else:
        dfs(L+1, weight + arr[L]) # 추를 왼쪽에 추가하는 경우
        dfs(L+1, weight - arr[L]) # 추를 오른쪽에 추가하는 경우 (물과 함께)
        dfs(L+1, weight) # 추를 추가하지 않는 경우

n = int(input())
arr = list(map(int, input().split()))
ans = set() # 중복제거를 위해 set사용
total = sum(arr)
dfs(0,0)
print(sum(arr) - len(ans))