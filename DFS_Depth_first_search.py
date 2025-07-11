def dfs_tree(tree, start):
    stack = [start]

    while stack:
        node = stack.pop()
        print(node)
        # Добавляем детей в стек (обратный порядок для правильного порядка обхода)
        stack.extend(reversed(tree.get(node, [])))

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

dfs_tree(tree, 'A')

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def dfs_recursive(graph, node):
    print(node)

    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor)

dfs_recursive(graph, 'A')
