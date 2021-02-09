'''
(는 무조건 스택에 push
    막대기의 시작지점

)는 무조건 스택에서 pop
    이전값이 (라면 스택의 크기만큼 토막수 증가 - 레이저
    이전값이 )라면 막대의 끝이므로 1만큼 토막수 증가 - 막대기의 끝
'''

arr = list(map(str,input()))

stack = []
curr = ''
sum = 0
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i-1] == '(': # 레이저
                sum += len(stack)
        else:
            sum += 1

print(sum)

'''
입력
(((()(()()))(())()))(()())

출력 
24
'''