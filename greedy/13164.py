person_n, gruop_n = map(int, input().split())
height = list(map(int, input().split()))

# 키 차이 리스트
dif = [height[i+1]-height[i] for i in range(person_n-1)]
dif.sort()

# 그룹 개수로 나누기
for i in range(gruop_n-1):
  dif.pop()

print(sum(dif))