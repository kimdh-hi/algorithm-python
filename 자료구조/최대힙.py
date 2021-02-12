'''
최대힙

heapq는 기본적으로 최소힙으로 동작함
최소힙 그대로 동작하되 삽입시 부호를 뒤집어서 최대힙으로 동작하도록 함.
'''
import heapq as hq

tree = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if not len(tree):
            print(-1)
        else:
            print(abs(hq.heappop(tree)))
    else:
        hq.heappush(tree, -n)

