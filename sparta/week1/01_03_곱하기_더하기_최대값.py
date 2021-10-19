
# 왼쪽부터 차례대로 연산될 때 +, *로만 가장 큰 수를 만들어라.

input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    result = 0

    for a in array:
        if a <= 1 or result <= 1:
            result += a
        else:
            result *= a

    return result


result = find_max_plus_or_multiply(input)
print(result)