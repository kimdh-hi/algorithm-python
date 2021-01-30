import random, time


def cocktailSort(a, n):
    l,r=1,n-1
    while l<r:
        for i in range(l,r):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]

        r-=1
        if a == list2:
            print(a)
        for i in range(r,l,-1):
            if a[i] < a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
        l+=1
        if a == list2:
            print(a)

    return a


list2 = list(map(int,input().split()))
list2.insert(0,-1)
list = list(map(int, input().split()))
list.insert(0,-1)
cocktailSort(list,len(list))



# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()

# print()
# list=[]
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(난수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# cocktailSort(list,N)
# end_time = time.time() - start_time
# print('(역수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))