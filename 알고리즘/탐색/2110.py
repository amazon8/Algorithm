home_num, wifi_num = map(int, input().split())
spot = []
for i in range(home_num):
  spot.append(int(input()))
spot.sort()
start = spot[1] - spot[0]
end = spot[-1] - spot[0]


# 거리 이진탐색으로 찾기
while start <= end:
  temp_num = 0
  mid = (start+end) // 2
  base = spot[0]
  for now_spot in spot:
    if now_spot >= base + mid:
      temp_num += 1
      base = now_spot

  if temp_num >= wifi_num-1:
    start = mid + 1
  else:
    end = mid -1

print(end)    