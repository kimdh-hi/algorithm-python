'''
N개 정수중 k개를 뽑는 조합의 합이 M의 배수인 개수

n개중 k개를 뽑는 문제이므로 조합문제임
매 레벨(재귀)마다 sum을 누적 후 배수확인
각 레벨마다 인덱스가 늘어나는 것임
    1,2,3,4 라면
    1로 가능한 조합 1,2 1,3 1,4 를 뽑음
    레벨이 증기되면 2부터 가능한 조합을 뽑는 것 !
'''

def dfs(L, s, sum):
    global cnt
    if L == k: # k개 만큼의 조합을 구성했을 때
        if sum % m == 0: # k개 조합의 합이 m의 배수인 경우
            cnt += 1
    else:
        for i in range(s, n):
            dfs(L+1, i+1, sum+arr[i])

n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0
dfs(0,0,0) # 레벨, 조합을 위한 인덱스, 각 레벨에서의 합계
print(cnt)
