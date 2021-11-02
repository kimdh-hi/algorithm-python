import sys
from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))
peeks = combinations(cards, 3) # cards배열에서 순서에 상관있게 3개를 고른 모든 경우
res = 0
for i in peeks:
    s = sum(i)
    if res < s <= m:
        res = s
print(res)