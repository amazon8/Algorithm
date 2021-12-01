'''
1. 계속 시간 초과 뜸 ....
--> replace 함수는 O(n)의 시간 복잡도를 가짐
♨ 스택을 통해서 품 
'''
import sys

str = sys.stdin.readline()
str = list(str.strip())
result=[]

# ppap 문자열 p로 바꿈
for i in range(len(str)):
  if len(result) >= 2 and i <= len(str)-2 and str[i] == "A" and result[-2] == "P" and result[-1] == "P" and str[i+1] == "P":
    del result[-2:]
  else:
    result.append(str[i])

if ''.join(result) == 'P':
  print('PPAP')
else:
  print("NP")