import collections
import heapq

class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            cur_time, current = heapq.heappop(minHeap)
            if current in visit:
                continue
            visit.add(current)
            t = cur_time
            for place, time_next in edges[current]:
                if place not in visit:
                    heapq.heappush(minHeap, (cur_time + time_next, place))
        return t if len(visit) == n else -1