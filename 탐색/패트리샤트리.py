'''
패트리샤트리
'''
maxb = 5


#maxb = 14
#maxb = 15
#maxb = 16
def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64
    # 알파벳 아스키코드로 바꿔서 숫자로 바꿔줌


class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~ (~0 << j)


class node:
    def __init__(self, key):
        self.key = key
        self.b = None
        self.left = None
        self.right = None


class Dict:
    itemMin = bitskey(0)
    head = node(itemMin)

    head.b = maxb
    # 참조 인덱스 maxb로 초기화
    head.right = head.left = head

    # 헤드 초기화

    def search(self, v):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        # 헤드의 왼쪽에서 시작
        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1):
                # v의 x.b번째 비트가 1이라면
                x = x.right
            else:
                x = x.left
        if v.get() != x.key.get(): return self.itemMin
        # 못찾으면 0 리턴
        return x.key

    def insert(self, v):
        v = bitskey(v)
        i = maxb
        # 비트의 수 넣어줌
        t = self.head.left
        # 왼쯕으로 내려와서 시작
        p = self.head

        while p.b > t.b:
            p = t
            if self.bits(v, t.b, 1):
                # v의 t.b번째 비트가 1이라면
                t = t.right
            else:
                t = t.left

        if v.get() == t.key.get(): return

        while self.bits(t.key, i, 1) == self.bits(v, i, 1):
            # t.key의 i 번째의 비트가 1이고 v의 i 번쨰 비트가 1이라면
            i -= 1

        p = self.head
        x = self.head.left
        # p의 인덱스와 x의 인덱스는 역순으로 될수없다
        # !!!!!!!!!
        while p.b > x.b and x.b > i:

            # x.b가 탐색키, 삽입된 원소가 하나라도 있다면
            # b는 참고하고있는 인덱스

            p = x
            if self.bits(v, x.b, 1):

                x = x.right
            else:
                x = x.left

        t = node(self.itemMin)
        t.key = v
        t.b = i

        # 어느 비트에 위치에 있는지 넣어줌 , 실선 그려주는거
        if self.bits(v, t.b, 1):
            t.left = x
            t.right = t
        else:
            t.left = t
            t.right = x

        if self.bits(v, p.b, 1):
            p.right = t
        else:
            p.left = t

    def check(self, v):
        v = bitskey(v)
        x = self.head.left
        p = x
        b = maxb
        while v.get() != x.key.get():

            p = x
            b = b - 1
            if v.bits(b, 1):
                x = x.right
            else:
                x = x.left

        print('key : %d , parents : %d' % (x.key.get(), p.key.get()))

    def bits(self, item, bit, cmp):

        # 비트가 같으면 1
        if item.bits(bit, 1) == cmp:
            return 1
        else:
            return 0


import random, time

# N = 10000
# #maxb = 14
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
#     start_time = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result.get() == -1 or result.get() != s_key[i]:
#         print('탐색 오류')
# end_time = time.time() - start_time
# print('(난수)패트리샤 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()

# N = 20000
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
# print('(난수)패트리샤 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
# N = 30000
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
# print('(난수)패트리샤 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
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
# print('(역수) 패트리샤 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
#
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
# print('(정렬) 패트리샤 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()
#
#
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
# print('(큰수작은수) 패트리샤 트리 탐색 실행시간(N = %d) : %0.3f'%(N, end_time))
# print('탐색 완료')
# key.clear()
# s_key.clear()


s_key = [1, 19, 5, 18, 3, 26, 9]
key = [1, 3, 5, 9, 18, 19, 26]
print(s_key)
N = 7
d = Dict()
for i in range(N):
    d.insert(s_key[i])
start_time = time.time()
for i in range(N):
    result = d.search(key[i])
    d.check(key[i])
    if result.get() != key[i] or result == -1:
        print('오류')
end_time = time.time() - start_time
print('패트리샤 트리의 실행시간 (N=%d) : %0.3f' % (N, end_time))
print('탐색 완료')