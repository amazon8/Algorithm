num, tree_final = map(int, input().split())
tree = sorted(list(map(int, input().split())))
start = 1; end = tree[-1]; mid = 0;

# 0부터 max 길이까지 이분 탐색
while start <= end:
  mid = (start + end) // 2
  tree_sum = 0
  for now_tree in tree:
    if now_tree > mid:
      tree_sum += now_tree - mid
  
  if tree_final <= tree_sum:
    start = mid+1
  else:
    end = mid-1
    
print(end)