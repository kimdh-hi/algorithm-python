'''
퀵 정렬 개선 2
중간 값 분할
    더미키 사용 x
    최악의 경우가 발생하는 확률을 낮춤
    전체 수행 시간을 5% 감소
'''

def quickSort(a, l, r):
    if r > l:
        i = partition(a, l , r)
        quickSort(a, l, i-1)
        quickSort(a,i+1,r)
    return a

def partition(a, l, r):
    v = a[r]
    i = l-1
    j = r
    while True:
        while True:
            i+=1
            if not v > a[i]: break
        while True:
            j-=1
            if not v < a[j]: break
        if i>=j: break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i


if __name__ == '__main__':
    list = [-1,9,3,1,275,513,38,20]
    print(quickSort(list,0,len(list)-1))