
def solve(str):
    # 대소문자를 구분하지 않으므로 알파벳 26개의 빈도수만 관리
    alp = [0] * 26
    # 모두 소문자로 변환
    str = str.lower()

    # 아스키 값을 이용해서 알파벳의 빈도를 구한다.
    for s in str:
        alp[ord(s) - ord('a')] += 1

    max = 0 # 빈도가 가장 높은 알파벳의 빈도수
    max_idx = 0 # 빈도가 가장 높은 알파벳의 위치 (인덱스)
    for i in range(len(alp)):
        if alp[i] > max: # 빈도의 최대값을 갱신하면서 위치도 함께 갱신한다.
            max = alp[i]
            max_idx = i

    cnt = 0 # 빈도의 최대값이 2개 이상이라면
    for a in alp:
        if a == max:
            cnt += 1 # 최대값을 발견하면 카운트 증가
            if cnt >= 2: # 최대값이 2개 이상이라면 최대빈도를 가진 알파벳이 2개 이상이라는 것이므로 '?' 리턴
                return '?'

    return chr(max_idx + ord('a')).upper()

str = input()
print(solve(str))

