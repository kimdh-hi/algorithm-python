# 문자열 중 최빈 알파벳 찾기

# 최대값 찾기 함수
def find_max_item(array):
    num = array[0]
    max_idx = 0

    for i in range(1, len(array)):
        if array[i] > num:
            num = array[i]
            max_idx = i

    return max_idx


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for s in string:
        if s.isalpha():
            alphabet_occurrence_array[ord(s) - ord('a')] += 1

    # 최빈값에 해당하는 알파벳의 인덱스를 반환 (0=a)
    max_idx = find_max_item(alphabet_occurrence_array)

    return chr(max_idx + ord('a'))


print(find_alphabet_occurrence_array("hello my name is sparta"))
