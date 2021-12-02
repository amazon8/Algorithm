'''
1. 다이나믹으로 풀었는데 어디서 틀렸는지 모르겠음...
--> 80% 쯤에서 틀리다는데 반례가 뭐지,,,? 왠만한거는 다 넣어 봤는데
'''

m, year = map(int, input().split())
money = [0 for i in range(year+1)]
money[0] = m 

# 연도별 이자 추가
for term in range(1, 6, 2):
  for now_year in range(1, year+1):
    if term == 1:
      money[now_year] = max(money[now_year], int(money[now_year-term]*1.05))
    elif term == 3 and now_year - term >= 0:
      money[now_year] = max(money[now_year], int(money[now_year-term]*1.2))
    elif term == 5 and now_year-term >= 0:
      money[now_year] = max(money[now_year], int(money[now_year-term]*1.35)) 

print(money[year])