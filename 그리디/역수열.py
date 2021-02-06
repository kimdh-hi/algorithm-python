

n = int(input())
a = list(map(int, input().split()))

tmp = [0] * (n + 1)

for i in range(n):
    cnt = 0
    for j in range(1, n+1):
        if cnt == a[i]:
            tmp[cnt] = i+1
            break
        elif tmp[j] == 0:
            cnt += 1

print(tmp)
