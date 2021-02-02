
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())


for _ in range(m):
    num, dirt, cnt = map(int, input().split())
    if dirt == 0:
        for i in range(cnt):
            matrix[num-1].append(matrix[num-1].pop(0))
    else:
        for i in range(cnt):
            matrix[num-1].insert(0,matrix[num-1].pop())

left, right = 0, n-1
ans = 0
for i in range(n):
    for j in range(left, right+1):
        ans += matrix[i][j]

    if i < n//2:
        left += 1
        right -= 1
    else:
        left -= 1
        right += 1

print(ans)



