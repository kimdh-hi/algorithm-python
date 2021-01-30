def merge2(list_a, low, mid, high):
    i=low
    j= mid+1
    k=low
    while(k <= high) :
        if(i> mid) :
            aux[k] = list_a[j]
            k += 1
            j += 1
        elif(j > high):
            aux[k] = list_a[i]
            k += 1
            i += 1
        elif(list_a[i] > list_a[j]):
            aux[k] = list_a[j]
            k += 1
            j += 1
        else:
            aux[k] = list_a[i]
            k += 1
            i +=1
    for i in range(low,high+1):
        list_a[i] = aux[i]
    # if list_a == list2:
    #     print(list_a)
    print(list_a)
def mergeSort(list_a, low, high):
    if(low>=high):
        return
    mid = int((low+high)/2)
    mergeSort(list_a,low,mid)
    mergeSort(list_a,mid+1,high)
    merge2(list_a,low,mid,high)

#list2 = list(map(int, input().split()))
list = list(map(int, input().split()))
aux = list.copy()
mergeSort(list,0, len(list)-1)

