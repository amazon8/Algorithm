size = int(input())
array = []
for i in range(size):
  line = input()
  array.append(line)

# 해당 리스트 압축 --> 안되면 4개로 분할
def compress(row, col, size):
  now = array[row][col]
  for rows in range(row, row+size):
    for cols in range(col, col+size):
      if now != array[rows][cols]:
        n_size = size //2
        return "("+compress(row, col, n_size) + compress(row, col+n_size, n_size) + compress(row+n_size, col, n_size) + compress(row+n_size, col+n_size, n_size)+")" 
  return str(now)

result = compress(0, 0, size)

print(result)