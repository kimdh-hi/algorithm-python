def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(v):
        visited[v] = 1
        for i in range(n):
            if computers[v][i] and visited[i] == 0:
                dfs(i)

    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    return answer

