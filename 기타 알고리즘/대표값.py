'''
n명의 학생의 성적 중 평균에 가장 가까운 학생은 몇 번째에 있는가?
(평균에 가장 가까운 학생이 2명 일 경우 성적이 높은 학생의 인덱스를 가져가도록.)
'''
import numpy as np

n = int(input())

narr = np.array(list(map(int,input().split())))
avg = int(narr.mean())
min = 2147000000
ans = 0
for i, item in enumerate(narr):
    min_tmp = abs(item - avg)
    if min_tmp < min:
        min = min_tmp
        ans = i
    elif min_tmp == min:
        if item > narr[ans]:
            ans = i

print(avg, ans + 1)

'''
입력예시
10
65 73 66 87 92 67 55 79 75 80
출력
74 9
'''