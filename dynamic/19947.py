money, year = map(int, input().split())
num = [0 for i in range(3)]
num[0] = year//5
if num[0]!=0:
  year = year//5
num[1] = year//3
if num[1]!=0:
  year = year//3
num[2] = year

# 이자 추가
for i in reversed(num):
  for j in range(i):
    if i == 2:
      money += int(money*0.05)
    elif i==1:
      money += int(money*0.2)
    else:
      money += int(money*0.35)

print(money)