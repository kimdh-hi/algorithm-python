'''
n*n 격자판에서 다이아몬드 형태 요소의 합
'''
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

left = right = n//2 # 시작위치
sum = 0
for i in range(n):
    for j in range(left, right+1):
        sum += matrix[i][j]
    # n*n이므로 가운데를 기준으로 탐색범위 변경
    if i < n//2: # 왼쪽,오른쪽으로 확장해가며 탐색
        left -= 1
        right += 1
    else: # 왼쪽, 오른쪽을 감소해가며 탐색
        left += 1
        right -= 1

print(sum)
