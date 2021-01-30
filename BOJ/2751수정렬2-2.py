'''
합병정렬
'''

def mergeSort(a, l , r):

    if l < r:
        m = (l + r) // 2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m ,r)

def merge(a, l, m, r):
    i = l
    j = m+1
    k = l
    while i <= m and j <= r:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1


    if i > m:
        while j <= r:
            tmp[k] = a[j]
            j+=1
            k+=1
    else:
        while i <= m:
            tmp[k] = a[i]
            i+=1
            k+=1
    a[0:] = tmp[0:]

import sys
sys.setrecursionlimit(3000)
N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)
tmp = arr.copy()
mergeSort(arr, 0, N-1)
for i in range(N):
    print(arr[i])




