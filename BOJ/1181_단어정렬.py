
n = int(input())
arr = []
arr2 = []
for i in range(n):
    s = input()
    if arr.__contains__(s):
        continue
    else:
        arr.append(s)
        arr2.append((s,len(s)))
arr2.sort(key=lambda x:(x[1],x[0]))
for a in arr2:
    print(a[0])
