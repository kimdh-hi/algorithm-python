
class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BST:
    x = p = node()
    null_node = node(key=0, left=0, right=0)
    null_node.left = null_node
    null_node.right = null_node
    head = node(key=0, left=0, right=null_node)

    def insert(self, v):
        x = p = self.head # 헤드부터 삽입위치 탐색
        while x != self.null_node:
            p = x
            if v == x.key: return
            if v < x.key:
                x = x.left
            else:
                x = x.right
        x = node(v, self.null_node, self.null_node)
        if v < p.key:
            p.left = x
        else:
            p.right = x

    def search(self, s_key):
        x = p = self.head # 헤드부터 탐색
        while x != self.null_node:
            p = x
            if s_key == x.key:
                return x.key
            if s_key < x.key:
                x = x.left
            else:
                x = x.right
        return -1

N = 1000
key = [i for i in range(N)]
s_key = [i for i in range(N)]
b  = BST()
for i in range(N):
    b.insert(key[i])
for i in range(N):
    result = b.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('오류')
print('탐색완료')



