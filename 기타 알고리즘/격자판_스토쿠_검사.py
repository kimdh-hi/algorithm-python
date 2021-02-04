
n = 9
matrix = [list(map(int, input().split())) for _ in range(n)]
ch1 = [0]*n
ch2 = [0]*n
ch3 = [0]*n
for i in range(n):
    ch1 = [0] * n
    ch2 = [0] * n
    for j in range(n):
        ch1[matrix[i][j]] = 1
        ch2[matrix[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) !=9:
        print("NO")
        exit()
ch1 = [0]*n
ch2 = [0]*n
for i in range(3):
    for j in range(3):
        ch3 = [0] * n
        for k in range(3):
            for z in range(3):
                ch3[matrix[i*3+k][j*3+z]]
        if sum(ch3) != 9:
            print("NO")
            exit()
print("YES")
