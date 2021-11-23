'''
시작 : 07:55

'''

n = int(input())

# 악수 가능한 경우 - 인접한 경우
if n==1:
  print(0)
else: 
  a = 2**(n-1) - (n-2)*(n-1)//2
  print(int(a)%10)