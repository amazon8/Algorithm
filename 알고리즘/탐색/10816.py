have_num = int(input())
have_temp = list(map(int, input().split()))

check_num = int(input())
check_card = list(map(int, input().split()))

have_card = [0 for i in range(500000)]

# 가지고 있는 카드 개수 정리
for now_card in have_temp:
  have_card[now_card] += 1

# 개수 출력  
for now_card in check_card:
  print(have_card[now_card], end=' ')