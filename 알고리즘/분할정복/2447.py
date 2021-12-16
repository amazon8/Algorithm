import sys

size = int(input())
n_size = 0
array = [[" " for col in range(size)]for row in range(size)]

# 9등분 해서 채워 넣기
def divide(row, col, size):
  for rows in range(row, row+size):
    for cols in range(col, col+size):
      if size != 3:
        n_size = size//3
        divide(row, col, n_size) 
        divide(row, col+n_size, n_size)
        divide(row, col+2*n_size, n_size)
        divide(row+n_size, col, n_size)
        divide(row+n_size, col+2*n_size, n_size)
        divide(row+2*n_size, col, n_size)
        divide(row+2*n_size, col+n_size, n_size)
        divide(row+2*n_size, col+2*n_size, n_size)
      else:
        array[row][col] = "*"
        array[row][col+1] = "*"
        array[row][col+2] = "*"
        array[row+1][col] = "*"
        array[row+1][col+1] = " "
        array[row+1][col+2] = "*"
        array[row+2][col] = "*"
        array[row+2][col+1] = "*"
        array[row+2][col+2] = "*"

divide(0, 0, size)
print = sys.stdout.write
for row in range(size):
  print(''.join(array[row])+"\n")
'''
for row in range(size):
  for col in range(size):
    print(array[row][col], end = '')
  print()
'''