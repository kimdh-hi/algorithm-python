'''
디지털트리
'''
class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    # x의 k번째 비트만 뽑아내기 위함
    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)


class node:
    def __init__(self, key):
        self.key = bitskey(key)
        self.left = None
        self.right = None


class Dict:
    itemMin = bitskey(0)

    z = node(itemMin)
    head = node(itemMin)
    head.left = z
    head.right = z

    def insert(self, v):
        v = bitskey(v) # 비트수준 비교를 위해 v를 비트화
        b = maxb - 1
        x = self.head.left
        p = self.head

        # 트리의 노드의 끝까지 탐색하며 x가 삽입될 위치의 부모노드를 찾음
        while x.key.get() != self.z.key.get():
            p = x # 부모노드 값을 기륙
            if v.bits(b, 1): # b번째 비트가 1이라면 오른쪽으로
                x = x.right
            else:   # b번째 비트가 0이라면 왼쪽으로
                x = x.left
            b -= 1  # 다음 번째 비트 비교를 위해 b감소

        # x가 삽입될 위치를 찾은 후
        x = node(self.itemMin) #x를 노드로 초기화
        x.key = v   # x에 키값 삽입
        x.left = self.z # 왼쪽 오른쪽 노드를 끝노드로 초기화
        x.right = self.z
        # 자리를 찾는 반복 중 마지막에 b를 감소하며 나오므로 b+1번째 비트를 비교해야 함
        if v.bits(b + 1, 1): # 삽입될 값의 b+1노드가 1이라면 부모의 오른쪽에 삽입
            p.right = x
        else: # 삽입될 값의 b+1노드가 0이라면 부모의 왼쪽에 삽입
            p.left = x

    def search(self, v):
        v = bitskey(v) # 비트수준 비교를 위해 v를 비트화
        p = x = self.head.left
        b = maxb # n번째 비트부터 비교
        self.z.key = v
        while v.get() != x.key.get():
            b = b - 1
            if v.bits(b, 1):
                p = x
                x = x.right
            else:
                p = x
                x = x.left
        if x == self.z:
            return -1
        else:
            self.check(v.get(), p.key.get())
            return x.key.get()

    def check(self, x, p):
        print('key : %d , parents : %d'%(x,p))


import random, time


'''
10000 ~ 30000 난수
'''
# N = 10000
# maxb = 14
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
#
#     start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)디지털 탐색 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
# N = 20000
# maxb = 15
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
#
#     start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)디지털 탐색 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
# N = 30000
# maxb = 16
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
#
#     start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)디지털 탐색 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()

# maxb = 14
# N = 10000
# key = list(range(N))
# s_key = list(range(N, 0, -1))
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(역수)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()

# maxb = 14
# N = 10000
# key = list(range(N))
# s_key = list(range(N))
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(정렬)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()

# maxb = 14
# N = 10000
# key = list(range(1, N+1))
# s_key = []
# for i in range(1, int(N/2)+1):
#     s_key.append(i)
#     s_key.append(N-i)
#
# d = Dict()
# for i in range(0, N):
#     d.insert(key[i])
# start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(큰수작은수)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()


''' 
check함수
'''
maxb = 5
s_key = [1, 19, 5, 18, 3, 26, 9]
key = [1, 3, 5, 9, 18, 19, 26]
print(s_key)
N = len(s_key)
d = Dict()
for i in range(N):
    d.insert(s_key[i])
start_time = time.time()
for i in range(N):
    result = d.search(key[i])
end_time = time.time() - start_time
print('디지털 탐색 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
print('탐색 완료')