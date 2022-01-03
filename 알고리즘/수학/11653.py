num = int(input())

# 소인수분해
while num > 1:
  for divide in range(2, num+1):
    if num % divide == 0:
      num = num//divide
      print(divide)
      break