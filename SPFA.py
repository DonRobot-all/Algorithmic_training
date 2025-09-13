from collections import deque

def bellman_ford_queue(graph, start):
    # Инициализация расстояний
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    # Инициализация очереди и множества для отслеживания вершин в очереди
    queue = deque([start])
    in_queue = {v: False for v in graph}
    in_queue[start] = True

    # Счётчик обновлений для обнаружения отрицательного цикла
    count = {v: 0 for v in graph}

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    count[v] += 1
                    # Проверка на отрицательный цикл
                    if count[v] > len(graph):
                        print("Граф содержит отрицательный цикл!")
                        return None

    return dist

# Пример графа с отрицательными весами
# graph = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('C', -1), ('D', 5)],
#     'C': [('B', -2), ('D', 3), ('E', 2)], 
#     'D': [('E', -3)],
#     'E': [('A', 3)]
# }
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('B', -3)],  # Ключевое отрицательное ребро!
    'D': [('E', 1)],
    'E': []
}


start_vertex = 'A'
distances = bellman_ford_queue(graph, start_vertex)
print(distances)
# Вывод результатов
for vertex, d in distances.items():
    print(f"Расстояние от {start_vertex} до {vertex} = {d}")
