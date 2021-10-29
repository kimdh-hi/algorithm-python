

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(start):
    q = [start]
    visited[start] = 1

    while(q):
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if adj[v][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
adj = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    # 양방향
    adj[a][b] = 1
    adj[b][a] = 1

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)