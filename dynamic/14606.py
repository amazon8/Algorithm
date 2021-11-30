height = int(input()) 
sum = [0 for i in range(height+1)]
if height >= 1:
  sum[1] = 0
if height >=2:
  sum[2] = 1
if height >= 3:
  sum[3] = 3


# heigt까지 값 채우기
for i in range(4, height+1):
  if i % 2 ==0:
    sum[i] = (i//2) * (i//2) + sum[i//2] * 2
  else:
    sum[i] = int(i//2) * (int(i//2)+1) + sum[int(i//2)] + sum[int(i//2)+1]

print(sum[height])