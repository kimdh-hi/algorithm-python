input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    cnt = 0
    for i in range(1, n):
        for j in range(i):
            cnt += 1
            if array[i-j] < array[i-j-1]:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else:
                break
    print(cnt)

insertion_sort(input)
print(input)