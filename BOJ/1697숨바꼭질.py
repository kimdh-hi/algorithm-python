from collections import deque

MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX
q = deque()
def bfs(n):
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v-2, v+1, v*2):
            if 0 <= i < MAX and visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1 # n이 증가한 값의 이동거리가 됨
print(bfs(n))


from collections import deque
def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)
MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()

