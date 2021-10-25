current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#    북,동,남,서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽 회전 메서드
# 북 -> 서 0 -> 3
# 동 -> 북 1 -> 0
# 남 -> 서 2 -> 3
# 서 ->남  3 -> 2
def rotate(d):
    return (d + 3) % 4

# 현재 방향 기준 반대쪽 방향으로 이동하는 메서드
# 북 -> 남 0 -> 2
# 동 -> 서 1 -> 3
# 남 -> 북 2 -> 0
# 서 -> 동 3 -> 1
def go_back(d):
    return (d+2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    res = 0
    if room_map[r][c] == 0:
        res += 1
        room_map[r][c] = -1
    q = [(r,c,d)]

    while q:
        r, c, d = q.pop(0)
        d_idx = d
        for i in range(4):
            d_idx = rotate(d_idx)

            nr = r + dr[d_idx]
            nc = c + dc[d_idx]

            if 0 <= nr < n and 0 <= nc < m and room_map[nr][nc] == 0:
                room_map[nr][nc] = -1
                q.append((nr, nc, d_idx))
                res += 1
                break # break를 해주지 않으면 4방향 중 청소 가능한 영역이 있음에도 반복문의 마지막에서 청소불가능이고 뒷쪽도 막혀있다면 종료되어버림

            elif i == 3: # 4번째 방향 탐색시(마지막 탐색) 위 if문에 걸리지 않았다면 청소가능한 지역이 아니라는 것이므로 뒤쪽 이동한다 (방향유지)
                d_idx = go_back(d)
                nr = r + dr[d_idx]
                nc = c + dc[d_idx]
                q.append((nr, nc, d))

                if room_map[nr][nc] == 1: # 뒤쪽방향이 벽으로 막힌 경우
                    return res

    return res


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))


