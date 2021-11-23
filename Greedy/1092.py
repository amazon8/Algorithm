'''
※ 그냥 작은 것 부터 박스 --> 크레인 넣음
  ☞ 마지막 남은 박스가 크레인 보다 큰 경우 횟수가 추가됨
※ 큰 것 부터 박스 --> 크레인 넣음
  ☞ 왜 안돌아가는지 모르겠음....
'''

n = int(input())
c = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
c.sort(reverse = True); box.sort(reverse = True)
i= 0 ; j = 0 ; time = 0 ; k=0

# 박스가 크레인 보다 큰 경우 판별
if max(box) > max(c):
  print(-1)
  exit()

while True:
  k = i
  while True:
    if box[i]!=0:
      if j ==n-1:
        time+=1; j=0
      if c[j] >= box[i]:
        j+=1; box[k] =0;
        if i==k:
          i+=1 
        break
      else:
        k+=1
  if i == m:
    print(time)
    exit()
