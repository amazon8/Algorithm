num = int(input())
vote = list(map(int, input().split()))
nums = [0 for i in range(num+1)]

# 투표자 개수 파악
for i in vote:
  nums[i] += 1

M = int
M = max(nums[1:])

# 모두 기권인 경우
if sum(nums[1:]) == 0:
  print("skipped")
  exit()
else:
  nums.pop(0)

# 최다 득표자에 따른 결과 출력 
if nums.count(M) >= 2:
  print("skipped")
else:
  print(nums.index(M)+1)