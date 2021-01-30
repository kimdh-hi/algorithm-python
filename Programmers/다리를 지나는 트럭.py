'''
큐 사용

(append)--> Queue -->(pop(0))
이 로직으로 다리에서 1초에 1만큼 이동하는 로직 구현

'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length

    while q:
        answer += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))


