'''
라이브러리를 사용하면 편하긴함 ..

실제 코테에서 라이브러리를 사용하지 못할수도
따라서 순열문제는 기본적으로 재귀를 통해 풀도록.

but 시간복잡도의 차이는 크게 없음.
'''
import itertools as it

n, m = map(int, input().split())
arr = list(range(1,n+1))
binomal = [1] * n

# 파스칼의 삼각형을 계산하기 위한 이항계수
for i in range(1, n):
    binomal[i] = (binomal[i-1]*(n-i)) // i

# 순열 추출
for tmp in it.permutations(arr):
    sum = 0
    # 이항계수를 곱한 모든 결과를 누적
    for i in range(n):
        sum += tmp[i] * binomal[i]
    if sum == m: # 결과가 타겟과 같다면 출력 후 종료
        print(tmp)
        break