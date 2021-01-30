'''
풀이

BFS

1. 입력받은 좌표를 양방향 그래프로 나타내기 위해 [x][y] = [y][x] = 1로 컴퓨터 위치를 양방향으로 초기화
2. 시작 컴퓨터는 1이므로 큐에 1을 넣고 시작
3. 큐에서 하나 꺼내고 꺼낸 값을 방문 노드로 check
4. 꺼낸 값과 연결되는 값(꺼낸값을 x로 하는 모든 노드) 중 해당 노드에 컴퓨터가 있고(1), 방문되지 않았고, 큐에 있지 않는 값을
   모두 큐에 푸쉬
5. 위 작업을 반복하면 visited배열에는 1과 연결된 노드의 값만 담기게 됨
6. 1까지 포함되므로 -1하여 답 출력
'''
from collections import deque

n = int(input())
m = int(input())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1
q = deque()
q.append(1)
visited = []
def bfs():
    while q:
        v = q.popleft()
        visited.append(v)
        for i in range(n+1):
            if matrix[v][i] and i not in visited and i not in q:
                q.append(i)
    return len(visited) - 1
print(bfs())


