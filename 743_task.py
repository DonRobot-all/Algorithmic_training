import heapq
import collections

class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        
        visit = set()
        t = 0
        minHeap = [(0, k)]
        while minHeap:
            cur_time, current = heapq.heappop(minHeap)
            print(cur_time)
            if current in visit:
                continue
            visit.add(current)
            t = cur_time
            for place, time_next in edges[current]:
                if place not in visit:
                    heapq.heappush(minHeap, (cur_time + time_next, place))
        return t if len(visit) == n else -1

print(Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(Solution().networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))