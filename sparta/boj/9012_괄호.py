n = int(input())

for _ in range(n):
    stack = []
    flag = True
    str = input()
    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) <= 0:
                flag = False
                break
            elif stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
    if not flag:
        print('NO')
    else:
        print("NO" if len(stack) > 0 else "YES")
