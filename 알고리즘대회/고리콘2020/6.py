num = int(input())
quality = sorted(list(map(int, input().split())))
benefit = 0

# 2개를 묶음으로 만들기
if len(quality) == 1:
  print(quality[-1])
  exit()

while quality: 
  if len(quality) == 1:
    benefit += quality[-1]
    break
  benefit += quality[-1] * 2
  quality.pop()
  quality.pop(0)

print(benefit)