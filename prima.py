# import heapq
# from typing import List, Tuple

# def prim_mst(graph: List[List[Tuple[int, int]]], n: int) -> Tuple[List[int], List[int]]:
#     """
#     Алгоритм Прима с min-heap. graph[i] = [(сосед, вес), ...]
#     Возвращает (parent, key) для MST
#     """
#     INF = float('inf')
#     key = [INF] * n
#     parent = [-1] * n
#     visited = [False] * n
#     pq = [(0, 0)]  # (key, vertex)
    
#     key[0] = 0
    
#     while pq:
#         _, u = heapq.heappop(pq)
#         if visited[u]:
#             continue
            
#         visited[u] = True
        
#         for v, weight in graph[u]:
#             if not visited[v] and weight < key[v]:
#                 key[v] = weight
#                 parent[v] = u
#                 heapq.heappush(pq, (key[v], v))
    
#     return parent, key

# # Пример использования
# def example():
#     # Граф: 4 вершины, ребра [(0,1,10), (0,2,6), (1,2,5), (1,3,15), (2,3,4)]
#     n = 4
#     graph = [
#         [(1, 10), (2, 6)],      # вершина 0
#         [(0, 10), (2, 5), (3, 15)],  # вершина 1
#         [(0, 6), (1, 5), (3, 4)],    # вершина 2
#         [(1, 15), (2, 4)]     # вершина 3
#     ]
    
#     parent, key = prim_mst(graph, n)
#     print("Parent:", parent)  # [0, 2, 0, 2]
#     print("Key:", key)        # [0, 5, 6, 4]
#     print("Общий вес MST:", sum(k for k in key if k != float('inf')))

# if __name__ == "__main__":
#     example()

# import networkx as nx
# import matplotlib.pyplot as plt

# # Создаем граф из списка смежности
# graph = [
#     [(1, 10), (2, 6)],      # вершина 0
#     [(0, 10), (2, 5), (3, 15)],  # вершина 1
#     [(0, 6), (1, 5), (3, 4)],    # вершина 2
#     [(1, 15), (2, 4)]     # вершина 3
# ]

# G = nx.Graph()
# n = len(graph)

# # Добавляем ребра с весами
# for u in range(n):
#     for v, weight in graph[u]:
#         if u < v:  # избегаем дублирования
#             G.add_edge(u, v, weight=weight)

# # Настройка позиций (круговое расположение)
# pos = nx.spring_layout(G, seed=42)  # фиксированный seed для воспроизводимости

# plt.figure(figsize=(10, 8))

# # Рисуем ребра
# nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color='gray')

# # Рисуем узлы
# nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
#                       node_size=800, alpha=0.9)

# # Метки узлов
# nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

# # Метки весов на ребрах
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, 
#                            font_size=12, font_color='red')

# plt.title("Граф для алгоритма Прима (4 вершины)", fontsize=16, pad=20)
# plt.axis('off')
# plt.tight_layout()
# plt.show()
