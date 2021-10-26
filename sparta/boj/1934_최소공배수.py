
n = int(input())

def get_gcd(a, b):
    if b == 0:
        return a

    return get_gcd(b, a % b)

for _ in range(n):
    a, b = map(int, input().split())
    print((a*b) // get_gcd(a, b))