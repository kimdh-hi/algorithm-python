'''
1. 각 노드는 Red or Black
2. 루트노드와 모든 리프노드는 Black
3. Red노드의 자식들은 전부 Black (즉, Red노드는 연속되지 못함)
4. 모든 노드애 대해서 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 Black노드가 존재한

'''
##red_black tree
black = 0
red = 1


class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right


class Dict:
    x = p = q = gg = node

    z = node(color=black, key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(color=black, key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right

        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x

            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)

        x = node(color=red, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black

        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black

    def rotate(self, v, y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right

        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc


import random, time

# N= 10
N = 10000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))

# key = [2,1,8,9,7,3,6,4,5]
# s_key = [2,1,8,9,7,3,6,4,5]
# s_key.sort()
# print(s_key)
# N = len(key)
# random.shuffle(key)
# print(key)

# d=Dict()


for i in range(0, N):
    # print(key[i])
    d.insert(key[i])

start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("error")
end_time = time.time() - start_time

# print(d)
print("실행 시간 (N=%d) : %0.3f" % (N, end_time))
print("탐색 완료")




















