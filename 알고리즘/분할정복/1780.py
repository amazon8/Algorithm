size = int(input())
paper = [0 for i in range(size)]
for i in range(1, size+1):
  row = list(map(int, input().split()))
  paper.append(row)

  