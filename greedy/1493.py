'''
1. 박스에서 큐브 만큼 뺀 후의 모양에 대한 식을 못 찾겠음...
--> 다른 알고리즘으로 풀어야 할 듯!!
'''

import math

length, wid, hei = map(int, input().split())
num = int(input())
cube = [[0 for col in range(2)] for row in range(num)]
for i in range(num):
  cube[i][0], cube[i][1] = map(int, input().split())
count = 0

# 큐브 부피만큼 빼는 과정
vol = length*wid*hei
for i in reversed(range(num)):
  cube_side = 2**cube[i][0]
  cube_vol = math.pow(cube_side, 3)
  if cube_side <= min(length, wid, hei):
    if vol // cube_vol <= cube[i][1]:
      count += int(vol //cube_vol) 
      vol = vol % cube_vol 
    else:
      vol = vol - (cube_vol*cube[i][1])
      count += cube[i][1]
  if vol == 0:
    break

if vol ==0 :
  print(count)
else:
  print(-1)    