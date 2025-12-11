import heapq
from typing import List, Tuple

def prim_mst(graph: List[List[Tuple[int, int]]], n: int) -> Tuple[List[int], List[int]]:
    ...



n = 4
graph = [
    [(1, 10), (2, 6)],      # вершина 0
    [(0, 10), (2, 5), (3, 15)],  # вершина 1
    [(0, 6), (1, 5), (3, 4)],    # вершина 2
    [(1, 15), (2, 4)]     # вершина 3
]
    
parent, key = prim_mst(graph, n)
print("Parent:", parent)  # [0, 2, 0, 2]
print("Key:", key)        # [0, 5, 6, 4]
print("Общий вес MST:", sum(k for k in key if k != float('inf')))

