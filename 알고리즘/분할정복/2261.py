'''
1. 병합정렬 --> 모든 경우 비교x, 개수가 홀수인 경우 비교 불가
2. 버블정렬로 가능 할 거 같은데,, --> 모든 경우 비교x 
ex) [1,-2] [2,9] [3,11] [4,1]
3. 분할정복, 스위핑을 써야할듯,,,,
'''
num = int(input())
location = []
for i in range(num):
  row = list(map(int, input().split()))
  location.append(row)

location.sort()
dif_x = abs(location[0][0]-location[1][0])
dif_y = abs(location[0][1]-location[1][1])
print(dif_x, dif_y)


# 버블정렬 방식
for now in range(1, num-1):
  if dif_x + dif_y > abs(location[now][0]-location[now+1][0])+abs(location[now][1]-location[now+1][1]):
    dif_x = abs(location[now][0]-location[now+1][0])
    dif_y = abs(location[now][1]-location[now+1][1])


print(dif_x**2+dif_y**2)