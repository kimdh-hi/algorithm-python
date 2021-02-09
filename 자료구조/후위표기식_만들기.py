'''
중위표기식을 후위표기식으로 만들기

1. 숫자의 경우 정답문자열에 누적.
2. 연산자의 경우 (기본 사칙연산)
    스택의 최상단값이 자기와 같거나 높은 우선순위를 갖는다면 pop 후 정답문자열에 누적
    스택의 최상단값이 자기보다 낮은 우선순위를 갖는다면 스택에 push
2-1 +,- 연산자의 경우 가장 낮은 우선순위이므로 스택에 있는 연산자를 모두 pop함
    주의, 스택의 최상단이 여는괄호라면 pop하지 않고 그대로 push !!
3. 괄호의 경우
    여는괄호 '('는 무조건 스택에 push
    닫는괄호 ')'를 만난다면 '('까지 모두 pop 후 정답문자열에 누적
4. 모든 문자열 검사 후에 스택에 남은 문자열 모두 정답문자열에 누적
'''
arr = input()
ans = ''
stack = []
for i in range(len(arr)):
    if arr[i].isdecimal(): # 문자 형태의 숫자인지 판별
        ans += arr[i] # 숫자라면 정답 문자열에 누적
    else: # 숫자가 아니라면, 연산자라면
        if arr[i] == '(': # 여는 괄호라면 무조건 스택에 push (List append)
            stack.append(arr[i])
        elif arr[i] == '*' or arr[i] == '/': # *, /의 경우
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                ans += stack.pop() # 자기와 같거나 높은 우선순위 연산자 스택에서 pop후 누적
            stack.append(arr[i]) # 현재 연산자 push
        elif arr[i] == '+' or arr[i] == '-':  # +, -의 경우
            while stack and stack[-1] != '(': # (가 아니라면 계쏙 pop후 누적
                ans += stack.pop()
            stack.append(arr[i])
        else: # 닫는 괄호라면
            while stack and stack[-1] != '(': # 여는 괄호 전까지 모두 pop
                ans += stack.pop()
            stack.pop() # 여는괄호 pop
if stack: # 나머지 연산자 누적
    for s in stack:
        ans += s

print(ans)



