import random, time, sys
def partition(a, l, r):
    v = a[r]
    i = l-1
    j=r

    while True:
        while True:
            i+=1
            if not a[i]<v: break
        while True:
            j-=1
            if not a[j]>v: break
        if i>=j: break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i

def quickSort(a, l, r):
    M=20
    if r > l:
        i = partition(a, l, r)
        if (r - l) <= M:
            #print(a)
            return insertionSort(a, r)
        quickSort(a,l,i-1)
        quickSort(a, i+1, r)
    return a

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
    # list = [-1,6,2,8,1,3,9,4,5,10,7]
    # print(quickSort(list,0,len(list)-1))
    sys.setrecursionlimit(100000)
    list = []
    # N=50000
    # for i in range(0,N):
    #     list.append(random.randint(0,N))
    # list.insert(0,-1)
    # start_time = time.time()
    # quickSort(list,0,len(list)-1)
    # end_time = time.time() - start_time
    # print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
    # list.clear()
    #
    # N=100000
    # for i in range(0,N):
    #     list.append(random.randint(0,N))
    # list.insert(0,-1)
    # start_time = time.time()
    # quickSort(list,0,len(list)-1)
    # end_time = time.time() - start_time
    # print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
    # list.clear()
    #
    # N=150000
    # for i in range(0,N):
    #     list.append(random.randint(0,N))
    # list.insert(0,-1)
    # start_time = time.time()
    # quickSort(list,0,len(list)-1)
    # end_time = time.time() - start_time
    # print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
    # list.clear()


    print()

    N = 3000
    for i in range(0, N):
        list.append(random.randint(0,N))
    list.insert(0,-1)
    start_time = time.time()
    quickSort(list,0,len(list)-1)
    end_time = time.time() - start_time
    print('(난수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
    list.clear()

    for i in range(0, N):
        list.append(i)
    list.insert(0,-1)
    start_time = time.time()
    quickSort(list,0,len(list)-1)
    end_time = time.time() - start_time
    print('(정렬)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
    list.clear()

    for i in range(N,0,-1):
        list.append(i)
    list.insert(0,-1)
    start_time = time.time()
    quickSort(list,0,len(list)-1)
    end_time = time.time() - start_time
    print('(역수)퀵 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))