'''
음이 아닌 정수배열과 정수n이 주어졌을 때,
정수배열 각 요소의 조합(더하기, 빼기)으로 n을 만들 수 있는 경우의 수

예제)
1,1,1,1,1로 3을 만들 수 있는 경우의 수 = 3

'''

def solution(numbers, target):
    q = [0] # Stack으로 사용할 list 초기화
    for n in numbers:
        s = [] # 매 반복마다 스택에 넣을 데이터
        for _ in range(len(q)): # 스택의 크기만큼
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)

print(solution([1,1,1,1,7], 3))