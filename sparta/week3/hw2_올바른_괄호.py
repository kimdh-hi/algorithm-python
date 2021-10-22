s = "(())()"


def is_correct_parenthesis(string):
    stack = list()

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!