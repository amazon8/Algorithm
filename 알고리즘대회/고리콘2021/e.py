testcase_num = int(input())


for i in range(testcase_num):
  final_sum, length = map(int, input().split())
  final_sum = final_sum - 1
  direction = "R"
  spot = 0
  sums = 0
  now_length = length

  # 최종 거리합 만큼 가기
  while True:
    if final_sum == sums:
      break    
    if final_sum < sums + now_length:
      if direction == "R":
        spot = spot + (final_sum - sums)
      elif direction == "L":
        spot = spot - (final_sum - sums)
      break  

    if direction =="R":
      spot += now_length
      sums += now_length
      direction = "L"
      now_length += length
    elif direction =='L':
      spot -= now_length
      sums += now_length 
      direction = "R"
      now_length += length

  print(spot, direction)