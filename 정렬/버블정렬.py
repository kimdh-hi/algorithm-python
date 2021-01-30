import random, time

def bubbleSort(a, n):
    for i in range(n,1,-1):
        for j in range(1,i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def bubbleSortPrint(a, n):
    for i in range(n,0,-1):
        for j in range(0,i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
        print(a)


list = list(map(int, input().split()))
bubbleSortPrint(list, len(list))


# list = []
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# print()

# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(난수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# bubbleSort(list,N)
# end_time = time.time() - start_time
# print('(역수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))