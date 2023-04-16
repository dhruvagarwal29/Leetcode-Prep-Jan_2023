# algorithm for dfs 

# find all the nodes from the source 

# graph 
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : ['H'],
  'H' : []
}

visited = set() # using set to track visited nodes 

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    

dfs(visited, graph, 'A')

