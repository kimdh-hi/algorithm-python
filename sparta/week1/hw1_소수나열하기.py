
# 입력받은 정수보다 작은 모든 소수를 구하여라

def get_all_prime(num):
    result = []
    arr = [0] * (num+1)
    for i in range(2, num):
        if arr[i] == 0:
            j = i*2
            while j <= num:
                arr[j] = 1
                j*=2

    for i in range(2, num+1):
        if arr[i] == 0:
            result.append(i)

    return result


num = int(input())
print(get_all_prime(num))
