m, year = map(int, input().split())
money = [0 for i in range(year+1)]
money[0] = m 

# 연도별 이자 추가
for i in range(1, 6, 2):
  for j in range(1, year+1):
    if i == 1:
      money[j] = max(money[j], int(money[j-i]*1.05))
    elif i ==3 and j-i>=0:
      money[j] = max(money[j], int(money[j-i]*1.2))
    elif i==5 and j-i>=0:
      money[j] = max(money[j], int(money[j-i]*1.35)) 

print(money[year])