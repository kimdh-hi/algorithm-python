def merge(a, b):
    i, j = 0, 0
    m = []
    n1 = len(a)
    n2 = len(b)
    while i < n1 and j < n2:
        if a[i] < b[j]:
            m.append(a[i])
            i += 1
        else:
            m.append(b[j])
            j += 1
    if i==n1:
        for k in range(j, n2):
            m.append(b[k])
    else:
        for k in range(i, n1):
            m.append(a[k])
    return m


def naturalmergeSort(a, n):
    i = 0
    x = []
    while i < n:
        y = []
        y.append(a[i])
        while i+1 < n and a[i] <= a[i+1]:
            y.append(a[i+1])
            i += 1
        x.append(y)
        i +=1
    print('최초 런:', x)

    n =len(x)
    while n > 1:  ## n이 1이면 런이 하나이므로 모두 정렬
        i = 0
        z = []
        while i < n:
            if i == n-1:
                z.append(x[i])
            else:
                z.append(merge(x[i], x[i+1]))
            i += 2
        x = []
        n = len(z)
        for j in range(n):
            x.append(z[j])
        print('과정 : ', x)
    print('정렬완료 : ', x[0])

list2 = list(map(int,input().split(' ')))
list = list(map(int, input().split()))
naturalmergeSort(list, len(list))
# '''
# makeRun(a[], N)
#     run <- [];
#     tmp <- [];
#     comp <- 0
#
#     for(i<-0; i<N; i<-i+1) do {
#         if(a[i] > comp) then {
#             "리스트 tmp에 새로운 원소 comp 추가"
#             comp <- a[i]
#         }else
#             "리스트 run에 새로운 원소 리스트tmp 추가"
#             comp <- a[i]
#             tmp <- []
#             "리스트 tmp에 새로운 원소 a[i] 추가"
#             if(i >= N-1) then
#                 "리스트 run에 새로운 원소 리스트tmp 추가"
#     }
#     return run
# end makeRun()
# '''
#
#
# # def makeRun(a, N):
# #     run = []
# #     tmp = []
# #     comp = 0
# #
# #     for i in range(N):
# #         if a[i] > comp:
# #             tmp.append(a[i])
# #             comp = a[i]
# #         else:
# #             run.append(tmp)
# #             comp = a[i]
# #             tmp = []
# #             tmp.append(a[i])
# #             if i >= N-1:
# #                 run.append(tmp)
# #     return run
#
#
# def makeRun(a, run):
#     i = j = 1
#     for i in range(1,N):
#         if a[i] > a[i+1]:
#             run[j] = i
#             j += 1
#     return j - 1
#
# def merge(a, l, m, r):
#     i=j=0
#     for i in range(m + 1, 1, -1):
#         b[i - 1] = a[i - 1]
#     i -= 1
#     for j in range(m, r):
#         b[r + m - j] = a[j + 1]
#     j += 1
#     for k in range(l, r + 1):
#         if b[i] < b[j]:
#             a[k] = b[i]
#             i += 1
#         else:
#             a[k] = a[j]
#             j -= 1
#
# def moveRun(run, cnt):
#     i=j=1
#     for i in range(2,cnt+1,2):
#         run[j] = run[i]
#         j+=1
#     if (cnt%2) !=0:
#         run[j] = run[i-1]
#     else: j-=1
#
#     return j
#
# def naturalMergeSort(a, n):
#     run[0] = 0
#     cnt = makeRun(a, run)
#     while cnt > 1:
#         if (cnt%2) != 0:
#             num = cnt-1
#         else:
#             num = cnt
#         for i in range(1,num+1,2):
#             merge(a, run[i-1]+1, run[i], run[i+1])
#         cnt = moveRun(run, cnt)
#     return a
#
# #list2 = list(map(int,input().split()))
# # list = list(map(int, input().split()))
# # N = len(list)
# # print(N)
# # b = run = [0 for i in range(N+1)]
# # naturalMergeSort(list,N)
# #
# import random, sys, time
# if __name__ == '__main__':
#     N = 10
#     a = [6,7,8,3,4,1,5,9,10,2]
#     b = run = [0 for i in range(N+1)]
#
#     print(naturalMergeSort(a, N))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
