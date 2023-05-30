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

visited = dfs(graph1,'A', [])
print("Ans :")
print(visited)
