
tree = [0,1,2,3,4,5,6,7]

def dfs1(v): # 전위순회
    if v >= len(tree): return
    else:
        print(tree[v], end=' ')
        dfs1(v*2)
        dfs1((v*2)+1)

def dfs2(v): # 중위순회
    if v >= len(tree): return
    else:
        dfs2(v*2)
        print(tree[v], end = ' ')
        dfs2(v*2+1)

def dfs3(v): # 후위순회
    if v >= len(tree): return
    else:
        dfs3(v*2)
        dfs3(v * 2+1)
        print(tree[v], end = ' ')

print("==전위순회==")
dfs1(1)
print()

print("==중위순회==")
dfs2(1)
print()

print("==후위순회==")
dfs3(1)