'''
삽입 정렬의 문제점
    삽입될 때, 이웃한 위치로만 이동
    삽입되어야 하는 위치가 멀리 떨어져 있다면 많은 이동을 필요로 함

삽입 정렬의 문제점 개선
    삽입 정렬과 다르게 전체 리스트를 한 번에 정렬하지 않음


'''
import random, time

def shellSort(a, n):
    h=1
    for h in range(1, n, 3*h+1):
        ...

    while h > 0:
        for i in range(h+1, n+1, 1):
            v = a[i]
            j = i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j = j - h
            a[j] = v
        h = h // 3
    return a

def shellSortPrint(a, n):
    h=1
    for h in range(1, n, 3*h+1):
        ...

    while h > 0:
        for i in range(h+1, n+1, 1):
            v = a[i]
            j = i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j = j - h
            a[j] = v
            print(a)
        h = h // 3

# list2 = list(map(int,input().split()))
# list2.insert(0,-1)
list = list(map(int, input().split()))
list.insert(0,-1)
shellSortPrint(list, len(list))


# list = [-1,3,14,12,4,10,13,15,5,2,7,9,6,8,11,1]
# print(len(list))
# shellSortPrint(list,len(list)-1)

# list = []
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(난수)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(난수)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(난수)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# print()
#
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(난수)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# shellSort(list,N)
# end_time = time.time() - start_time
# print('(역수)쉘 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))