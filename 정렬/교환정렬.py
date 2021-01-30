import random,time
'''
큰 값이 왼쪽으로 정렬됨 (내림차순)
왼쪽의 비교하는 값은 고정하고 오른쪽 값들과 비교
'''
def exchangeSort(a, n):
    for i in range(1,n-1):
        for j in range(i+1,n):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
    return a

# list = []
# N=5000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# exchangeSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=10000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# exchangeSort(list,N)
# end_time = time.time() - start_time
# print('(난수)선택 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# N=15000
# for i in range(0,N):
#     list.append(random.randint(0,N))
# list.insert(0,-1)
# start_time = time.time()
# exchangeSort(list,N)
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
# exchangeSort(list,N)
# end_time = time.time() - start_time
# print('(난수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# exchangeSort(list,N)
# end_time = time.time() - start_time
# print('(정렬)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# exchangeSort(list,N)
# end_time = time.time() - start_time
# print('(역수)버블 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))

