'''
숫자n에서 m개 자리수를 제거했을 때 n이 최대가 되도록.
n의 순서는 유지되어야 함.

숫자 n리스트가 최대값이 되기 위해선 자기 앞 자리보다 뒷자리가 작아야 한다.
스택에 넣어가며 작은 값이 발견되면 pop, 자기보다 큰 값을 만날때까지 반복
'''
n, m = map(int, input().split())
nums = list(map(int, str(n)))

stack = []

for a in nums:
    # 빈 스택이 아니고
    # 제거해야 할 자리수(m)이 남았고
    # 스택의 최상단 값이 현재 값보다 작은 경우
    while stack and m > 0 and stack[-1] < a:
        stack.pop() # 현재 값이 앞으로 이동되어 삽입되도록 최상단 값 pop
        m -= 1 # 제거할 자리수 감소
    stack.append(a) # while문이 통과되었다면 리스트에는 현재 값보다 큰 값이 없다는 의미이므로 삽입
# 위 규칙으로 m만큼 제거를 못한 경우 남은 m개는 뒤에서부터 m개를 제거
if m != 0:
    stack = stack [:-m]
print(stack)

'''
입력예시
9977252641 5

출력
99776
'''