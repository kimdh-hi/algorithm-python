
def solve(kg):
    result = 0
    while kg > 0:
        if kg % 5 == 0:
            tmp = kg // 5
            result += tmp
            for _ in range(tmp):
                kg -= 5
        else:
            kg -= 3
            result += 1

    return -1 if kg < 0 else result

n = int(input())
print(solve(n))