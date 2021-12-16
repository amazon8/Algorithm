'''
♨ 함수 입력값이  여러개인 알고리즘을 생각을 못함
재귀의 경우 어떤 값이 들어오고, 무엇이 반환되는지 명확히 파악해야함
'''

num = int(input())
count = [0 for i in range(21)]
count[1] = 1

# 하노이 재귀 n개를 a-->c 로 이동
def h(n, a, b, c):
  if n==1:
    print(a, c)
  else:
    h(n-1, a, c, b)
    print(a, c)
    h(n-1, b, a, c)

for i in range(2, num+1):
  count[i] = count[i-1]*2+1
print(count[num])
h(num, 1, 2, 3)