
b = [1 for i in range(41)]
b.insert(0,0)

def fibo(n):
    for i in range(3,n+1):
        b[i] = b[i-1] + b[i-2]

fibo(41)

N = int(input())

for i in range(N):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(b[n-1], b[n])