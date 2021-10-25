
n = int(input())
list = []
for i in range(n):
    a, b = map(int, input().split())
    list.append((a, b))

list = sorted(list, key=lambda x: (x[1], x[0]))

for l in list:
    print(l[0], l[1])