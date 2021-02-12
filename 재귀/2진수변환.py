
n = int(input())

def toBinary(n):
    if n == 0: return
    else:
        toBinary(n//2)
        print(n % 2, end='')

toBinary(n)