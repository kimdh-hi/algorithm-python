'''
KMP Algorithm

1. LPS 배열을 구해야 함
    LPS배열은 패턴 스트링의 접두사와 접미사가 같은 최대 길이를 저장, 인덱스는 타켓 스트링의 인덱스가 됨
    ex)
        AB = 0
        ABA = 1 (A)
        ABAB = 2 (AB)
        ABCDEABC = 3 (ABC)
2. LPS 배열 구하는 방법 (패턴스트링(=p))
    lps배열을 초기화
    두 개의 인덱스를 사용 (패턴 스트링의 1번째부터 비교하는 i와 0번째부터 비교하는 j)
        i는 왜 1부터인가? => 0번째 끼리 비교하는 것은 의미가 없음 무조건 0임
    p[i]와 p[j]가 같은 경우
        lps배열의 j번째에 j+1 삽입
        => i=1, j=0일 때, 같다면 lps배열에는 j+1에 1이 삽입
        => i=2, j=1일 때, 같다면 lps배열애는 j+1에 2가 삽입 ...
        ==> 같다면 이 과정을 반복
    p[i]와 p[j]가 다른 경우
        lps배열의 j-1을 j에 삽입
        => i=1, j=0일 때, 같다면 lps배열의 j+1에 1이 삽입
        => i=2, j=1일 때, 다르다면 j에는 lps[j-1] 값이 삽입
        ==> lps[j-1] 즉 다르게 된 위치 전의 lps부터 다시 비교
'''

def calculateLPS(p, n):

    # 반환해줄 lps배열 초기화
    lps = [0 for i in range(n)]

    # 패턴이 일치하는 지 비교할 인덱스, 다르게 된 경우 lps의 인덱스로 사용됨
    j = 0

    # 0번째는 무조건 0이므로 비교할 필요 없음 1부터 시작
    for i in range(1, n):

        # 패턴이 불일치하는 경우
        while j > 0 and p[i] is not p[j]:
            j = lps[j-1]

        # 패턴이 일치하는 경우
        if p[i] is p[j]:
            # 인덱스 증가 i는 반복문을 돌며 증가됨
            j += 1
            # lps값 조정
            lps[i] = j
    return lps

def kmp(t, p , tn, pn):
    lps = calculateLPS(p, pn)
    j = 0
    ans = []
    for i in range(0, tn):

        while j > 0 and t[i] is not p[j]:
            j = lps[j-1]

        if t[i] == p[j]:
            if j == pn - 1:
                ans.append(i-pn+1)
                j = lps[j]
            else:
                j += 1
    return ans

targ = 'ABCABABACDDDABAC'
patt = 'aaaaaaaa'
print(calculateLPS(patt, len(patt)))

ans = kmp(targ,patt,len(targ), len(patt))

print(ans)
for i in range(0,len(ans)):
    print(targ[ans[i]:len(patt)])


































