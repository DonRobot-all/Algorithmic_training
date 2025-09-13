class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float('inf') for _ in range(n)]
        dists[src] = 0

        for _ in range(k+1):
            nxt = dists.copy()
            for i in range(len(flights)):
                u, v, w = flights[i]
                if dists[u] + w < nxt[v]:
                    nxt[v] = dists[u] + w
            dists = nxt
        return dists[dst] if dists[dst] != float('inf') else -1