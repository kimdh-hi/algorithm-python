
n = int(input())
time = []
end = 0
ans = 0

for i in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time = sorted(time, key=lambda t:t[0])
time = sorted(time, key=lambda t:t[1])

for s, e in time:
    if s >= end:
        end = e
        ans += 1
print(ans)
