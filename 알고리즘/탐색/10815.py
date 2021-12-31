have_num = int(input())
have_card = sorted(list(map(int, input().split())))

check_num = int(input())
check_card = list(map(int, input().split()))

check = ['0' for i in range(check_num)]

# 이분탐색으로 카드가 존재하는지 확인
for now_card in range(check_num):
  start = 0; end = have_num-1
  while start <= end:
    mid = (start+end) // 2
    if have_card[mid] == check_card[now_card]:
      check[now_card] = '1'
      break
    if check_card[now_card] < have_card[mid]:
      end = mid-1
    else:
      start = mid+1

print(" ".join(check))