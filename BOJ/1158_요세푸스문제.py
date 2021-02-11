'''

1,2,3,4,5,6,7


'''

n, k = map(int, input().split())

arr = list(range(1,n+1))
ans = []
rm_idx = 0
for i in range(n):
    rm_idx += k-1
    if rm_idx >= len(arr):
        rm_idx = rm_idx % len(arr)
    ans.append(str(arr.pop(rm_idx)))

print("<",", ".join(ans[0:]),">", sep='')
