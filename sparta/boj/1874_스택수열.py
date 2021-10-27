
n = int(input())
cnt = 1
flag = True
push_pop = []
stack = []
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        push_pop.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        push_pop.append('-')
    else:
        # 일단 입력은 끝까지 다 받아야 하니까 flag로 처리
        flag = False

if not flag:
    print('NO')
else:
    for p in push_pop:
        print(p)






