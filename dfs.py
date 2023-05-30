from queue import Queue
graph1 = {
    1:[2,3],
    2:[1],
    3:[1,4,5],
    4:[3],
    5:[3] 
}
print("The adjacency List representing the graph is:")
print(graph1)

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited

visited = dfs(graph1,1, [])
print("Ans :")
print(visited)
print("\n")

def bfs(graph,source):
    Q=Queue()
    visited=set()
    Q.put(source)
    visited.update({0})

    while not Q.empty():
        vertex=Q.get()
        print(vertex,end="--->")
        for u in graph[vertex]:
            if u not in visited:
                Q.put(u)
                visited.update({u})
bfs(graph1,1)
print("\n")
    
