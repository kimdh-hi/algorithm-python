'''
조합구하기

1~n까지 번호가 적인 구술이 있다.
M개를 뽑는 방법의 수
    방법의 수 = 중복 X = 조합

dfs의 레벨(depth)가 증가될 때마다 자리수가 증가되는 것임 (=순열과 동일)
레벨이 증가될 때, 매개변수로 자기+1을 전달(s)
반복문의 시작을 자기+1부텉 시작함.
'''

def dfs(L, s):
    global cnt
    if L == m:
        for c in check:
            if c > 0: print(c, end = ' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            check[L] = i
            dfs(L+1, i+1)

n, m = map(int, input().split())
check = [0] * (n+1)
cnt = 0
dfs(0,1)
print(cnt)