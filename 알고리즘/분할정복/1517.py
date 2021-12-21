'''
1. 버블정렬 풀이
  recursion error가 표시됨,,, 재귀오류가 왜 일어나는 걸까,,?
--> 시간복잡도가 1초보다 훨씬 초과 됨, 대략적으로는 시간을 측정하고 알고리즘 방향을 결정해야 할듯
2. 병합 정렬 알고리즘 --> 메모리 초과,, 흠,,
3. 병합 정렬에서 리턴 값 없앤 풀이!
4. 참조 : https://jokerldg.github.io/algorithm/2021/09/12/bubble-sort.html
'''
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