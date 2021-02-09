'''

21 9
'''
arr = input()
stack = []


for i in range(len(arr)):
    if arr[i].isdecimal():
        stack.append(int(arr[i]))
    else:
        if arr[i] == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(y + x)
        elif arr[i] == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif arr[i] == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(y // x)

print(stack[0])