import time
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start_time = time.time()
arr.sort()

for _ in range(m):
    arr[0] += 1
    arr[-1] -= 1
    arr.sort()
end_time = time.time() - start_time
print(end_time)
print(arr[-1] - arr[0])

# import time
# n = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# cnt = [0] * 101
#
# maxh = -214000000
# minh = 214000000
# start = time.time()
# for a in arr:
#     cnt[a] += 1
#     if a > maxh: maxh = a
#     if a < minh: minh = a
#
# for i in range(m):
#     if cnt[maxh] == 1:
#         cnt[maxh] -= 1
#         maxh -= 1
#         cnt[maxh] += 1
#     else:
#         cnt[maxh] -= 1
#         cnt[maxh-1] += 1
#
#     if cnt[minh] == 1:
#         cnt[minh] -= 1
#         minh += 1
#         cnt[minh] += 1
#     else:
#         cnt[minh] -= 1
#         cnt[minh+1] += 1
# end = time.time()-start
# print(end)
# print(maxh - minh)