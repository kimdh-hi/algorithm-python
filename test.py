
kg, n = map(int, input().split())

dogs = []
for _ in range(n):
    dogs.append(int(input()))

dogs.sort(reverse=True)

lt, rt = 0, n
ans = 0
while lt <= rt:
    mid = (lt+rt) // 2
    sum = 0
    for i in range(mid+1):
        sum += dogs[i]
    if sum < kg:
        if ans < sum:
            ans = sum
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)
