import sys
sys.setrecursionlimit(1000020)

num = int(input())
nums = [1000000 for i in range(num+1)]
nums[1] = 0

# 최소값 찾기
def mins(now):
  result = int
  if nums[now]!=1000000:
    return nums[now]
  else:
    nums[now] = min(mins(now-1)+1, nums[now])
    if int(now/2) == now/2:
      nums[now] = min(nums[now], mins(now//2)+1)
    if int(now/3) == now/3:
      nums[now] = min(nums[now], mins(now//3)+1)
    return nums[now]
    
print(mins(num))
