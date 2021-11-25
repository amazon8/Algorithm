s = input()
t = list(input())
num = len(t)-len(s)

# 거꾸로 하나씩 제거
for i in range(num):
  if t[-1] == 'A':
    t.pop()
  else:
    t.pop()
    t.reverse()

# 비교
if "".join(t)==s:
  print(1)
else:
  print(0)
