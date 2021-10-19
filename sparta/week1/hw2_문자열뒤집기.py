
# 0, 1로 구성된 문자열을 뒤집어서 모두 같은 문자로 맞추고 싶을 때 최소 뒤집는 횟수를 구하여라

input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    to_one = 0
    to_zero = 0

    if string[0] == '0':
        to_one += 1
    else:
        to_zero += 1
    for i in range(len(string)-1):
        if string[i] is not string[i+1]: # 앞 뒤가 달라지는 순간이 뒤집는 순간
            if string[i+1] == '0':
                to_one += 1
            else:
                to_zero += 1

    return min(to_one, to_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)