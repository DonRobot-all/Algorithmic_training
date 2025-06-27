from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        print(current, path)
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)
        for point in graph[current]:
            if point not in visited:
                queue.append((point, path + [point]))


graph = { 'A': ['B', 'C'],    'B': ['D'],    'C': ['E'],    'D': ['F'],    'E': ['F'],    'F': []}
result = bfs_shortest_path(graph, 'A', 'F')
print(result)  # ['A', 'B', 'D', 'F']