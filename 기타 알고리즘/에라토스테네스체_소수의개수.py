'''
소수의 개수 - 에라토스테네스 체
'''
n = int(input())

check = [0] * (n+1)
ans = 0 # 소수의 개수
for i in range(2, len(check)): # 0, 1은 소수가 아니므로 2부터 시작
    if check[i] == 0: # i번째가 0이라면 해당 인덱스는 소수임을 의미
        ans += 1 # 소수 카운트 증가
        for j in range(i,len(check), i): # i의 배수들을 검사
            check[j] = 1 # i의 배수는 j는 i를 약수로 취하므로 소수가 아님을 체크 (1삽입)
print(ans)