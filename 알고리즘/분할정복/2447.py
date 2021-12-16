'''
1. 분할정복 알고리즘 : 시간복잡도에 문제가 없는거 같은데 시간초과가 계속 해서 뜨네,,,
2. 분할정복 알고리즘 기존 문제풀이 방식에서 벗어나는 풀이
♨ 1. 분할정복 문제를 풀 때 어떠한 틀에 갇히지 말자!! --> 분할정복은 단순히 재귀의 형태로 문제 푸는 것을 의미
2. 리스트는 슬라이싱으로도 할당 가능
'''
import sys

size = int(input())
n_size = 0
array = [[" " for col in range(size)]for row in range(size)]

# 9등분 해서 채워 넣기
def divide(row, col, size):
  
  if size == 3:
    array[row][col] = "*"
    array[row][col+1] = "*"
    array[row][col+2] = "*"
    array[row+1][col] = "*"
    array[row+1][col+1] = " "
    array[row+1][col+2] = "*"
    array[row+2][col] = "*"
    array[row+2][col+1] = "*"
    array[row+2][col+2] = "*"
    return

  n_size = size //3
  divide(row, col, n_size)

  for rows in range(row, size, n_size):
    for cols in range(col, size, n_size):
      if rows != n_size or cols != n_size:
        for now_line in range(n_size):
          array[rows+now_line][cols:cols+n_size] = array[row+now_line][col:col+n_size]
  return        


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