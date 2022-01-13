'''
1. bfs보다는 dp문제 같은데,,,,
'''

subin, brother = map(int, input().split())
spot = [ i for i in range(brother+2)]
print(spot)
for index in range(subin+1):
  spot[index] = 0
print(spot)

# 수빈부터 동생있는 곳까지 dp
for now in range(subin+1, brother+1):
  spot[now] = min(spot[now-1]+1, spot[now+1]-1)
  if now % 2 == 0 and now >= subin*2:
    spot[now] = min(spot[now], spot[now//2]+1)

print(spot)
print(spot[brother])