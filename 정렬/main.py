import random, time

def selectionSort(a, n):
    for i in range(1 , n):
        minIndex = i
        for j in range(i + 1, n + 1):
            if a[j] < a[minIndex]:
                minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]
    return a

def bubbleSort(a, n):
    for i in range(n,1,-1):
        for j in range(1,i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
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


def checkSort(a, n):
    isSorted=True
    for i in range(1,n):
        if (a[i] > a[i+1]) :
            isSorted = False
        if (not isSorted) :
            break
    if isSorted:
        print("정렬완료")
    else:
        print("오류발생")


#############################
# list = []
# N=5000
#
# for i in range(0,N+1):
#     list.append(random.randint(0,N))
#
# start_time = time.time()
# selectionSort(list,N)
# end_time = time.time() - start_time
# print('선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# checkSort(list,len(list)-1)

# list = []
# N=5000
#
# for i in range(0,N+1):
#     list.append(random.randint(0,N))
# start_time = time.time()
# bubbleSort(list,N+1)
# end_time = time.time() - start_time
# print('버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# checkSort(list,len(list)-1)

# list = []
# N=10000
# list.append(-1)
# for i in range(0,N-1):
#     list.append(random.randint(0,N))
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(난수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# checkSort(list,len(list)-1)

# list.clear()
# list.append(-1)
# for i in range(N,1,-1):
#     list.append(i)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(역수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# checkSort(list,len(list)-1)
#
# list.clear()
# list.append(-1)
# for i in range(1,N):
#     list.append(i)
# start_time = time.time()
# insertionSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# checkSort(list,len(list)-1)



list = []
for i in range(0,5000):
    list.append(i)
list.insert(0,-1)
checkSort(shellSort(list,len(list)-1),len(list)-1)
# list.insert(0,-1)
# print(list)
# print(len(list))
# print(shellSort(list,len(list)-1))














