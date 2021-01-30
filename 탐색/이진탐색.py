'''
binarySearch(a[], search_key, n)
    left<-0;
    right<-n-1;
    while (left <= right) do {
        mid <- (left + right) / 2;
        if (a[mid].key = search_key) then return mid;
        if (a[mid].key > search_key) then right <=- mid -1;
        else left <- mid +1;
    }
    return -1;
end binarySearch()
'''
import random, time, sys

class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key):
        left = 0
        right = len(Dict.a) - 1
        while left <= right:
            mid = int((left + right)//2)
            if Dict.a[mid].key == search_key:
                return mid
            if Dict.a[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def insert(self,v):
        Dict.a.append(node(v))

def insertionSort(a, n):
    for i in range(2,n):
        v = a[i]
        j=i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v
    return a



if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    N = 10000
    key = list(range(1, N+1))
    random.shuffle(key)
    s_key = list(range(1, N+1))
    random.shuffle(s_key)
    d1 = Dict()
    for i in range(N):
        d1.insert(key[i])
    s_start_time = time.time()
    key.sort()
    s_end_time = time.time() - s_start_time
    start_time = time.time()
    for i in range(N):
        result = d1.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            #print('탐색 오류')
            pass
    end_time = time.time() - start_time
    print('실행 시간 (N=%d) : %0.3f' % (N, end_time + s_end_time))
    print('탐색완료')
    key.clear()
    s_key.clear()

    N=20000
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    random.shuffle(key)
    random.shuffle(s_key)
    d2 = Dict()
    for i in range(N):
        d2.insert(key[i])
    s_start_time = time.time()
    key.sort()
    s_end_time = time.time() - s_start_time
    start_time = time.time()
    for i in range(N):
        result = d2.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            #print('탐색 오류')
            pass
    end_time = time.time() - start_time
    print('실행 시간 (N=%d) : %0.3f' % (N, end_time+s_end_time))
    print('탐색완료')
    key.clear()
    s_key.clear()

    N=30000
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    random.shuffle(key)
    print(key)
    random.shuffle(s_key)
    d3 = Dict()
    for i in range(N):
        d3.insert(key[i])
    s_start_time = time.time()
    key.sort()
    s_end_time = time.time() - s_start_time
    start_time = time.time()
    for i in range(N):
        result = d3.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            #print('탐색 오류')
            pass
    end_time = time.time() - start_time
    print('실행 시간 (N=%d) : %0.3f' % (N, end_time + s_end_time))
    print('탐색완료')
    key.clear()
    s_key.clear()


# def binarySearch(a, key, n):
#     l, r = 1, n
#     while l <= r:
#         mid = (l+r)//2
#         if a[mid] == key:
#             return mid
#         else:
#             if a[mid] > key:
#                 r = mid-1
#             else:
#                 l = mid+1
#     return -1
#
# list = [-1,1,2,3,4,5]
# print(binarySearch(list,3,len(list)))

