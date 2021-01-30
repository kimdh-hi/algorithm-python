def solution(a, b):
    week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    idx = 5
    s = 0
    for i in range(1,a):
        if i == 2:
            s += 29
        elif i == 8:
            s += 31
        elif i < 8:
            if i%2==0:
                s+=30
            else:
                s+=31
        else:
            if i%2==0:
                s+=31
            else:
                s+=30
    s += b
    s = s % 7
    return week[((s+idx)%7)-1]

a, b = map(int,(input().split()))
print(solution(a, b))