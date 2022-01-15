now_year, now_month, now_day = map(int, input().split())
future_year, future_month, future_day = map(int, input().split())

# 총 날짜 계산
days = (future_year-now_year)*360 + (future_month - now_month) * 30 + (future_day - now_day)

# 휴가 계산
month_rest = days // 30
if month_rest > 36:
  month_rest = 36

year_num = days // 360

now_year_rest = 0
year_rest = 0
for now in range(1, year_num+1):
  year_rest += now_year_rest+15
  if now % 2 == 0:
    now_year_rest += 1

print(year_rest, month_rest)
print("{}days".format(days))
