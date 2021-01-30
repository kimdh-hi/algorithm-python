'''
sequentialSearch(a[], key, n)
    i<-1;
    while(i<=n and a[i].key==key) do {
        i<-i+1;
    }
    if (i=n+1) then return -1;
end sequentialSearch()
'''

import random, time

class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key):
        i = 0
        n = len(Dict.a)
        while i<n and Dict.a[i].key != search_key:
            i += 1
        if i == n:
            return -1
        else:
            return i

    def insert(self, v):
        Dict.a.append(node(v))

# N=10
# key = list(range(1,N+1))
# random.shuffle(key)
# s_key = list(range(1,N+1))
# d = Dict()
# cnt=1
# for i in range(0,N):
#     d.insert(key[i])
# for i in range(0,N):
#     result = d.search(s_key[i])
#     if result!=-1:
#         cnt += result+1
# print('%0.2f' %(cnt//10))


N = 5000
key = list(range(1, N+1))
s_key = list(range(1, N+1))
random.shuffle(key)
d1 = Dict()
for i in range(N):
    d1.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d1.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('오류')
end_time = time.time() - start_time
print('실행 시간 (N=%d) : %0.3f'%(N, end_time))
print('탐색완료')

key.clear()
s_key.clear()
N = 10000
key = list(range(1, N+1))
s_key = list(range(1, N+1))
random.shuffle(key)
d2 = Dict()
for i in range(N):
    d2.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d2.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('오류')
end_time = time.time() - start_time
print('실행 시간 (N=%d) : %0.3f'%(N, end_time))
print('탐색완료')

key.clear()
s_key.clear()
N = 15000
key = list(range(1, N+1))
s_key = list(range(1, N+1))
random.shuffle(key)
d3 = Dict()
for i in range(N):
    d3.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d3.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('오류')
end_time = time.time() - start_time
print('실행 시간 (N=%d) : %0.3f'%(N, end_time))
print('탐색완료')