def solution(clothes):
    answer = 0
    l = []
    for c in clothes:
        l.append(c[1])
    ls = set(l)
    if len(ls) != 1:
        answer = len(clothes) + len(ls)
    else:
        answer = len(clothes)
    return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
clothes2 = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
print(solution(clothes2))
