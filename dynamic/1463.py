num = int(input())
divs = [2, 3]
nums = [33334 for i in range(num+1)]
nums[1] = 0

# 숫자를 최소값으로 갱신
for now in range(2, num+1):
  if int(now/2) == now/2:
    nums[now] = min(nums[now], nums[now//2]+1)
  if int(now/3) == now/3:
    nums[now] = min(nums[now], nums[now//3]+1)
  nums[now] = min(nums[now], nums[now-1]+1)

print(nums[num])