import sys

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

d = dict()

for s in s1:
    d[s] = d.get(s, 0) + 1

for s in s2:
    d[s] = d.get(s, 0) - 1

for s in s1:
    if d[s] > 0:
        print("NO")
        break
else:
    print("YES")
