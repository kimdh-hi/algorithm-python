'''
퀵정렬
'''
def quickSort(a, l, r):
    start = l
    end = r
    pivot = a[(l+r)//2]

    # partition
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    if l < end:
        quickSort(a, l, end)
    if start < r:
        quickSort(a, start, r)

N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)
quickSort(arr, 0, N-1)
for i in range(N):
    print(arr[i])


