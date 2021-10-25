
import sys

n = int(input())
stack = []
for _ in range(n):
    # command = input() # 시간초과
    command = sys.stdin.readline().rstrip().split()
    a = command[0]
    if a == 'push':
        stack.append(int(command[1]))
    elif a == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif a == 'empty':
        print(0 if len(stack) > 0 else 1)
    elif a == 'size':
        print(len(stack))
    elif a == 'top':
        print(stack[-1] if len(stack) > 0 else -1)