num = int(input())
str = [0 for i in range(num)]
for i in range(num):
  str[i] = input()

# 가로 세로 비교
for now in range(num):
  if str[0][now] != str[now][0] or str[num-1][now] != str[now][num-1]:
    print("NO")
    exit()

print("YES")
