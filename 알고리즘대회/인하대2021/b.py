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
  right_count, down_count, diagonal_count = 0, 0, 0
  if col != num-1 and spot[row][col+1] =="W":
    right_count = right(row, col+1, count)
    print("오른쪽 끝 결과", right_count)
  if row != num-1 and spot[row+1][col] =="W":
    down_count = down(row+1, col, count)
  if col < num-1 and row < num-1 and spot[row+1][col+1] =="W":
    diagonal_count = diagonal(row+1, col+1, count)
  
  print(right_count, down_count, diagonal_count)
  return (right_count + down_count + diagonal_count)

# 오른쪽 개수 확인
def right(row, col, count):
  print("abs")
  if col == num-1:
    return 0
  elif spot[row][col+1] == "W":
    count += 1
    return right(row, col+1, count)
  elif spot[row][col+1] == "B":
    print("오른쪽 끝", count)
    return count
  else:
    return 0

# 밑으로 개수
def down(row, col, count):
  print("down")
  if row == num-1:
    return 0
  elif spot[row+1][col] == "W":
    count += 1
    return down(row+1, col, count)
  elif spot[row+1][col] == "B":
    return count
  else:
    return 0

# 대각선 개수
def diagonal(row, col, count):
  print("댁각선")
  if row == num - 1 or col == num-1:
    return 0
  elif spot[row+1][col+1] == "W":
    count += 1
    return diagonal(row+1, col+1, count)
  elif spot[row+1][col+1] == "B":
    return count
  else:
    return 0

res = []
# 판 전체 dfs로 탐색
for row in range(num):
  for col in range(num):
    count = 0
    if spot[row][col] == ".":
      temp_res = dfs(row, col, count)
      print("kkkk")
      res.append([temp_res, col, row])

print(res)