'''
# 해당 문제의 풀이들과 같은 O(n*3/2)이 걸리지만 해당 코드 제출시 시간 초과 출력됨...
시작 : 11:25
'''

import math, time

start = time.time()
n = int(input())
m = math.floor(math.sqrt(n))
a = [50001 for i in range(n+1)]
a[1] = 1

# n까지 제곱들의 합 최소 개수로 나타내기
for i in range(1, m+1):
  for j in range(1, n+1):
    if math.sqrt(j)%1 ==0:
      a[j] = 1
    elif (j-i**2)>0:
      a[j] = min(a[j], a[j-i**2]+1)

print(a[n])
end = time.time()
print("{:.5f} sec".format(end-start))
