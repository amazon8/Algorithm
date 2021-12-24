length = int(input())
array = [[0 for col in range(10)]for row in range(1001)]
array[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 끝에 맞혀서 개수 추가해가기
for now_line in range(2, length+1):
  for now_end in range(10):
    for plus_index in range(now_end+1):
      array[now_line][now_end] += array[now_line-1][plus_index]

print(sum(array[length])%10007)