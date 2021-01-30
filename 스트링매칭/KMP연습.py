'''
initNext 구현방법

패턴의 1번째부터 비교시작

패턴이 일치했을 때
:j를 next[i]에 삽입 후 j증가
:i와 j증가

패턴이 불일치했을 때
:불일치 이후 패턴의 첫글자가 일치하는 곳으로 이동

개선된 유한 상태 장치
1. 기존의 유한 상태 장치를 그리기
2. 기존의 유한 상태 장치에서 연결된 상태노드의 값이 같다면 다음 상태노드로 이동
3. 상태노드의 값이 다르다면 그대
'''

def initNext1(p, m):
    m = len(p)
    next[0] = -1
    i = 0
    j = -1
    while i < M:
        next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

# next = [0] * 50
# pattern = '10100111'
# M = len(pattern)
# initNext1(pattern, M)
# for i in range(1, M):
#     print(next[i], end=' ')

def initNext2(p, m):
    m = len(p)
    next[0] = -1
    i = 0
    j = -1
    while i < M:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1
next = [0] * 50
pattern = '10100111'
M = len(pattern)
initNext2(pattern, M)
print(pattern)
for i in range(1, M):
    print(next[i], end=' ')

print()
next = [0] * 50
pattern = 'AAAAAAAA'
M = len(pattern)
initNext2(pattern, M)
print(pattern)
for i in range(1, M):
    print(next[i], end=' ')

print()
next = [0] * 50
pattern = 'abcabcabc'
M = len(pattern)
initNext2(pattern, M)
print(pattern)
for i in range(1, M):
    print(next[i], end=' ')

print()
next = [0] * 50
pattern = 'abcabcacab'
M = len(pattern)
initNext2(pattern, M)
print(pattern)
for i in range(1, M):
    print(next[i], end=' ')

print()
next = [0] * 50
pattern = 'bababcba'
M = len(pattern)
initNext2(pattern, M)
print(pattern)
for i in range(1, M):
    print(next[i], end=' ')





























