import heapq

# heap = [('A', 0)]

# while heap:
#     heap.heappush

# import heapq
# heap = []
# heapq.heappush(heap, ('A', 3))
# heapq.heappush(heap, ('B', 5))
# heapq.heappush(heap, ('A', 3))
# print(heap)  # [1, 3, 5]
# min_item = heapq.heappop(heap)
# print(min_item)  # 1

import heapq

def dijkstra(graph, start):
    # Инициализируем словарь расстояний: бесконечность для всех, кроме старта
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # Очередь с приоритетом — содержит пары (расстояние, узел)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Если мы уже нашли путь короче — пропускаем
        if current_dist > dist[current_node]:
            continue

        # Обходим всех соседей текущего узла
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            # Если нашли более короткий путь — обновляем и добавляем в очередь
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return dist

# Пример графа
graph = {    
    'A': [('B', 1), ('C', 4)],    
    'B': [('C', 2), ('D', 5)],    
    'C': [('D', 1)],    
    'D': []
}

# Вызов алгоритма
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)
