'''
두 알파벳 문자열
문자열의 나열 순서는 다르지만 구성이 일치하다면 두 단어는 아나그램
'''

d1 = dict()
d2 = dict()

s1 = input()
s2 = input()

for s in s1:
    if d1.get(s):
        d1[s] += 1
    else:
        d1[s] = 1

for s in s2:
    if d2.get(s):
        d2[s] += 1
    else:
        d2[s] = 1

for i in d1.keys():
    if i in d2.keys():
        if d1[i] != d2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")