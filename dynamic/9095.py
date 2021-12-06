num = int(input())
test = []
for i in range(num):
  test.append(int(input()))
method = [0 for i in range(11)]


# n까지 방법 갯수 저장
for now in test:
  method[1] = 1
  if now >=2:
    method[2] = 2
  if now>=3:
    method[3] = 4
  if now>=4:
    method[4] = 7
  if method[now] != 0:
    print(method[now])
  else:
    for n in range(5, now+1):
      method[n] = method[n-1] + method[n-2] + method[n-3]
    print(method[now])