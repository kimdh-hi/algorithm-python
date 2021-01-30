import random, time

def selectionSort(a, n):
    for i in range(1 , n):
        minIndex = i
        for j in range(i + 1, n + 1):
            if a[j] < a[minIndex]:
                minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]
    return a

def selectionSortPrint(a, n):
    for i in range(0 , n-1):
        minIndex = i
        for j in range(i + 1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]
        print(a)


list = list(map(int, input().split()))
selectionSortPrint(list, len(list))





# list = []
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# print()
#
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('(역수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))

