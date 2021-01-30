import random, time
'''
2번 째 원소부터 시작
두 번째 원소는 첫 번째 자료와 비교
세 번째 원소는 두 번째 첫 번째 원소와 비교
n 번째 원소는 n-1...첫 번째 원소와 비교 하며 자리를 찾음
'''

def insertionSort(a, n):
    for i in range(2,n):
        v = a[i]
        j=i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v
    return a

def insertionSortPrint(a, n):
    for i in range(2,n):
        v = a[i]
        j=i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v
        print(a)



list = list(map(int, input().split()))
list.insert(0,-1)
insertionSortPrint(list, len(list))


# list = []
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# print()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(역수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))