# from collections import deque
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# visited = set()
#
# def bfs(start):
#     queue = deque([start])
#     while queue:
#         vertex = queue.popleft()
#         if vertex not in visited:
#             print(vertex)
#             visited.add(vertex)
#             queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
#
# bfs('A')  # Output: A B C D E F
#

s = "3aba"
print(s[0])
