num = int(input())
count = [0 for i in range(num+1)]
count[1] = 9
if num>=2:
  count[2] = 17

# num까지 개수 채워가기
for now in range(3, num+1):
  count[now] = (count[now-1]-2)*2+2

print(count[num]%1000000000)

2개만 빠지는 게 아니라 더 많이 빠짐