'''
뒤집은 소수
'''

def reverse(num):
    ret = 0
    while num > 0:
        tmp = num % 10
        ret = ret*10+tmp
        num //= 10
    return ret

def isPrime(num):
    if num == 1: return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
for a in arr:
    r_num = reverse(a)
    if isPrime(r_num):
        print(r_num, end=' ')

