'''
생성자로 숫자를 만드는 규칙
자기숫자 + 각 자리수
'''


def find_non_self_number(number):
    sum = 0  # 각 자리수의 합을 담을 변수
    tmp = str(number)  # 문자열로 바꾸면 숫자를 문자열 슬라이싱 하듯 사용할 수 있음 (각 자리를 편하게 볼 수 있음)
    for n in tmp:
        sum += int(n)  # 각 자리수를 누적한다.
    return sum + number  # 자기자신 + 각 자리수의 합


# 생성자를 갖는 숫자들이 저장될 리스트
list = []

for i in range(1, 10001):
    # 1 ~ 10000 까지 하나씩 해당 숫자가 생성자를 갖고있는 지 확인한다.
    result = find_non_self_number(i)
    list.append(result)

for i in range(1, 10001):
    # 생성자를 갖는 리스트에 i가 있다면 해당 숫자는 셀프넘버가 아니다.
    if i in list:
        pass
    else:
        print(i)



