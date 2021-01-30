'''
DFS
:words의 첫번째 문자열부터 순차적으로 target과 비교
:words의 길이만큼 visited배열 선언 후 방문되었던 words배열에 다시 접근하지 않도록 함
:visited가 0이라면,
 begin과 한 문자씩 words[i]번째를 비교
 다른 문자열이 발생하는 양을 저장
:다른 문자열이 발생하는 양이 1이라면,
 해당 인덱스를 방문처리하고 cnt를 늘리며 재귀
'''

def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    res = []
    def dfs(start, cnt):
        if start == target: # 타겟문자와 같은 경우
            res.append(cnt) # 최소값 비교를 위해 cnt 배열에 저장
            return
        else:
            for i in range(len(words)):
                if visited[i] == 1:
                    continue
                w_idx = 0
                for j in range(len(start)):
                    if start[j] != words[i][j]:
                        w_idx += 1
                if w_idx == 1:
                    visited[i] = 1
                    dfs(words[i], cnt + 1)
                    visited[i] = 0
    dfs(begin, 0)
    print(res)
    if len(res) != 0:
        answer = min(res)
    return answer

words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
begin = 'hit'
target = 'cog'
print(solution(begin, target,words))










