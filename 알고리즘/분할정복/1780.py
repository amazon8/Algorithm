size = int(input())
paper = []
n_size = 0
count = [0, 0, 0]
for i in range(1, size+1):
  row = list(map(int, input().split()))
  paper.append(row)

# 종이를 작은 종이로 분할

def check(row, col, size):
  now = paper[row][col]
  for rows in range(row, row+size):
    for cols in range(col, col+size):
      if now!=paper[rows][cols]:
        n_size = size//3
        check(row, col, n_size)
        check(row, col+n_size, n_size)
        check(row, col+2*n_size, n_size)
        check(row+n_size, col, n_size)
        check(row+n_size, col+n_size, n_size)
        check(row+n_size, col+2*n_size, n_size)
        check(row+2*n_size, col, n_size)
        check(row+2*n_size, col+n_size, n_size)
        check(row+2*n_size, col+2*n_size, n_size)
        return

  if now == -1:
    count[2] +=1
  elif now == 0:
    count[0] += 1
  elif now == 1:
    count[1] += 1
  return

check(0, 0, size)
print(count[2])
print(count[0])
print(count[1])