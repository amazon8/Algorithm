'''
1. 왜 틀렸는지 모르겠네,,,,
  --> 경계가 되는 부분에서 예외가 발생하는지 확인!!
'''
final_channel = int(input())
broken_num = int(input())
if broken_num != 0:
  broken = list(map(int, input().split()))
else:
  broken = []
if final_channel == 100:
  print(0)
  exit()
if broken_num == 10:
  print(abs(final_channel-100))
  exit()

channel = 0
optimal_channel = 10000001

def possible_channel(channels):
  global broken
  list_channel = list(map(int, str(channels)))
  for index in range(len(list_channel)):
    if list_channel[index] in broken:
      return False
  return channels

# 채널값의 차이가 최소인 값 찾기
while channel <= 1000000:
  res_channel = possible_channel(channel)
  if res_channel != False and abs(optimal_channel-final_channel)+len(str(optimal_channel))>abs(res_channel-final_channel)+len(str(res_channel)):
    optimal_channel = res_channel
  channel += 1  

print(min((abs(optimal_channel-final_channel)+len(str(optimal_channel))), abs(final_channel-100)))