'''
숫자 뒤집기

17 => 71
3500 => 53
'''

def reverse(num):
    res = 0
    while num > 0:
        tmp = num % 10
        res = res * 10 + tmp
        num //= 10
    return res

while True:
    n = int(input())
    if n == -1: break
    print(reverse(n))