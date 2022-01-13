'''
1. bfs보다는 dp문제 같은데,,,, 
  --> bfs로 풀 수는 있는데 dp로 푸는게 나을 듯
'''

subin, brother = map(int, input().split())
spot = [abs(subin-i) for i in range(brother+3)]

# 수빈부터 동생있는 곳까지 dp
for now in range(subin+1, brother+2):
  spot[now] = min(spot[now-1]+1, spot[now+1]+1)
  if now % 2 == 0 :
    spot[now] = min(spot[now], spot[now//2]+1)
    spot[now-1] = min(spot[now-1], spot[now]+1)

print(spot[brother])