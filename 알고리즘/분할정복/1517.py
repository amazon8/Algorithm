num = int(input())
array = list(map(int, input().split()))
swap_c = 0

# 병합정렬로 swap 카운트
def merge_sort(start, end):
  global swap_c
  temp = []
  if start == end:
    return
  mid = (start+end)//2
  left = merge_sort(start, mid)
  right = merge_sort(mid+1, end)
  
  left_index = 0; right_index = 0
  while left_index < mid and right_index < end:
    if array[mid+right_index] < array[start+left_index]:
      swap_c += mid-left_index
      print(start, end, array, left_index, right_index, swap_c)
      temp.append(array[mid+right_index])
      right_index += 1
    else:
      temp.append(array[start+left_index])
      left_index += 1

  if left_index == mid:
    temp.extend(array[right_index:end+1])
  else:
    temp.extend(array[left_index:mid])

  for index in range(len(temp)):
    array[start+index] = temp[index]

merge_sort(0, num-1)
print(swap_c)