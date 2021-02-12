import sys

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

arr = [0] * 52

for s in s1:
    arr[s] += 1

for s in s2:
    arr[s] -= 1

for s in s1:
    if arr[s] > 0:
        print("NO")
        break
