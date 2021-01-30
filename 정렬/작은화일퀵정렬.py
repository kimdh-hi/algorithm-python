def smallquickSort(a,l,r):
    if r-l <= m:
        insertionSort(a,l,r)
    else:
        v,i,j=a[r],l-1,r
        while True:
            i +=1
            while a[i]<v:
                i+=1
            j-=1
            while a[j] > v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
        a[i],a[r]=a[r],a[i]
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)
        print(a)

def insertionSort(a,l,r):
    for i in range(l+1,r+1):
        v,j=a[i],i
        while a[j-1] >v:
            a[j] = a[j-1]
            j -=1
        a[j]
        print(a)

def quickSort(a,l,r):
    if r > l:
        v,i,j = a[r],l-1,r
        while True:
            i = i+1
            while a[i]<v:
                i = i+1
            j -=1
            while a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
        a[i],a[r]=a[r],a[i]
        quickSort(a,l,i-1)
        quickSort(a,i+1,r)
    print(a)

m = 5
list2 = list(map(int,input().split()))
list2.insert(0,-1)
list = list(map(int, input().split()))
list.insert(0,-1)
smallquickSort(list, 0, len(list)-1)