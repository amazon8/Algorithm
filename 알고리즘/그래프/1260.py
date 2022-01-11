from collections import deque

vertex_num, edge_num, start_node = map(int, input().split())

# 그래프 딕셔너리 만들기
graph = [[] for i in range(vertex_num+1)]
for i in range(edge_num):
  key_1, key_2 = map(int, input().split())
  graph[key_1].append(key_2)
  graph[key_2].append(key_1)
  graph[key_1].sort(reverse = True)
  graph[key_2].sort(reverse = True)

def dfs(graph, start_node):

  stack = list()
  visit = set()

  stack.append(start_node)

  while stack:
    node = stack.pop()
    while node not in visit:
      visit.add(node)
      stack.append(graph[node])

  return visit

def bfs(graph, start_node):

  stack = deque()
  visit = set()

  stack.append(start_node)

  while stack:
    node = stack.leftpop()
    if node not in visit:
      visit.add(node)
      stack.extend(graph[node])

  return visit



dfs_res = dfs(graph, start_node)
for row in range(len(graph)):
  graph[row].sort()
bfs_res = bfs(graph, start_node)

for index in range(len(dfs_res)):
  print(dfs_res[index], end = ' ')
print()
for index in range(len(bfs_res)):
  print(bfs_res[index], end = ' ')  
