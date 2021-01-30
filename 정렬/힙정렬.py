import random, sys, time

def heapify(a, h, m):
    v = a[h]
    j=2*h
    while j <= m:
        if j<m and (a[j]<a[j+1]):
            j+=1
        if v >= a[j]:
            break
        else:
            a[int(j//2)]=a[j]
        j=2*j
    a[int(j//2)] = v


def heapSort(a, n):
    for i in range(int(n//2),0,-1):
        heapify(a,i,n)
    for i in range(n-1,0,-1):
        print(a)
        a[1],a[i+1] = a[i+1],a[1]
        heapify(a,1,i)
    return a

# list2 = list(map(int,input().split()))
# list2.insert(0,-1)
list = list(map(int, input().split()))

heapSort(list,len(list)-1)


# if __name__ == '__main__':
#     list = [-1,6,2,8,1,3,9,4,5,10,7]
#     heapSort(list, len(list) - 1)
    # list = []
    # N = 100000
    # for i in range(0, N):
    #     list.append(random.randint(0, N))
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(난수)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
    # list.clear()
    #
    # N = 200000
    # for i in range(0, N):
    #     list.append(random.randint(0, N))
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(난수)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
    # list.clear()
    #
    # N = 300000
    # for i in range(0, N):
    #     list.append(random.randint(0, N))
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(난수)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
    # list.clear()
    #
    # print()
    #
    # N = 10000
    # for i in range(0, N):
    #     list.append(random.randint(0, N))
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(난수)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
    # list.clear()
    #
    # for i in range(0, N):
    #     list.append(i)
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(정렬)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
    # list.clear()
    #
    # for i in range(N, 0, -1):
    #     list.append(i)
    # list.insert(0, -1)
    # start_time = time.time()
    # heapSort(list, N-1)
    # end_time = time.time() - start_time
    # print('(역수)힙 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))

