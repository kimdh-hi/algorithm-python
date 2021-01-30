from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def bfs(v):
        q = deque()
        q.append(v)
        while q:
            v = q.popleft()
            visited[v] = 1
            for i in range(n):
                if computers[v][i] and visited[i] == 0:
                    q.append(i)

    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1

    return answer