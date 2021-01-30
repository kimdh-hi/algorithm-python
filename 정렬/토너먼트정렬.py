'''
최초 노드설정
1. 트리의 리프노드에 각 배열이 차례대로 위치해야 함
2. 예시를 봤을 때, 트리의 0번은 더미값임, 0인 상태로 초기화
3. n만큼 0을 삽입하고 후에 n만큼 배열을 순회하며 삽입
4. 배열이 홀수인 경우 끝에 0을 추가해줘야 함 (완전이진트리)
'''
'''
비교방법
1. 자식노드를 가진 가장 끝 부모노드의 자식부터 비교 
    tree길이 // 2 ==> 부모노드(parent)
    부모노드*2     ==> 왼쪽자식노드
    (부모노드*2)+1 ==> 오른쪽자식노드
2. 루트노드(1)의 자식까지 (parent>=1) parent를 감소해가며 큰 값을 부모노드로 삽입
3. 반복이 끝났다면 루트노드의 값을 새로운 배열b의 끝부터 저장
4. 루트노드의 값을 알아내어서 a에서 해당 값을 임의의 작은 값으로 만듬 (비교가 안되도록) => 중복되지 않는 키값이니 가능..?
5. 바뀐 a를 다시 initTree를 통해 토너먼트트리로 초기화 시키고 반복..
'''


def tournamentSort(a, n):
    initTree(a, n)
    tlen = len(tree)-1
    parent = int(tlen // 2)
    child = parent * 2
    cnt = 1
    while cnt <= n:
        parent = int(tlen // 2)
        while parent >= 0:
             if tree[child] < tree[child+1]:
                 tree[parent] = tree[child+1]
             else:
                 tree[parent] = tree[child]
             parent -= 1
             child = parent *2
        b[n-cnt] = tree[1]
        print(b)
        # if b == list2:
        #     print(b)
        for i in range(n):
            if a[i] == tree[1]:
                a[i] = 0
        del tree[1:]

        initTree(a, n)
        cnt+=1

def initTree(a, n):
    for i in range(n):
        tree.append(0)
    for i in range(n):
        tree.append(a[i])
    if (n%2) !=0:
        tree.append(0)
tree = [0]
list2 = list(map(int,input().split()))
list = list(map(int, input().split()))
b = list.copy()
tournamentSort(list,len(list))
# import random, time
# list = []
# tree = [0]
# N=15000
# for i in range(0, N-1):
#     list.append(N-i)
# b = list.copy()
# random.shuffle(list)
# start_time = time.time()
# tournamentSort(list,N-1)
# end_time = time.time() - start_time
# print('(난수)토너먼트 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
# tree = [0]
# b.clear()
#
# tree = [0]
# N=10000
# for i in range(0, N-1):
#     list.append(N-i)
# b = list.copy()
# random.shuffle(list)
# start_time = time.time()
# tournamentSort(list,N-1)
# end_time = time.time() - start_time
# print('(난수)토너먼트 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
# tree = [0]
# b.clear()
#
# tree = [0]
# N=15000
# for i in range(0, N-1):
#     list.append(N-i)
# b = list.copy()
# random.shuffle(list)
# start_time = time.time()
# tournamentSort(list,N-1)
# end_time = time.time() - start_time
# print('(난수)토너먼트 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
# list.clear()
# tree = [0]
# b.clear()
'''
                7
        7               5
   6        7      5       2 (n*2)/2
4   6   7   3   5   1   2   0
=> 7,7,5,6,7,5,2,4,6,7,3,5,1,2,0

                6
        6               5
   6        3      5        2 
4   6   0   3   5   1   2   0
=>6,6,5,6,3,5,2,4,6,0,3,5,1,2,0

                5
        4               5
   4        3      5        2 
4   0   0   3   5   1   2   0
=>5,4,5,4,3,5,2,4,0,0,3,5,1,2,
'''