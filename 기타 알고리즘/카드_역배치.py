
card = list(range(21))

def swap(arr, s,e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s+=1
        e-=1
    return arr

for i in range(10):
    ai, bi = map(int, input().split())
    for j in range((bi-ai+1)//2):
        card[ai], card[bi] = card[bi], card[ai]
        ai += 1
        bi -= 1

print(card[1:])
'''
▣ 입력예제 1 
5 10
9 13
1 2
3 4 
5 6 
1 2 
3 4 
5 6 
1 20 
1 20
▣ 출력예제 1
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''