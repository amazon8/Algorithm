book, num = map(int, input().split())
place = sorted(list(map(int,input().split())))
now = 0; sum =0
M = max(place)

# 양수 거리 더해줌
while place and place[-1] >= 0:
  if now == 0:
    sum += place[-1]*2
    place.pop()
  else:
    place.pop()
  now+=1
  if now == num:
    now = 0

# 음수 거리 더해줌
place = sorted(list(map(abs, place)))
if place:
  M = max(M, max(place))
now = 0
while place:
  if now == 0:
    sum += place[-1]*2
    place.pop()
  else:
    place.pop()
  now+=1
  if now == num:
    now = 0

print(sum-M)