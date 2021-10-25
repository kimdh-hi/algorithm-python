import math

def is_prime(n):
    to = int(math.sqrt(n))
    for i in range(2, to+1):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        print(i)

