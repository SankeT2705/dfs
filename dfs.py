from queue import Queue
graph1 = {
    0:[1,2,3],
    1:[0,4],
    2:[0,3,5],
    3:[0,2,7,6],
    4:[1],
    5:[2],
    6:[3],
    7:[3]
}
print("The adjacency List representing the graph is:")
print(graph1)

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited

visited = dfs(graph1,0, [])
print("DFS:")
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
print("BFS :")
bfs(graph1,0)
print("\n")
    
