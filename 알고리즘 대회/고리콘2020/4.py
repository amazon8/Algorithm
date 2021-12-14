import sys

num = int(input())
drink = sorted(list(map(int, sys.stdin.readline().split())))
new = float

# 새로운 드링크 만들기
for i in range(num-1):
  new = drink[0]/2 + drink[-1]
  drink.pop(0)
  drink.pop()
  drink.append(new)
  drink.sort()

if int(drink[0]) == drink[0]:
  print(int(drink[0]))
else:
  print(drink[0])