num = int(input())
vote = list(map(int, input().split()))
nums = [0 for i in range(num+1)]

# 투표자 개수 파악
for i in vote:
  nums[i] += 1

M = int
M = max(nums[1:])
if nums.count(M) >= 2:
  print("skipped")
else:
  print(nums.index(M))  