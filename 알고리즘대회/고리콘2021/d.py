input()
num = list(map(int, input().split()))
count = [0 for i in range(25)]

# 자리별 1의 개수 확인
for now_num in num:
  temp = now_num
  n = 0
  while temp > 0:
    count[n] += temp % 2
    n += 1
    temp = temp // 2

print(max(count))