
def digit(d, k):
    div = 1
    for i in range(1,k):
        div *= 10
    d = int(d / div)
    d %= 10
    print(d)

digit(123,3)