
# 반복되지 않는 첫번째 문잘를 찾아라.

input = "abadabac"

def find_not_repeating_character(string):
    alp = [0] * 26

    for s in string:
        alp[ord(s) - ord('a')] += 1

    for i in range(len(string)):
        if alp[ord(string[i]) - ord('a')] == 1:
            return string[i]
    return "_"


result = find_not_repeating_character(input)
print(result)