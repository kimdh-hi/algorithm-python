'''
최소공백수 => (두 수의 곱) / 최대공약수

최대공약수 => 유클리드 호제법
- a가 b보다 클 때 a를 b로 나눈 나머지가 0일 때 b가 a와 b의 최대공약수이다.
- b가 0이 될 때까지 b를 a에 넣고 b에는 a와 b를 나눈 나머지를 넣는다.
'''


# a가 b보다 클 때 a를 b로 나눈 나머지가 0일 때 b가 a와 b의 최대 공약수이다.
def get_gcd(a, b):
    if b == 0:
        return a

    return get_gcd(b, a % b)


a, b = map(int, input().split())
gcd = get_gcd(a, b)
print(gcd)
print((a*b)//gcd)

