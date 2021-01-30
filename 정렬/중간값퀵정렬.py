def midquickSort(a,l,r):
    if r-l>l:
        mid = int((l+r)/2)

        if a[l]> a[mid]:
            a[l],a[mid] = a[mid],a[l]
        if a[mid] > a[r]:
            a[mid],a[r] =a[r],a[mid]
        if a[l]> a[mid]:
            a[l],a[mid]=a[mid],a[l]
        a[mid],a[r-1]=a[r-1],a[mid]
        v,i,j=a[r-1],l,r-1
       # print(a)

        while True:
            i +=1
            while a[i]<v:
                i+=1
            j-=1
            while a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]

        a[i],a[r-1]=a[r-1],a[i]
        midquickSort(a,l,i-1)
        midquickSort(a,i+1,r)
        print(a)

    elif a[l] >a[r]:
        a[l],a[r]=a[r],a[l]
        #print(a)

list2 = list(map(int,input().split()))
list2.insert(0,-1)
list = list(map(int, input().split()))
list.insert(0,-1)
midquickSort(list, 0, len(list)-1)
