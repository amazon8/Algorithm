'''
1. 소수 판별 함수 --> 시간 초과
  --> 시간 복잡도를 로그로 바꿔야 할듯,,
2. 해당 수에 확인하는 수를 루트 n 까지로 잡으니 시간초과 해결
♨ 시간초과의 경우 N --> logN 뿐만 아니라 루트 N(math.sqrt)으로도 줄일 수 있음!!
'''
import math

start, end = map(int, input().split())

# 소수 판별
def check_prime(num):
  if num==1:
    return
  if num == 2:
    print(num)
    return
  end = math.floor(math.sqrt(num))

  for divide in range(2, end+1):
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