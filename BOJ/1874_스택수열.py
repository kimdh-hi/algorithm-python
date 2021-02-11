'''
문제가 왜이래 ..

n개 정수를 입력받음
스택을 이용해서 n개 정수의 출력을 만들어야 함.
스택에 push될 때 반드시 오름차순의 형태로 push가 되어야 함.


입력 4,3,6,8,7,5,2,1

4 -> 1,2,3,4 ++++
3 -> 1,2 --
6 -> 1,2,5,6 ++ -
8 -> 1,2,5,7,8 ++ -
7 -> 1,2,5 -
5 -> 1,2 -
1 -> --
'''

n = int(input())
stack = []
arr = []
ans = []
tmp = 1
flag = True
for i in range(n):
    arr.append(int(input()))

for a in arr:
    while tmp <= a: # 입력 정수만큼
        stack.append(tmp) # 스택에 오름차순으로 push
        tmp += 1 # push될 때마다 값 증가
        ans.append("+") # push 체크
    if stack and stack[-1] == a: # 스택 최상단 값이 일치할 때,
        stack.pop() # 해당 값 pop
        ans.append("-") # pop 체크
    else:
        flag = False
        break
if flag:
    for a in ans:
        print(a)
else:
    print("NO")



