str = list(input())
result=[]
i=0

# 스택으로 ppap제거
while True:
  if i<=len(str)-4 and str[i]=="P" and str[i+1]=="P" and str[i+2]=="A" and str[i+3]=="P":
    result.append(str[i])
    i+=4
  else:
    result.append(str[i])
    i+=1
  if 'PPAP' in "".join(result):
    for j in range(3):
      result.pop()
  if i == len(str):
    break

print(result)
if ''.join(result)=='P':
  print('PPAP')
else:
  print('NP')