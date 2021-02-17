from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d_x = [1,0,-1,0] # x축 이동
d_y = [0,1,-0,-1] # y축 이동
visited = [[0]*n for _ in range(n)]
dq = deque()
dq.append((n//2, n//2)) # 홀수 배열만 입력되므로 가운데 좌표에서 기작
visited[n//2][n//2] = 1 # 시작좌표 표시
ans = arr[n//2][n//2] # 시작좌표 누적
L = 0
while True:
    if L == (n//2): break # n/2만큼만 반복하면 다이아몬드 순회 완료
    qsize = len(dq)
    for i in range(qsize):
        x, y = dq.popleft()
        for j in range(4):
            new_x = x + d_x[j]
            new_y = y + d_y[j]
            if visited[new_x][new_y] == 0:
                ans += arr[new_x][new_y]
                visited[new_x][new_y] = 1
                dq.append((new_x, new_y))
    L += 1

print(ans)
