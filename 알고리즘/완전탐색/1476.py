e, s, m = map(int, input().split())
if e == 15:
  e = 0
if s == 28:
  s = 0
if m == 19:
  m = 0
num = 1

# 해당되는 수 나올때까지 num 증가
while True:
  if num % 15 == e and num % 28 == s and num % 19 == m:
    print(num)  
    break
  num += 1  
