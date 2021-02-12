import sys

input = sys.stdin.readline

n = int(input())
mycard = sorted(list(map(int, input().split())))
m = int(input())
target = list(map(int, input().split()))

for t in target:
    tmp = 0
    lt, rt = 0, n-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if t == mycard[mid]:
            tmp = 1
            break
        elif t < mycard[mid]:
            rt = mid - 1
        else:
            lt = mid + 1
    print(tmp, end = ' ')

# import sys
# input = sys.stdin.readline
# n = int(input())
# s = list(map(int, input().split()))
# m = int(input())
# s_ = list(map(int, input().split()))
# s.sort()
# for i in s_:
#     low, high = 0, n
#     while low <= high:
#         mid = (low + high) // 2
#         if 0 <= mid < n:
#             if s[mid] < i: low = mid + 1
#             else: high = mid - 1
#         else: break
#     if 0 <= high + 1 < n:
#         if s[high + 1] == i: print(1, end=" ")
#         else: print(0, end=" ")
#     else: print(0, end=" ")



