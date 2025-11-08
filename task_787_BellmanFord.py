# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         dists = [float('inf') for _ in range(n)]
#         dists[src] = 0

#         for _ in range(k+1):
#             nxt = dists.copy()
#             for i in range(len(flights)):
#                 u, v, w = flights[i]
#                 if dists[u] + w < nxt[v]:
#                     nxt[v] = dists[u] + w
#             dists = nxt
#         return dists[dst] if dists[dst] != float('inf') else -1


from collections import deque
from math import inf

def bellman_ford(graph, start):
    """
    Реализация алгоритма Беллмана–Форда с использованием очереди.
    
    graph — словарь вида:
        {
            'A': [('B', 4), ('C', 2)],
            'B': [('C', -3), ('D', 2)],
            ...
        }
    start — стартовая вершина
    """
    # Инициализация
    dist = {v: inf for v in graph}
    dist[start] = 0
    
    in_queue = {v: False for v in graph}
    count = {v: 0 for v in graph}
    
    queue = deque([start])
    in_queue[start] = True
    
    num_vertices = len(graph)
    
    # Основной цикл
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
                    if count[v] > num_vertices:
                        print("Обнаружен отрицательный цикл!")
                        return None
    
    return dist


# Пример использования:
if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', -3), ('D', 2)],
        'C': [('D', 3)],
        'D': []
    }
    
    result = bellman_ford(graph, 'A')
    
    if result:
        print("Кратчайшие расстояния от вершины A:")
        for v, d in result.items():
            print(f"{v}: {d}")
