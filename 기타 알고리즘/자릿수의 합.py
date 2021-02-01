'''
N개 정수 중 각 자리수의 합이 최대인 정수를 출
'''
n = int(input())

arr = list(map(int, input().split()))

def digit_sum(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num //= 10
    return sum

max = -2147000000
res = 0
for i in range(n):
    res_tmp = digit_sum(arr[i])

    if res_tmp > max:
        max = res_tmp
        res = i

print(arr[res])

