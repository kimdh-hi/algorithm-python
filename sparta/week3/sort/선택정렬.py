input = [4, 6, 2, 9, 1]


def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
