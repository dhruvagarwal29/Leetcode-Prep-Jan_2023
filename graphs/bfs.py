# algorithm for bfs 

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
visited = []
queue = []

def bfs(graph, node, visited):

    visited.append(node)
    queue.append(node)

    while queue:
        source = queue.pop(0)
        print(source)
        for neighbour in graph[source]:
            if neighbour not in visited:

                visited.append(neighbour)
                queue.append(neighbour)


bfs(graph, 'A', visited)

