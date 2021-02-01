
n, target = map(int, input().split())

arr = list(map(int,input().split()))

res = 0

lt = 0
sum = 0
for rt in range(n):
    sum += arr[rt]
    if sum == target:
        res += 1
    while sum >= target and lt < rt:
        sum -= arr[lt]
        if sum == target:
            res += 1
        lt += 1
print(res)



# for i in range(n):
#     sum = arr[i]
#     if i == n-1:
#         if arr[i] == target:
#             res +=1
#             break
#         else: break
#     if sum == target:
#         res += 1
#         continue
#     for j in range(i+1, n):
#         sum += arr[j]
#         if sum == target:
#             res += 1
#             break
#
# print(res)