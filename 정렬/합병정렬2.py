
def mergeSort(list):

    if len(list) <= 1:     # 리스트 길이 1 이하이면 리턴
        return list

    mid = int(len(list) // 2)   # 분할을 위한 중간값
    # 분할을 위한 재귀 호출
    # mid를 기준으로 왼쪽, 오른쪽으로 나누어서 재귀, 분할
    left, right = mergeSort(list[:mid]), mergeSort(list[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    lp = rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result.extend(left[lp:])
    result.extend(right[rp:])
    print('left =', format(left))
    print('right =', format(right))
    print('result =', format(result))
    return result

import random , time

list = [10,9,8,7,6,5,4,3,2,1]
result = mergeSort(list)
print(result)

# if __name__ == '__main__':
#     list = []
#     N = 100000
#     for i in range(0, N):
#         list.append(random.randint(0, N))
#     list.insert(0, -1)
#     b = list.copy()
#     start_time = time.time()
#     mergeSort(list)
#     end_time = time.time() - start_time
#     print('(난수)합병 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
#     list.clear()
#     b.clear()
#
#
#     N = 200000
#     for i in range(0, N):
#         list.append(random.randint(0, N))
#     list.insert(0, -1)
#     b = list.copy()
#     start_time = time.time()
#     mergeSort(list)
#     end_time = time.time() - start_time
#     print('(난수)합병 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
#     list.clear()
#     b.clear()
#
#     N = 300000
#     for i in range(0, N):
#         list.append(random.randint(0, N))
#     list.insert(0, -1)
#     b = list.copy()
#     start_time = time.time()
#     mergeSort(list)
#     end_time = time.time() - start_time
#     print('(난수)합병 정렬 실행시간 (N=%d) : %0.3f' % (N, end_time))
#     list.clear()
#     b.clear()


