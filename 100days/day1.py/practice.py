from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node)
    visited.add(node)
    for nei in graph[node]:
        dfs(nei)
dfs('A')


visited1 = set()
def bfs(start):
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited1:
            print(vertex)
            visited.add(vertex)
            queue.extend(nei for nei in graph[vertex] if nei not in visited)
bfs('A')