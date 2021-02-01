'''
N개 문자열 중 문자열을 앞부터 읽었을 때와 뒤부터 읽었을 때 결과가 같은 문자열의 개수
'''
n = int(input())
sarr = []
for i in range(n):
    sarr.append(input().lower())
ans = []

for i in range(n):
    lt = 0
    rt = len(sarr[i])-1
    while True:
        if lt >= rt:
            #ans.append("YES")
            print("#",i+1," YES")
            break
        elif sarr[i][lt] == sarr[i][rt]:
            lt += 1
            rt -= 1

        else:
            print("#", i + 1, " No")
            #ans.append("NO")
            break
#print(ans)

'''
입력예시
5
level
moon
abcba
soon
gooG

출력

'''