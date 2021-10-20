def find_self_number(number):
    sum = number
    tmp = str(number)
    for n in tmp:
        sum += int(n)
    return sum

list = []
for i in range(1, 10001):
    list.append(find_self_number(i))

for i in range(1, 10001):
    if i in list:
        pass
    else:
        print(i)