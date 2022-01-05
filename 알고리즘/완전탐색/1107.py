final_channel = int(input())
a = input()
broken = list(map(int, input().split()))
channel = 0
optimal_channel = 0

# 버튼 9999까지 확인
while channel <= 9999:

  int_channel = channel
  list_channel = list(map(int, str(channel)))
  for index in range(len(list_channel)):
    if list_channel[index] in broken:
      break
    else:
      if index == len(list_channel)-1 and abs(optimal_channel - final_channel) > abs(int_channel-final_channel):
        optimal_channel = int_channel

  channel += 1


shift = abs(final_channel-optimal_channel)
final_channel = list((str(final_channel)))
shift += len(final_channel)

print(shift)

