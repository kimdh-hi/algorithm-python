def solve(n):
    res = 666

    while True:
        if '666' in str(res):
            n -= 1
            if n == 0:
                break
        res += 1

    return res


n = int(input())
print(solve(n))
