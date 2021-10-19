input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    n = array[0]
    for i in range(1, len(array)):
        if array[i] > n:
            n = array[i]
    return n


result = find_max_num(input)
print(result)