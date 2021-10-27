
def rotate_left(q):
    front = q.pop(0)
    q.append(front)
    return q

def rotate_right(q):
    back = q.pop()
    q.insert(0, back)
    return q

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
q = [i for i in range(1,n+1)]
res = 0

for num in num_list:
    qlen = len(q)
    idx = q.index(num)
    if idx < qlen - idx:
        while True:
            if num == q[0]:
                del q[0]
                break
            else:
                rotate_left(q)
                res += 1
    else:
        while True:
            if num == q[0]:
                del q[0]
                break
            else:
                rotate_right(q)
                res += 1

print(res)




