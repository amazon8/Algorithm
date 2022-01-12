end_node, edge_num = map(int, input().split())
graph = [[]for i in range(end_node+1)]

for i in range(edge_num):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

# dfs함수
def dfs(graph, end_node):
  visit = set()
  stack = set()
  num = 0
  for now_node in range(1, end_node+1):
    stack.add(now_node)
    if now_node not in visit:
      while stack:
        node = stack.pop()
        if node not in visit:
          visit.add(node)
          stack.update(set(graph[node])-visit)
      num += 1

  return num
    
res = dfs(graph, end_node)
print(res)