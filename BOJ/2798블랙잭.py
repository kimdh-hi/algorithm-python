'''
브루트포스

문제
N장의 카드 중 M에 가장 가까운 3장의 카드의 합

1.
N개 중 3개를 고른 모든 결과를 배열에 담고 최대값 출력?
:itertools사용
'''

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

'''
2. 
3중 for문
'''
# import sys
# from itertools import combinations
#
# n, m = map(int, input().split())
# cards = list(map(int, sys.stdin.readline().split()))
# max = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             tmp = cards[i] + cards[j] + cards[k]
#             if max < tmp <= m:
#                 max = tmp
# print(max)




