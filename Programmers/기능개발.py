
import math
def solution(progresses, speeds):

    days = []
    # 각 작업별 작업시간에 따른 완료까지의 시간
    for p,s in zip(progresses, speeds):
        day = math.ceil((100-p) / s)
        days.append(day)

    # 첫번째 작업의 작업시간을 최대값으로
    max = days[0]
    # 첫번째 작업 완료일자 초기화
    answer = [1]

    for i in range(1, len(days)):

        # 최대 작업시간보다 적게 걸릴 때,
        if days[i] <= max:
            answer[-1] += 1 # 배열의 이전 원소에 +1
        # 최대 작업시간 보다 오래 걸릴 때,
        else:
            max = days[i] # 최대 작업시간 갱신
            answer.append(1) # 새로운 완료 일자 생성
    return answer

progresses = [93, 90, 55]
speeds = [1,30,5]
print(solution(progresses, speeds))
