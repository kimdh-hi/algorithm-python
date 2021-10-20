def solve(num):
    target = num
    cnt = 0
    while True:
        a = num // 10
        b = num % 10
        tmp = a + b
        num = (b*10) + (tmp % 10)
        cnt += 1
        if num == target:
            return cnt

num = int(input())
print(solve(num))