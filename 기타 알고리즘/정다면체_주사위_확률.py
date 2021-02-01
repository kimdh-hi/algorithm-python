
n, m = map(int, input().split())

cnt = [0] * ((n+m)+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
max = -21400000
ans = []
for i in range(len(cnt)):
    if cnt[i] > max:
        max = cnt[i]
        ans.clear()
        ans.append(i)
    elif cnt[i] == max:
        ans.append(i)

print(ans)


