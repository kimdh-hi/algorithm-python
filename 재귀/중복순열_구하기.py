
'''
1~n까지 m개의 중복을 허락하는 순열을 출력

m개의 체크 배열을 생성
체크배열의 인덱스를 dfs의 레벨로 함
'''

def dfs(L):
    global check, cnt
    if L >= m:
        for c in check:
            print(c, end = ' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            check[L] = i
            dfs(L+1)


n, m = map(int, input().split())
check=[0]*m
cnt = 0
dfs(0)
print(cnt)

