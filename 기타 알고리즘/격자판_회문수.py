'''
가로세로 방향으로 5자리 회문수가 몇 개 있는지
'''
matrix = [list(map(int, input().split())) for _ in range(7)]
ans = 0
for i in range(3):
    for j in range(7):
        tmp = matrix[j][i:i+5]
        if tmp == tmp[::-1]: # tmp의 역순 비교
            ans += 1
        flag = True
        for k in range(2):
            if matrix[i+k][j] != matrix[i+4-k][j]:
                flag = False
                break
        if flag:
            ans += 1

print(ans)
'''
입력
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

출력
3
'''