
arr = input()

stack = []
ans = ''
for a in arr:
    if a.isalpha():
       ans += a
    else:
        if a == '(':
            stack.append(a)
        elif a == '+' or a == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop(0)
            stack.append(a)
        elif a == '*' or a == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(a)
        elif a == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)

