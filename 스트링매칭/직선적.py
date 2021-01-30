
def bututeForce(p, t):
    pn = len(p)
    tn = len(t)
    i=j=0
    while j < pn and i < tn:
        if p[j] != t[i]:
            i -= j
            j -= 1
        i += 1
        j += 1
    if j == pn:
        return i - pn
    else:
        return i

p = '1111'
t = '00001111'
print(bututeForce(p, t))