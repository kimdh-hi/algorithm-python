'''
기수탐색트라이
'''
class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self, key):
        if key.get() == 0:
            self.key = bitskey(0)
            self.external = False
        else:
            self.key = key
            self.external = True
        self.left = 0
        self.right = 0

class Dict:

    itemMin = bitskey(0)
    head = 0
    head_check = False

    def search(self, v):
        v = bitskey(v)
        return self.searchR(self.head, v, maxb-1)

    def insert(self, v):
        v = bitskey(v)
        self.insertR(self.head, v, maxb-1)

    def insertR(self, h, v, d):
        if h == 0:
            # 내부노드라면

            h = node(v)
            if self.head_check == False:
                self.head = h
            return h

        if h.external:
            # 외부노드라면

            leaf = node(v)
            # 말단을 노드화
            h = self.split(leaf, h, d)
            if self.head_check == False:
                self.head = h
                self.head_check = True
            return h
        if v.bits(d, 1) == 0:
            # 비트가 0이면 왼, 1이면 오
            h.left = self.insertR(h.left, v, d - 1)
        else:
            h.right = self.insertR(h.right, v, d - 1)

        return h

    def split(self,p,q,d):
        # p = leaf , q = h
        t= node(self.itemMin)

        # q가 기존의 외부노드 ,p가 들어오려는 노드 0이면 둘다 왼쪽
        if ((p.key.bits(d,1)) *2 + (q.key.bits(d,1))) == 0:
            t.left = self.split(p,q,d-1)
        # q만 1인 경우
        elif ((p.key.bits(d,1)) *2 + (q.key.bits(d,1))) == 1:
            t.left = p
            t.right = q
        # p만 1인 경우
        elif ((p.key.bits(d,1)) *2 + (q.key.bits(d,1))) == 2:
            t.left = q
            t.right = p
        # 둘다 1인 경우 오른쪽으로 내려감
        elif ((p.key.bits(d,1)) *2 + (q.key.bits(d,1))) == 3:
            t.right = self.split(p,q,d-1)
        return t


    def searchR(self,h,v,d):
        if h==0:
            return self.itemMin

        if v.get() == h.key.get():
            return v

        if v.bits(d,1) == 0:
            return self.searchR(h.left,v,d-1)
        else:
            return self.searchR(h.right,v,d-1)

    def check(self, v):
        v = bitskey(v)
        b = maxb
        x = self.head
        print(v.get(), end=' ')

        while v.get() != x.key.get():
            b -= 1
            if v.bits(b, 1):
                x = x.right
                print('right', end=' ')
            else:
                x = x.left
                print('left', end=' ')
        print()
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수) 기수탐색 트라이의 실행시간 (N=%d) : %0.3f' % (N, end_time))
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)기수탐색 트라이의 실행시간 (N=%d) : %0.3f' % (N, end_time))
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)기수탐색 트라이의 실행시간 (N=%d) : %0.3f' % (N, end_time))
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(역수)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(정렬)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색오류')
# end_time = time.time() - start_time
# print('(큰수작은수)디지털 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()


''''
check
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
    d.check(key[i])
    if result.get() != key[i] or result.get() == -1:
        print('오류')
end_time = time.time() - start_time
print('기수탐색 트라이의 실행시간 (N=%d) : %0.3f' % (N, end_time))
print('탐색 완료')

