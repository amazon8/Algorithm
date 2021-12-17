'''
1. 병합정렬 --> 모든 경우 비교x, 개수가 홀수인 경우 비교 불가
'''
num = int(input())
location = []
for i in range(num):
  row = list(map(int, input().split()))
  location.append(row)

# 병합정렬 방식 중 분할
def split(location):
  print(location)
  mid = int
  if len(location) == 2:
    return location
  mid = len(location) // 2
  left = location[:mid]
  right = location[mid:]
  split(left)
  split(right)
  return merge(left, right)

# 병합
def merge(left, right):
  if abs(left[0][0]-left[1][0])+abs(left[0][1]-left[1][1]) >= abs(right[0][0]-right[1][0])+abs(right[0][1]-right[1][1]):
    print("오른쪽 : {}".format(right))
    return right
  else:
    pritn("왼쪼 :{}".foramt(left))
    return left

result = split(location)
dis = abs(result[0][0]-result[1][0])**2+abs(result[0][1]-result[1][1])**2
print(dis)