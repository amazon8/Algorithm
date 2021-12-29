now_lan, need_lan = map(int, input().split())
lan = []
for i in range(now_lan):
  lan.append(int(input()))
lan.sort()
start = 1; end = lan[-1]; mid = 0; 


# 0부터 max길이 까지 나오는 랜선 길이 비교 --> 최대 길이 찾기
while start <= end :
  mid = (start+end)//2
  nums = 0
  for now_length in lan:
    nums += now_length // mid
  
  print("nums:{}, need_lan:{}, mid:{}, start:{}, end:{}".format(nums, need_lan, mid, start, end))
  if nums >= need_lan:
    start = mid+1
  else:
    end = mid-1

print(end)