'''
1. 버블정렬 풀이
  recursion error가 표시됨,,, 재귀오류가 왜 일어나는 걸까,,?
--> 시간복잡도가 1초보다 훨씬 초과 됨, 대략적으로는 시간을 측정하고 알고리즘 방향을 결정해야 할듯
2. 병합 정렬 알고리즘 --> 메모리 초과,, 흠,,
'''

num = int(input())
arr = list(map(int, input().split()))
left = []
right = []
swap_c = 0; mid = 0
final_array = []

# 분할 함수
def split(array):
  if len(array) ==1:
    return array
  mid = len(array)//2
  left = split(array[:mid])
  right = split(array[mid:])
  return merge(left, right)

# 병합 함수
def merge(left, right):
  global swap_c
  final_array = []
  left_index = 0; right_index = 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] > right[right_index]:
      swap_c += 1
      final_array.append(right[right_index])
      right_index += 1
    else:
      final_array.append(left[left_index])
      left_index += 1

  if right_index == len(right):    
    final_array.extend(left)
  else: 
    final_array.extend(right)

  return final_array

result = split(arr)
print(swap_c)