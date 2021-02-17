

def dfs(L, p):
    global cnt
    if L == n:
        for i in range(p):
            if 1 <= check[i] <= 26:
                print(chr(check[i]+64), end = '')
        print()
    else:
        for i in range(1, 27):
            if i == code[L]:
                check[p] = i
                dfs(L+1, p+1)
            elif i >= 10 and (code[L] == i//10 and code[L+1] == i%10):
                check[p] = i
                dfs(L+2, p+1)




code = list(map(int, input().rstrip()))
print(code)
n = len(code)
code.insert(n, -1)
check = [0] * (n+3)
cnt = 0
print()
dfs(0, 0)


