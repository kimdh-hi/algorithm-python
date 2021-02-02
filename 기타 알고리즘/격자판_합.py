
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
ans = -2147000000


for i in range(n):
    x = y = 0
    for j in range(i,n):
        x += matrix[i][j] # 행의 합
        y += matrix[j][i] # 열의 합
    if ans < max(x, y):
        ans = max(x, y)

dig1 = dig2 = 0
for i in range(n):
    dig1 += matrix[i][i]
    dig2 += matrix[i][n-i-1]
print(max(ans, dig1, dig2))
'''
입력
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

출력
155


'''