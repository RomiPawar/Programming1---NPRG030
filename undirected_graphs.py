def dfs(graph, vertex, visited, component):
        visited[vertex] = True
        component.append(vertex)

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                dfs(graph, neighbour, visited, component)
    
def connected_components(graph, vertices):
        visited = [False] * (vertices + 1)
        components = []
        for vertex in range(1, vertices+1):
            if not visited[vertex]:
                component =[]
                dfs(graph, vertex, visited, component)
                components.append(component)
        return components
    
vertices = int(input())
edges = int(input())
graph = {i: [] for i in range(1, vertices + 1)}

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

components = connected_components(graph, vertices)
for component in components:
    print(" ".join(map(str, component)))
