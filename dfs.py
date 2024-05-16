
def dfs(node, depth=0):
    if node not in visited:
        print(node, depth)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, depth + 1)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()


# Начинаем обход графа с вершины 'A'
dfs('A') 