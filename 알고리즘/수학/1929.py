1
start, end = map(int, input().split())

# 소수 판별
def check_prime(num):
  if num==1:
    return
  if num == 2:
    print(num)
    return
  for divide in range(2, num//2+1):
    if num % divide ==0:
      return
  print(num)
  return

if start <= 2:
  print(2)

if start % 2==0:
  start += 1

for now in range(start, end+1, 2):
  check_prime(now)