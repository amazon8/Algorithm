num = int(input())
method = [0 for i in range(num+1)]
method[1] = 1
if num >= 2:
  method[2] = 3

# num까지 방법 채우기
for i in range(3, num+1):
  method[i] = method[i-1] + 2*method[i-2]

print(method[num]%10007)