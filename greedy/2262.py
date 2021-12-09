num = int(input())
rank = list(map(int, input().split()))
pop_1 = 0; pop_2 = 0
result = 0

# 차가 가장 작은 값 부터 없애기
while len(rank) > 1:
  min_dif = abs(rank[1] - rank[0])
  pop_1 = rank[1]
  pop_2 = rank[0]
  for c in range(len(rank)-1):
      if abs(rank[c] - rank[c+1]) < min_dif:
        pop_1 = rank[c]
        pop_2 = rank[c+1]
        min_dif = abs(pop_1 - pop_2)
      elif abs(rank[c] - rank[c+1]) == min_dif:
        if max(pop_1, pop_2) <= max(rank[c], rank[c+1]):
          pop_1 = rank[c]
          pop_2 = rank[c+1]
          min_dif = abs(pop_1 - pop_2)
  result += abs(pop_1-pop_2)
  rank.remove(max(pop_1, pop_2))

print(result)