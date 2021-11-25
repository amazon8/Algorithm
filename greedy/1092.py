'''
※ 그냥 작은 것 부터 박스 --> 크레인 넣음
  ☞ 마지막 남은 박스가 크레인 보다 큰 경우 횟수가 추가됨
※ 큰 것 부터 박스 --> 크레인 넣음
  ☞ 왜 안돌아가는지 모르겠음....
♨ 그리디 알고리즘 풀이 방향을 어떻게 가져가야 될지 모르겠음..
뭔가 모든 경우를 다 검사하면서 그 순간 최선의 선택을 하는 코드는 되게 지저분하고 복잡한 느낌,,,,
→ 그리디 문제는 정당성(!!)을 확보하면 그냥 그렇게 하나씩 확인하면서 푸는 방식이 맞는듯! ... 풀이보니 다 지저분함
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
