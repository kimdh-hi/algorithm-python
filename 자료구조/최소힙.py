'''
최소힙

1. 부모노드가 자식노드 보다 작게 구성
2. pop시
    루트노드가 pop되고 가장 마지막 리프노드가 루트로 올라감
    이후 heapify진행 (down-heap)
3. push시
    가장 마지막 리프노드에 삽입
    이후 heapify진행 (up-heap)
'''
import heapq as hq

tree = []
while True:
    n = int(input())
    if n == -1: # 루프 종료조건
        break
    if n == 0: # pop
        if not len(tree): # 힙이 비었다면 -1 출력
            print(-1)
        else: # 루트노드에서 pop
            print(hq.heappop(tree))
    else: # push
        hq.heappush(tree, n) # tree에 n 푸쉬

