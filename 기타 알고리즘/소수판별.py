
def is_prime(num):
    flag = True;
    if num == 1: return False
    for i in range(2, num):
        if num%i==0:
            flag = False
            break
    return flag

while True:
    n = int(input())
    if n == -1: break
    if is_prime(n):
        print(n," 은 소수")
    else:
        print(n," 은 소수아님")