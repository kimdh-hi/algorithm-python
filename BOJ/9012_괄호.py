
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

for a in arr:
    stack = []
    flag = True
    for x in a:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                flag = False
                print("NO")
                break
            else:
                stack.pop()
    if not flag:
        continue
    if stack:
        print("NO")
    else:
        print("YES")


'''

'''