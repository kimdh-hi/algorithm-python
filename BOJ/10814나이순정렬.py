import sys
N = int(sys.stdin.readline())
list = []
for i in range(N):
    list.append(sys.stdin.readline().split())
list.sort(key=lambda x:int(x[0]))
'''
def func(x):
    return x[0]    
'''

for item in list:
    print(item[0], item[1])