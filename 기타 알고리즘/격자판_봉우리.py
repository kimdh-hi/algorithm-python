
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
d_x = [-1,0,1,0]
d_y = [0,1,0,-1]
matrix.insert(0,[0]*n)
matrix.append([0]*n)
ans = 0
for m in matrix:
    m.insert(0,0)
    m.append(0)

for i in range(n+1):
    for j in range(n+1):
       if all(matrix[i][j] > matrix[i+d_x[k]][j+d_y[k]] for k in range(4)):
           ans += 1
print(ans)
# ans_list = []
# for i in range(n+1):
#     for j in range(n+1):
#         flag = True
#         for k in range(4):
#             print(i+d_x[k])
#             if i+d_x[k] < 0 or j+d_y[k] < 0 or i+d_x[k] > n+1 or j+d_y[k] > n+1:
#                 flag = False
#                 break
#             if matrix[i][j] < matrix[i+d_x[k]][j+d_y[k]]:
#                 flag = False
#                 break
#         if flag:
#             ans_list.append((i,j))
#             ans += 1
# print(ans)

# for m in matrix:
#      print(m)
