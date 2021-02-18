'''
2차원 리스트의 최솟값 좌표에서 최대값 좌표까지 현재 노드보다 높은 값의 노드만을 지나가며 도착하는 경우의 수
'''

def dfs(x, y):
    global ans
    if x == maxx and y == maxy:
        ans += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n: # 다음 좌표가 미로 내에 있는지 확인
                if check[nx][ny] == 0: # 다음 좌표가 이미 방문되었는지 확인
                    if m[nx][ny] > m[x][y]: # 다음 좌표값이 현재 좌표값보다 큰 지 확인
                        check[nx][ny] = 1 # 방문표시
                        dfs(nx, ny)
                        check[nx][ny] = 0 # 재귀를 마치고 돌아올 때 체크를 풀어주어야 함. (DFS에서 언제나 주의)
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]
mmax = -214000000
mmin = 214000000

# 리스트에서 최대값, 최소값의 좌표찾기
i=0
for t in m:
    if max(t) > mmax:
        mmax = max(t)
        maxx, maxy = i, t.index(mmax)
    if min(t) < mmin:
        mmin = min(t)
        minx, miny = i, t.index(mmin)
    i += 1

dx = [1,0,-1,0] # 이동방향
dy = [0,1,0,-1]
ans = 0
check[minx][miny] = 1 # 최소값 좌표를 시작으로 함
dfs(minx,miny) # 최소값 좌표를 시작으로 함
print(ans)