
arr = []
def solve(n):
    global arr
    result = 0
    len = (n*2)+1
    arr = [True] * len
    arr[1] = False
    for i in range(2, len):
        if arr[i]:
            for j in range(i+i, len, i):
                arr[j] = False

    for i in range(n+1, len):
        if arr[i] is True:
            result += 1
    return result


while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))

