width = int(input())
method = [0 for i in range(width+1)]
method[1] = 1
if width >= 2:
  method[2] = 2

# 방법 1부터 width 까지 저장
for i in range(3, width+1):
  method[i] = method[i-1] + method[i-2]

print(method[width]%10007)