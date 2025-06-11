class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isBipartite(self):
        colorArr = [-1] * self.V
        queue = []

        for i in range(self.V):
            if colorArr[i] == -1:
                queue.append(i)
                colorArr[i] = 1

                #bfs
                while queue:
                    u = queue.pop(0)

                    for v in self.graph[u]:
                        if colorArr[v] == -1:
                            colorArr[v] = 1 - colorArr[u]
                            queue.append(v)
                        elif colorArr[v] == colorArr[u]:
                            return None  #not bipartite

        group1 = [i + 1 for i, color in enumerate(colorArr) if color == 1]
        group2 = [i + 1 for i, color in enumerate(colorArr) if color == 0]

        return group1, group2

N = int(input())
M = int(input())

g = Graph(N)

for _ in range(M):
    u, v = map(int, input().split())
    g.addEdge(u - 1, v - 1)

#checking for bipartite graph
result = g.isBipartite()

#for o/p
if result is None:
    print("Nelze")
else:
    group1, group2 = result
    print(" ".join(map(str, group1)))
    print(" ".join(map(str, group2)))
