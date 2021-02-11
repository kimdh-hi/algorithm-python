
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(0,n):
    arr[i] = (i, arr[i])
arr.sort(reverse=True, key=lambda x:(x[1],x[0]))
print(arr)
cnt = 0
for i in range(n):
    cnt += 1
    if arr[i][0] == m:
        print(cnt)
        break