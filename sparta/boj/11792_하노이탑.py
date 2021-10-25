# n개 기둥을 _from에서 _to로 옮기는데 _mid를 보조기둥으로 사용한다.
def hanoi(n, _from, _to, _mid, move_list):
    # 원판의 개수(n)이 1이 되면 해당 원판을 목적지 기능(_to)로 이동한다.
    if n == 1:
        move_list.append((_from, _to))
        return

    hanoi(n-1, _from, _mid, _to, move_list)
    move_list.append((_from, _to))
    hanoi(n-1, _mid, _to, _from, move_list)


n = int(input())
# 1번 기둥의 3개 원판을 3번 기둥으로 옮기는데 2번 기둥을 보조기둥으로 사용한다.
move_list = []
hanoi(n,1,3,2, move_list)

print(len(move_list))
for move in move_list:
    print(move[0], move[1])

