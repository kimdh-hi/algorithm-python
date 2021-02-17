from collections import deque

MAX_DIST = 10000

def bfs(v):
    dq = deque()
    dq.append(v)
    while dq:
        curr = dq.popleft()
        for i in (curr+1, curr-1, curr+5):
            if visited[i] == 0 and (0 < i < MAX_DIST):
                visited[i] = visited[curr] + 1
                if i == e:
                    return visited[i]
                dq.append(i)


s, e = map(int, input().split())
visited = [0] * (MAX_DIST+1)
visited[s] = 0
bfs(s)
print(visited[e])

