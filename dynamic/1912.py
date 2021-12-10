'''
1. array를 전, 전+지금, 지금 세개 비교 후 max 넣기
  --> 앞뒤로는 작은데 전제가 큰 경우가 발생
2. array를 전, 전+지금, 지금 비교 --> 지금이 max가 아니면 전+지금 값을 array에 넣기
'''
num = int(input())
array = list(map(int, input().split()))

# 연속된 합의 최대로 채워가기
for now in range(1, len(array)):
  M = max(array[now-1], array[now-1]+array[now], array[now])
  if M == (array[now-1]+array[now]) or M == array[now-1]:
    array[now] = array[now-1] + array[now]

print(max(array))