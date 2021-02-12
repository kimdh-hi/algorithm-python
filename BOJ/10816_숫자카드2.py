import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

dict = {}
for card in cards:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

print(' '.join(str(dict[t]) if t in dict.keys() else '0' for t in target))

# for t in target:
#     if t in dict.keys():
#         print(dict[t], end = ' ')
#     else:
#         print(0, end = ' ')