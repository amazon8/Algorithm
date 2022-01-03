import math

num = int(input())

# 팩토리얼
factorial = math.factorial(num)
factorial = str(factorial)
zero_num = 0

for now in reversed(factorial):
  if now =='0':
    zero_num +=1
  else:
    print(zero_num)
    break