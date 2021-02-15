import sys
'''
1~n까지의 어떤 순열이 있고 이 순열의 파스칼의 삼각형의 끝 값이 주어졌을 때 순열을 구하시오

1. 1~n의 이항계수를 구함
2. 재귀를 돌며 순열이 만들어질 때마다 이항계수로 곱해주어 목표값과 같은지 확인 
'''
def dfs(L):
    if L == n: # n개 만큼의 순열이 만들어진 경우
        tmp = 0
        for i in range(n): # 순열에 이항계수를 곱해줌
            tmp += (bin[i] * p[i])
        if tmp == m: # 곱한 값이 타겟값과 같을 때 출력
            for c in p:
                print(c, end = ' ')
            sys.exit(0)
    else:
        for i in range(1,n+1):
            if check2[i] == 0: # 순열에 중복방지
                check2[i] = 1 # i라는 숫자가 쓰였음을 의미
                p[L] = i # 순열에 추가
                dfs(L+1) # 순열의 다음 인덱스로 재귀
                check2[i] = 0 # 재귀 후 이전 인덱스로 돌아올 때 쓰였던 값을 쓰이지 않은 것으로 초기화

n, m = map(int, input().split())
bin = [1] * n # n의 이항계수
p = [0] * n # 순열배열
check2 = [0] * (n+1) # 순열을 만들기 위한 중복방지 배열

for i in range(1,n): # 이항계수 만들기
    bin[i] = (bin[i-1] * (n-i)) // i # 이항계수의 첫 값은 1이므로 이전값을 이용하며 이항계수 구성

dfs(0)