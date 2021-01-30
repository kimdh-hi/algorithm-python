import random, time, sys

def quickSort(a, l ,r):
    if l < r:
        i = partition(a, l, r)
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)
        print(a)
    return a

def partition(a, l, r):
    v = a[r]
    i = l-1
    j = r

    while True:
        while True:
            i+=1
            if not a[i] < v: break
        while True:
            j-=1
            if not a[j] > v: break
        if i>=j: break
        a[i],a[j] = a[j],a[i]
    a[i],a[r] = a[r],a[i]
    return i



list = list(map(int, input().split()))
list.insert(0,-1)
quickSort(list, 0, len(list)-1)




# if __name__ == '__main__':
#     sys.setrecursionlimit(10000)
#     list = []
#     N=100000
#     for i in range(0,N):
#         list.append(random.randint(0,N))
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
#     list.clear()
#
#     N=200000
#     for i in range(0,N):
#         list.append(random.randint(0,N))
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
#     list.clear()
#
#     N=300000
#     for i in range(0,N):
#         list.append(random.randint(0,N))
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
#     list.clear()
#
#     print()
#
#     N = 10000
#     for i in range(0, N):
#         list.append(random.randint(0,N))
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
#     list.clear()
#
#     for i in range(0, N):
#         list.append(i)
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(정렬)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
#     list.clear()
#
#     for i in range(N,0,-1):
#         list.append(i)
#     list.insert(0,-1)
#     start_time = time.time()
#     quickSort(list,0,len(list)-1)
#     end_time = time.time() - start_time
#     print('(역수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))




