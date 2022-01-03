num = int(input())
result = 1

# 팩토리얼
for now in range(1, num+1):
  result *= now

print(result)