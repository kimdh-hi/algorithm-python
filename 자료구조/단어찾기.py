'''
n개 입력받은 단어 중 쓰이지 않은 단어
'''
n = int(input())
d = dict()
for i in range(n):
    word = input()
    d[word] = 1 # 단어를 key, val은 1로 체크

for i in range(n-1):
    word = input()
    d[word] = 0 # 쓰인 단어에 val을 0으로 체크

for key, val in d.items():
    if val: # val이 0인 것이 쓰이지 않은 것
        print(key)
        break
