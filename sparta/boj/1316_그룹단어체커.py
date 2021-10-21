
def solve(word):
    check_list = []
    check_stack = []

    for w in word:

        if len(check_stack) == 0 and w not in check_list:
            check_stack.append(w)
        elif len(check_stack) == 0 or check_stack[-1] is not w:
            if w in check_list:
                return False
            else:
                check_list.append(check_stack.pop())
    return True


n = int(input())

cnt = 0
for _ in range(n):
    word = input()
    if solve(word):
        cnt += 1

print(cnt)