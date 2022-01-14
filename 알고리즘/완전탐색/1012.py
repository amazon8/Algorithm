#배추 dfs
def dfs(row, col):
  global garden
  garden[row][col] = 100
  if garden[row-1][col] == 1:
    dfs(row-1, col)
  if garden[row+1][col] == 1:
    dfs(row+1, col)
  if garden[row][col-1] == 1:
    dfs(row, col-1)
  if garden[row][col+1] == 1:
    dfs(row, col+1)
  return



test_num = int(input())
for i in range(test_num):
  row_num, col_num, cabage_spot_num = map(int, input().split())
  garden = [[0 for col in range(col_num+1)]for row in range(row_num+1)]
  row, col = 0, 0
  for i in range(cabage_spot_num):
    cabage_row, cabage_col = map(int, input().split())
    garden[cabage_row][cabage_col] = 1

  count = 0
  # 개수 탐색 
  for row in range(row_num):
    for col in range(col_num):
      if garden[row][col] == 1:
        count += 1
        dfs(row, col)

  print(count)