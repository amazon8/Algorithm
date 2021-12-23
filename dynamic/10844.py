'''
♨ dp에서는 반복되는 부분이 무엇인지 정확히 파악하기
'''

length = int(input())
num = [[0 for col in range(10)]for row in range(102)]
num[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# 끝에 따라 개수 채워가기
for now_length in range(2, length+1):
  for now_end in range(10):
    if now_end == 0:
      num[now_length][now_end] = num[now_length-1][1]
    elif now_end ==9:
      num[now_length][now_end] = num[now_length-1][8]
    else:
      num[now_length][now_end] = num[now_length-1][now_end-1]+num[now_length-1][now_end+1]


print(sum(num[length])%1000000000)