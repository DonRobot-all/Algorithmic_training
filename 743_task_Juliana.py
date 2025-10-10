from collections import deque, defaultdict
import heapq

def networkDelayTime(times, n, k):
    d = {}
    for start, end, path in times:
        if start not in d:
            d[start] = [(end, path)]
        else:
            d[start].append((end, path))
    d =defaultdict(list)

    for u, v, w in times:
        d[u].append((v, w))
    visited = set()
    t = 0
    min_heap = [(0, k)]
    while min_heap:
        now_t, now_n = heapq.heappop(min_heap)
        if now_n in visited:
            continue
        visited.add(now_n)
        t = now_t
        # if d.get(now_n) != None:
        for neighbors, time in d[now_n]:
            if neighbors not in visited:
                heapq.heappush(min_heap, (time+now_t, neighbors))
    if len(visited) == n:
        return t
    else:
        return -1

print(networkDelayTime(times = [[1,2,1],[2,1,3]], n = 2, k = 2))