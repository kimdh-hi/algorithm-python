import sys
n = int(sys.stdin.readline())
arr1 = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for a in arr2:
    lt = 0
    rt = n-1
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if a == arr1[mid]:
            ans = 1
            break
        elif a < arr1[mid]:
            rt = mid  - 1
        else:
            lt = mid + 1
    print(ans)






