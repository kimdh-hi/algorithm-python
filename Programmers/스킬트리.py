
def solution(skill, skill_trees):

    answer = 0

    for s in (skill_trees):
        skill_idx = 0
        flag = True
        for i in range(len(s)):
            if skill_idx < skill.find(s[i]):
                flag = False
                break
            elif (skill_idx == skill.find(s[i])):
                skill_idx += 1
        if flag:
            answer += 1
    return answer


skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
skill = "CBD"

print(solution(skill, skill_trees))
