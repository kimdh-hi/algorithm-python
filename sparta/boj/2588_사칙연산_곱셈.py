
def solve(num1, num2):
    res = 0
    a = '1'
    for i in range(2, -1, -1):
        sum = 0
        for j in range(3):
            sum = sum * 10 + int(num1[j]) * int(num2[i])
        print(sum)
        res = res + sum * int(a)
        a += '0'
    return res


num1 = input()
num2 = input()
print(solve(num1, num2))
