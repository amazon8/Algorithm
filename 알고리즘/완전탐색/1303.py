import sys
sys.setrecursionlimit(10**9)

col_num, row_num = map(int, input().split())
spot = []
for i in range(row_num):
  row = input()
  row = list(row)
  spot.append(row)

# 전쟁터 dfs 
def dfs(row, col):
  global spot, count
  count += 1
  temp = spot[row][col]
  spot[row][col] = 0
  row_shifts = [-1, 1, 0, 0]
  col_shifts = [0, 0, -1, 1]
  for row_shift in row_shifts:
    for col_shift in col_shifts:
      if 0 <= row+row_shift <= row_num-1 and 0<= col+col_shift <= col_num-1 and spot[row+row_shift][col+col_shift] == temp:
        dfs(row+row_shift, col+col_shift)
  return count


w_res, b_res = 0, 0
for row in range(row_num):
  for col in range(col_num):
    count = 0
    if spot[row][col] == "W":
      w_res += dfs(row, col)**2
    elif spot[row][col] =='B':
      b_res += dfs(row, col)**2  

print(w_res, b_res)