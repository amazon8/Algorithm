'''
♨ 변수 네이밍이 중요함을 느낌!! --> 코드가 길어지면 코드 진행 안에서 변수의 의미가 헷갈리는 경우가 생김!
'''

r, c, w = map(int, input().split())
a = [[1 for i in range(31)]for j in range(31)]

# 파스칼 삼각형 만들기
for row in range(3, 30):
  for col in range(2, row):
    a[row][col] = a[row-1][col-1]+a[row-1][col]

# 해당 크기 만큼 더하기
sum = 0
for row in range(r, r+w):
  col_num = 1
  row_now = row - r +1
  while col_num <= row_now:
    sum += a[row][c+col_num-1]
    col_num+=1

print(sum)