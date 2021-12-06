num = int(input())
test =[]
for i in range(num):
  test.append(int(input()))
num_0 = 0
num_1 = 0
results = 0
result = [0 for i in range(41)]

# 피보나치
def fib(n):
  global num_0, num_1
  if n==0:
    num_0 += 1
    return 0
  elif n==1:
    num_1 += 1
    return 1    
  else:
    if result[n] != 0:
      return result[n]
    else:  
      result[n] = fib(n-1) + fib(n-2)
      return result[n]

results = fib(40)

for n in test:
  if n == 0:
    print(1, 0)
  else:
    print(fib(n-1), fib(n))