
def solve(str):
    alp = [0] * 26
    str = str.lower()
    for s in str:
        alp[ord(s) - ord('a')] += 1

    max = 0
    max_idx = 0
    for i in range(len(alp)):
        if alp[i] > max:
            max = alp[i]
            max_idx = i

    cnt = 0
    for a in alp:
        if a == max:
            cnt += 1

    if cnt > 1:
        return '?'

    return chr(max_idx + ord('a')).upper()

str = input()
print(solve(str))

