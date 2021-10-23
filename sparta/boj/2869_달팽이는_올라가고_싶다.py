
a, b, v = map(int, input().split())
one_day = a-b

if (v - a) % one_day == 0:
    print(((v-a) // (one_day))+1)
else:
    print(((v-a) // (one_day))+2)