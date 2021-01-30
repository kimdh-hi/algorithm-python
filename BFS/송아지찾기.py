'''
BFS
직선 위의 n부터 m까지 3가지 방법으로 이동시 m에 도달하는 최소 이동횟수
'''

from collections import deque

MAX_DIST = 10000 # 직선의 최대거리

n, m = map(int, input().split()) # 시작지점, 도착지점

visited = [0] * (MAX_DIST + 1) # 노드 방문여부 + 방문시 이동횟수 체크용도

dq = deque()
dq.append(n) # 출발 위치 초기화
visited[n] = 1 # 출발 위치 방문표시

while dq:
    now = dq.popleft() # 초기값 or 이동 후 현재 위치
    if now == m: # 이동 후 위치가 도착지점과 같다면 루프종료
        break
    for step in (now-1, now+1, now+5): # 이동 (뒤로1, 앞으로1, 앞으로5)
        if 0 < step <= MAX_DIST:
            if visited[step] == 0: # 방문되지 않았다면,
                visited[step] = visited[now] + 1 # 현재 위치까지의 이동횟수 + 1
                dq.append(step)
# 방문되지 않은 노드를 0으로 표현하기 위해 출발 위치를 1로 초기화하였으므로 -1 필요
print(visited[m]-1)