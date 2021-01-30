'''
문자열 압축 kakao

1. 압축할 패턴을 뽑아내야 됨
    1-1 전체 문자열의 절반+1 (홀수길이대비)까지 반복
    1-2 1씩 늘려가며 패턴을 뽑아냄 (파이썬 슬라이싱)
2. 2중 포문
    2-1 외부 포문 인덱스부터 시작하여 패턴의 길이만큼 늘려가며 비교
    2-2 패턴과 패턴이후 전체 문자열의 패턴만큼 길이 문자열이 같다면 count증가
    2-3 다르다면, 카운트가 1이 아닐때 (1보다 큰 경우)
        임시문자열에 count+패턴 삽입
    2-4 다르다면, 카운트가 1일 때
        임시문자열에 패턴삽입
3. 패턴이동
    패턴 불일치가 발생하면 2-3, 2-4 수행 후 패턴을 j+i만큼 이동
    count초기화
4. i만큼 패턴을 잘라내어 비교 후 문자열 길이의 최소값을 유지
'''
def solve(s):
    answer = 99999
    for i in range(1, len(s)//2+1):
        pattern = s[:i]
        count = 1
        ret = ""
        for j in range(i, len(s) + i, i):
            if pattern == s[j:j+i]:
                count += 1
            else:
                if count != 1:
                    #ret = ret + str(count) + pattern
                    ret += str(count) + pattern
                else:
                    #ret = ret + pattern
                    ret += pattern

                pattern = s[j:j+i]
                count = 1
        answer = min(len(ret), answer)
    return min(answer, len(s))

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for s in a:
    print(solve(s))

