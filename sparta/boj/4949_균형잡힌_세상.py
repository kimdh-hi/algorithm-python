'''
오답 케이스
')' 만 입력
']' 만 입력
'''

while True:
    str = input()

    if str == '.':
        break

    flag = True
    stack = []

    for s in str:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if len(stack) == 0 or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif s == ']':
            if len(stack) == 0 or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if len(stack) > 0:
        flag = False

    print('yes' if flag else 'no')
