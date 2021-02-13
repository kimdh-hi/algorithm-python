import sys

def dfs(L, sub_total):
    if n == L:
        if sub_total == (total - sub_total):
            print("YES")
            sys.exit(0)
    else:
        dfs(L+1, sub_total + arr[L]) # 이전 노드 값을 사용 (누적)
        dfs(L+1, sub_total) # 이전 노드 값을 사용하지 않음



cnt = 0
n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dfs(0,0)
print("NO")