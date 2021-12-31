'''
1. 이진탐색으로 탐색 해야 할 것이 차이임을 인식하지 못함,,,
♨ 이진 탐색에서 stat, end가 무엇을 의미하는지 정확히 파악!!
'''
home_num, wifi_num = map(int, input().split())
spot = []
for i in range(home_num):
  spot.append(int(input()))
spot.sort()
start = 1
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