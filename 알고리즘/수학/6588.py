'''
1. num 입력
2. def check_composition 
'''

import math

array = [1 for i in range(1000001)]
array[0], array[1] = 0, 0

# 소수 판별 함수
def check_prime(num):
  start = 2
  end = math.floor(math.sqrt(num))+1
  for divide in range(start, end+1):
    if num % divide == 0:
      array[num] = 0 # 합성수 1은 소수
      return
  return    


# 소수 인지 판별  
for now in range(3, 1000001):
  check_prime(now)

# 소수 두개로 나누기
while True:
  num = int(input())
  if num == 0:
    exit()
  for first_prime in range(2, num):
    if array[first_prime] ==1:
      second_prime = num - first_prime
      if array[second_prime] ==1:
        print("{} = {} + {}".format(num, first_prime, second_prime))
        break




'''
# 소수 두개로 나누기
while num != 0:
  for first_prime in range(2, num):
    if check_composition(first_prime) != 0:
      second_prime = num - first_prime
      if check_composition(second_prime) != 0:
        print(first_prime, second_prime)
        break

  num = int(input())
'''
