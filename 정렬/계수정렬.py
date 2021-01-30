import time
def countingSort(a, n, m):
    b = [0 for i in range(n)]
    b.insert(0,-1)
    count = [0 for i in range(m+1)]

    for i in range(1,n):
        count[a[i]] += 1
    print(count)
    for j in range(2,m+1):
        count[j] = count[j-1] + count[j]
    print(count)
    for i in range(n-1,0,-1):
        b[count[a[i]]] = a[i]
        count[a[i]] = count[a[i]]-1
    a[1:n] = b[1:n]
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

list=[-1,0,9,8,7,6,5,4,3,2,1]
checkSort(list,len(list)-1)
print(countingSort(list,len(list),9))

# N=10000
# list=[]
# for i in range(0,N):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# countingSort(list,N,10001)
# print(list)
# checkSort(list,len(list))
# end_time = time.time() - start_time
# print('(정렬)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
#
#
# for i in range(N,0,-1):
#     list.append(i)
# list.insert(0,-1)
# start_time = time.time()
# countingSort(list,N,10001)
# end_time = time.time() - start_time
# print('(역수)삽입 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))