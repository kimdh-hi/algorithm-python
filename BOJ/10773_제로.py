
n = int(input())
arr = []
for i in range(n):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))