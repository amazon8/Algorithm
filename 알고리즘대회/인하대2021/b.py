'''
1. 해당 장소가 b가 되면서 뒤쪽으로 흰색이 뒤집히는 경우 카운트 하지 못함,,
'''

num = int(input())
spot = []
for row in range(num):
  rows = list(input())
  spot.append(rows)

# dfs
def dfs(row, col, count):
  global spot
  count += 1
  right_count, left_count, up_count, down_count, diagonal_count, ru_diagonal_count, lu_diagonal_count, ld_diagonal_count = 0, 0, 0, 0, 0, 0, 0, 0
  if col != num-1 and spot[row][col+1] =="W":
    right_count = right(row, col+1, count)
  if col != 0 and spot[row][col-1] =="W":
    left_count = left(row, col-1, count)
  if row != num-1 and spot[row+1][col] =="W":
    down_count = down(row+1, col, count)
  if row != 0 and spot[row-1][col] =="W":
    up_count = up(row-1, col, count)
  if col < num-1 and row < num-1 and spot[row+1][col+1] =="W":
    diagonal_count = diagonal(row+1, col+1, count)
  if col < num-1 and row > 0 and spot[row-1][col+1] =="W":
    ru_diagonal_count = ru_diagonal(row-1, col+1, count)
  if col > 0 and row <num-1 and spot[row+1][col-1] =="W":
    ld_diagonal_count = ld_diagonal(row-1, col-1, count)
  if col > 0 and row > 0 and spot[row-1][col-1] =="W":
    lu_diagonal_count = lu_diagonal(row+1, col+1, count)
  
  return (right_count + left_count + down_count + up_count + diagonal_count + ru_diagonal_count + lu_diagonal_count + ld_diagonal_count)

# 오른쪽 개수 확인
def right(row, col, count):
  if col == num-1:
    return 0
  elif spot[row][col+1] == "W":
    count += 1
    return right(row, col+1, count)
  elif spot[row][col+1] == "B":
    return count
  else:
    return 0
# 왼쪽 개수
def left(row, col, count):
  if col == 0:
    return 0
  elif spot[row][col-1] == "W":
    count += 1
    return right(row, col-1, count)
  elif spot[row][col-1] == "B":
    return count
  else:
    return 0

# 밑으로 개수
def down(row, col, count):
  if row == num-1:
    return 0
  elif spot[row+1][col] == "W":
    count += 1
    return down(row+1, col, count)
  elif spot[row+1][col] == "B":
    return count
  else:
    return 0

# 위로 개수
def up(row, col, count):
  if row == 0:
    return 0
  elif spot[row-1][col] == "W":
    count += 1
    return down(row-1, col, count)
  elif spot[row-1][col] == "B":
    return count
  else:
    return 0


# 대각선 개수
def diagonal(row, col, count):
  if row == num - 1 or col == num-1:
    return 0
  elif spot[row+1][col+1] == "W":
    count += 1
    return diagonal(row+1, col+1, count)
  elif spot[row+1][col+1] == "B":
    return count
  else:
    return 0

def ru_diagonal(row, col, count):
  if row == 0 or col == num-1:
    return 0
  elif spot[row-1][col+1] == "W":
    count += 1
    return diagonal(row-1, col+1, count)
  elif spot[row-1][col+1] == "B":
    return count
  else:
    return 0

def lu_diagonal(row, col, count):
  if row == 0 or col == 0:
    return 0
  elif spot[row-1][col-1] == "W":
    count += 1
    return diagonal(row-1, col-1, count)
  elif spot[row-1][col-1] == "B":
    return count
  else:
    return 0

def ld_diagonal(row, col, count):
  if row == num - 1 or col == 0:
    return 0
  elif spot[row+1][col-1] == "W":
    count += 1
    return diagonal(row+1, col-1, count)
  elif spot[row+1][col-1] == "B":
    return count
  else:
    return 0


res = [[0, 0, 0],
       [0, 0, 0]] 

# 판 전체 dfs로 탐색
for row in range(num):
  for col in range(num):
    count = 0
    if spot[row][col] == ".":
      temp_res = dfs(row, col, count)
      res.append([temp_res, col, row])

res.sort(reverse = True)
if res[0][0] == 0:
  print("PASS")
else:
  print(res[0][1], res[0][2])
  print(res[0][0])