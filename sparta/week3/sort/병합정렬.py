def merge(l_arr, r_arr):
    tmp = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(l_arr) and r_idx < len(r_arr):
        if l_arr[l_idx] < r_arr[r_idx]:
            tmp.append(l_arr[l_idx])
            l_idx += 1
        else:
            tmp.append(r_arr[r_idx])
            r_idx += 1

    if l_idx < len(l_arr):
        for i in range(l_idx, len(l_arr)):
            tmp.append(l_arr[i])
    else:
        for i in range(r_idx, len(r_arr)):
            tmp.append(r_arr[i])
    return tmp


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    m = n // 2
    l_arr = merge_sort(array[:m])
    r_arr = merge_sort(array[m:])

    return merge(l_arr, r_arr)


array = [6, 1, 8, 2, 9]
print(merge_sort(array))




