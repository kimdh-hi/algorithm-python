'''
브루트포스

풀이
:7명의 키의 합이 100이 되어야 하는 것은 9명의 키의 합에서 2명의 키의 합을 뺀 결과가 100이되는 것과 동일
:2중 for문으로 i번째와 i+1번째부터 끝까지 비교하며 i,i+1번째의 합을 전체 키의 합에서 뺀결과를 비교
'''
a = []
for i in range(9):
    a.append(int(input()))
tmp_sum = sum(a) # 9명 난쟁이 키의 합
a.sort() # 정렬된 출력을 위한 출력

for i in range(9):
    for j in range(i+1, 9): # i+1 번째 부터 비교
        # 7명의 난쟁이의 키의 합이 100이 되는 경우는
        # 9명의 난쟁이에서 2명의 키를 뺀 결과가 100인 것과 동일
        if tmp_sum - (a[i] + a[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    print(a[k])
            exit()




