length, wid, hei = map(int, input().split())
num = int(input())
cube = [[0 for col in range(2)] for row in range(num)]
for i in range(num):
  a[i][0], a[i][1] = map(int, input().split())

# 큐브 부피만큼 빼는 과정
vol = length*wid*hei
for i in reversed(range(num)):
  cube_side = 2**cube[i][0]
  if cube_side <= max(length, wid, hei):
    if vol // cube_side*cube_side*cube_side <= cube[i][1]:
      vol = vol % (2**cube[i][0])  