import time

n = int(input())
a = list(map(int, input().split()))
a.insert(0,0)
seq=[0]*n

start_time = time.time()
for i in range(1, n+1):
    for j in range(n):
        if a[i] ==0 and seq[j] ==0:
            seq[j] = i
            break
        elif seq[j] == 0:
            a[i] -= 1
end_time = time.time() - start_time
print(end_time)
for x in seq:
    print(x, end=' ')

# 3.4