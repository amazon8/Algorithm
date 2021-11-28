import sys

str = sys.stdin.readline()
str = str.strip()

# ppap 있는 경우 p로 치환
while 'PPAP' in str:
  str = str.replace('PPAP', 'P')

if str == 'P':
  print("PPAP")
else:
  print("NP")
