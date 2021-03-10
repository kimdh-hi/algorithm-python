
str = input()
alp = [0] * 26

for s in str:
    alp[ord(s)-97] += 1
for a in alp:
    print(a, end=' ')