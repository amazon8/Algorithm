'''
1. 분할정복(시간 복잡도 때문에 복사, num을 k로 임의 수정)
--> 식이 너무 복잡함,,,,,
2. 모두 분할정복, k대신 num 자체로 진행
♨ 1. 분할정복 알고리즘에 있어 복사를 할지, 모두 호출 할지는 시간복잡도와 상황에 맞게 판단하기!!
2. 함수에서 인자를 어떤것으로 할지 상황에 맞게 정하기
'''
num = int(input())
array = [[" " for col in range(num*2+1)]for row in range(num+1)]

# 별찍기 - 3개로 분할
def star_print(num, row, col):
  if num ==3:
    array[row][col] = "*"
    array[row+1][col-1] = "*"; array[row+1][col+1] = "*"
    array[row+2][col-2] = "*"; array[row+2][col-1] = "*"; array[row+2][col] = "*"; array[row+2][col+1] = "*"; array[row+2][col+2] = "*"
    return
  next_num = num // 2
  star_print(next_num, row, col)
  star_print(next_num, row+num//2, col-num//2)
  star_print(next_num, row+num//2, col+num//2) 

star_print(num, 1, num)
for row in range(1, num+1):
  print("".join(array[row][1:-1]))