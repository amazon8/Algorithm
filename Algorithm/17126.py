import math

n = int(input())
m = math.floor(math.sqrt(n))
a = [50001 for i in range(n+1)]
a[1] = 1

# n까지 제곲들의 합 최소 개수로 나타내기
for i in range(1, m+1):
  for j in range(1, n+1):
    if math.sqrt(j)%1 ==0:
      a[j] = 1
    else:
      a[j] = min(a[j], a[j-i**2]+1)


print(a[n])