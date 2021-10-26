n = int(input())

stack = []
sum = 0
for _ in range(n):
    num = int(input())
    if num == 0 and len(stack) > 0:
        sum -= stack.pop()
    else:
        sum += num
        stack.append(num)

print(sum)
