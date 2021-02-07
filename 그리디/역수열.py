'''
0을 만날 때마다 카운트 ++

카운트와 입력수열이 같다면
'''
import time

n = int(input()) # 8개

arr = list(map(int, input().split())) # 입력받은 배열
tmp = [0] * n # 0으로 초기화된 배열
start_time = time.time()
for i in range(n): # 입력받은 배열 제어
    cnt = 0 # 0을 만날때마다 증가될 변수
    for j in range(n): # tmp배열을  순회할 배열
        if arr[i] == cnt: # 0을 만난 횟수와 같다면
            if tmp[j] != 0: # 같은데 삽입할 곳이 0이 아니라면
                j+=1 # 다음 0을 맘날때까지 인덱스 증가
                continue
            tmp[j] = i+1
            break
        if tmp[j] == 0: # 0을 만났을 때
            cnt += 1
end_time = time.time() - start_time
print(end_time)
print(tmp)

# 0.0019299983978271484
#.002805948257446289