'''
요세푸스 문제랑 거의 똑같은 듯

n명의 왕자가 시계방향으로 돌아가며 k라는 숫자를 외침
외친 왕자에서 시계방향으로 k번째 왕자는 제외됨

마지막 남은 왕자의 번호

'''
n, k = map(int, input().split())

arr = [_ for _ in range(1,n+1)]
idx = 0
for i in range(n-1):
    idx += k-1
    if idx >= len(arr):
        idx = idx % len(arr)
    arr.pop(idx)
print(arr[0])

