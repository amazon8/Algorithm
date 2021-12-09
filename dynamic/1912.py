num = int(input())
array = list(map(int, input().split()))

# 연속된 합의 최대로 채워가기
for now in range(1, len(array)-1):
  if max(array[now-1], array[now-1]+array[now], array[now]) == (array[now-1]+array[now]):
    array[now] = max(array[now-1], array[now-1]+array[now], array[now])
  else:
    array[now] = 0
  print(array)

print(max(array))