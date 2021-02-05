'''
n명의 씨름 선수 지원자의 키와 몸무게가 입력 됨
씨름 선수 중 다른 어떤 씨름 선수보다 키와 몸무게가 모두 적다면 탈락된다.

씨름 선수로 선출되는 최대 인원수를 출력
'''

n = int(input()) # 씨름 선수 수
arr = [] # 씨름 선수 키, 몸무게 배열
for i in range(n):
    t, w = map(int, input().split())
    arr.append((t,w)) # 키, 몸무게 튜플로 저장
arr.sort(reverse=True, key=lambda x:x[0]) # 키 기준 내림차순 정렬
maxx = 0
ans = 0
for a, b in arr:
    if b > maxx: # 몸무게가 더 무거운지 비교
        # 내림차순 정렬된 상태이므로 앞선 요소보다 키는 작은 상태임
        # 따라서 몸무게만 비교하여 무겁다면 선출 후 몸무게를 갱신
        # 몸무게가 더 무겁지 않은 경우가 있다면 키, 몸무게 모두 적은 것이므로 선출되지 않음.
        ans += 1
        maxx = b # 몸무게 최대값 갱신

print(ans)

# drop = 0 # 탈락자 수
# for i in range(1, n): # 0번째는 키가 가장 크므로 무조건 선출됨 따라서 1번째 부터 시작
#     tt, tw = arr[i]
#     for j in range(i-1, -1, -1):
#         if tt < arr[j][0] and tw < arr[j][1]: # 키, 몸무게 모두 적은 선수
#             drop += 1 # 탈락자 증가
#             break
# print(n-drop)
'''
입력
5
172 67
183 65
180 70
170 72
181 60

출력
3
'''