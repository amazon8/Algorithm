'''
♨ 그리디 문제에서 정당성을 어떻게 확인하는게 맞는가...? 테스트 케이스를 우리가 만들기에 복잡한 경우......
'''
num = int(input())
rank = list(map(int, input().split()))
pop_1 = 0; pop_2 = 0
result = 0

# 차가 가장 작은 값 부터 없애기
while len(rank) > 1:
  min_dif = abs(rank[1] - rank[0])
  for c in range(len(rank)-1):
    if abs(rank[c] - rank[c+1]) < min_dif:
      pop_1 = rank[c]
      pop_2 = rank[c+1]
      min_dif = abs(pop_1 - pop_2)    
  result += min_dif
  rank.remove(max(pop_1, pop_2))

print(result)